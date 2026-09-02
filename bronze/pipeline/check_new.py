"""MazyOS - checa se ha aulas novas na Kirvano comparando com o catalogo local.

Usa o Chrome de pipeline (perfil ~/.chrome-edj, CDP na porta 9222), que precisa
estar logado na Kirvano (login manual, uma vez; a sessao fica salva no perfil).
Se o Chrome nao estiver rodando, este script sobe um em modo headless.

A area de membros fica em https://app.kirvano.com/lessons/<course_uuid>
(o caminho antigo /members-area/<uuid> foi descontinuado pela Kirvano).

Uso:
  .venv/bin/python check_new.py            # so relata (exit 0 = sem novidade, 1 = tem aula nova)
  .venv/bin/python check_new.py --write    # alem de relatar, adiciona as aulas novas em lessons.json
  .venv/bin/python check_new.py --notify   # manda notificacao do macOS se houver novidade

Dependencia: websocket-client (pip install websocket-client, de preferencia
num venv em bronze/pipeline/.venv).
"""

import argparse
import json
import os
import re
import subprocess
import sys
import time
import unicodedata
import urllib.request

import websocket

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, ".."))
CATALOGO = os.path.join(ROOT, "catalogo", "lessons.json")
DEBUG = "http://localhost:9222"
PROFILE = os.path.expanduser("~/.chrome-edj")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

_id = [0]


def cdp_send(ws, method, params=None):
    _id[0] += 1
    mid = _id[0]
    ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get("id") == mid:
            return msg.get("result", msg)


def debug_alive():
    try:
        with urllib.request.urlopen(DEBUG + "/json/version", timeout=3):
            return True
    except Exception:
        return False


def ensure_chrome(headless):
    if debug_alive():
        return None
    args = [CHROME, f"--user-data-dir={PROFILE}", "--remote-debugging-port=9222",
            "--no-first-run", "--window-size=1400,900"]
    if headless:
        args.insert(1, "--headless=new")
    proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    for _ in range(30):
        if debug_alive():
            return proc
        time.sleep(1)
    raise RuntimeError("Chrome de debug nao subiu na porta 9222")


def page_ws():
    with urllib.request.urlopen(DEBUG + "/json") as r:
        tabs = [t for t in json.load(r) if t["type"] == "page"
                and not t["url"].startswith(("chrome", "about:", "devtools"))]
    if not tabs:
        raise RuntimeError("nenhuma aba de pagina no Chrome de debug")
    return websocket.create_connection(tabs[0]["webSocketDebuggerUrl"], timeout=60, suppress_origin=True)


def evaluate(ws, js):
    res = cdp_send(ws, "Runtime.evaluate", {"expression": js, "returnByValue": True, "awaitPromise": True})
    return res.get("result", {}).get("value")


def sidebar_text(ws):
    return evaluate(ws, "(document.querySelector('aside')||document.body).innerText") or ""


def expand_modules(ws):
    """Expande os modulos ainda colapsados (os que o parse ve com 0 aulas)."""
    for _ in range(20):
        modules = parse_sidebar(sidebar_text(ws))
        pending = [m["title"] for m in modules if not m["lessons"]]
        if not pending:
            return
        title = pending[0]
        ok = evaluate(ws, f"""(()=>{{
          const hs=Array.from(document.querySelectorAll('div,p')).filter(e=>{{
            const ls=(e.innerText||'').trim().split('\\n');
            return ls.length===2 && ls[0]==={json.dumps(title)} && /^\\d+ conteúdos?$/.test(ls[1]);
          }});
          const h=hs[hs.length-1]; if(!h) return false;
          const btn=h.closest('button,[role=button]'); if(!btn) return false;
          btn.click();
          return true;
        }})()""")
        if not ok:
            return
        time.sleep(1.2)


def parse_sidebar(text):
    """Converte o innerText da sidebar em [{title, lessons:[{title,type}]}]."""
    lines = [ln.strip() for ln in text.split("\n")]
    lines = [ln for ln in lines if ln]
    modules = []
    cur = None
    i = 0
    while i < len(lines):
        ln = lines[i]
        if ln in ("Comentários", "Marcar como assistido"):
            break
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if re.fullmatch(r"\d+ conteúdos?", nxt):
            cur = {"title": ln, "lessons": []}
            modules.append(cur)
            i += 2
            continue
        if cur is not None and nxt in ("Vídeo", "Texto") and not re.fullmatch(r"\d+", ln):
            cur["lessons"].append({"title": ln, "type": nxt})
            i += 2
            continue
        i += 1
    return modules


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="adiciona aulas novas em lessons.json (sem video_id)")
    ap.add_argument("--notify", action="store_true", help="notificacao do macOS se houver novidade")
    ap.add_argument("--no-headless", action="store_true")
    args = ap.parse_args()

    with open(CATALOGO, encoding="utf-8") as f:
        cat = json.load(f)
    course = cat["course_uuid"]
    known = {norm(l["title"]) for m in cat["modules"] for l in m["lessons"]}
    known_modules = {norm(m["title"]) for m in cat["modules"]}

    proc = ensure_chrome(headless=not args.no_headless)
    try:
        ws = page_ws()
        cdp_send(ws, "Page.enable")
        cdp_send(ws, "Page.navigate", {"url": f"https://app.kirvano.com/lessons/{course}"})
        for _ in range(20):
            time.sleep(2)
            if "conteúdo" in sidebar_text(ws):
                break
        url = evaluate(ws, "location.href")
        if "/lessons/" not in (url or ""):
            print(f"ERRO: caiu em {url} - sessao da Kirvano provavelmente expirou.")
            print("Abra o Chrome do pipeline e faca login de novo:")
            print(f'  "{CHROME}" --user-data-dir={PROFILE} https://app.kirvano.com')
            sys.exit(2)
        expand_modules(ws)
        modules = parse_sidebar(sidebar_text(ws))
        ws.close()
    finally:
        if proc:
            proc.terminate()

    if not modules:
        print("ERRO: nao consegui ler a lista de modulos (layout mudou?).")
        sys.exit(2)

    news = []
    for m in modules:
        for l in m["lessons"]:
            if norm(l["title"]) not in known:
                news.append({"module": m["title"], **l, "new_module": norm(m["title"]) not in known_modules})

    total_remote = sum(len(m["lessons"]) for m in modules)
    print(f"Kirvano: {len(modules)} modulos, {total_remote} conteudos. Catalogo: {len(known)} conteudos.")
    if not news:
        print("Sem aulas novas.")
        sys.exit(0)

    print(f"\n{len(news)} conteudo(s) novo(s):")
    for n in news:
        flag = " [MODULO NOVO]" if n["new_module"] else ""
        print(f"  - [{n['module']}]{flag} {n['title']} ({n['type']})")

    if args.write:
        for n in news:
            mod = next((m for m in cat["modules"] if norm(m["title"]) == norm(n["module"])), None)
            if mod is None:
                slug = re.sub(r"[^a-z0-9]+", "-", norm(n["module"])).strip("-")
                mod = {"module": f"{len(cat['modules'])}-{slug}", "title": n["module"], "lessons": []}
                cat["modules"].append(mod)
            mod["lessons"].append({"order": len(mod["lessons"]) + 1, "title": n["title"],
                                   "video_id": None, "type": n["type"]})
        with open(CATALOGO, "w", encoding="utf-8") as f:
            json.dump(cat, f, ensure_ascii=False, indent=2)
        print("\nlessons.json atualizado (video_id fica null; capture com o /atualizar do Claude).")

    if args.notify:
        subprocess.run(["osascript", "-e",
                        f'display notification "{len(news)} aula(s) nova(s) no MazyOS. Rode: claude /atualizar no mazyos-brain" with title "mazyos-brain"'])
    sys.exit(1)


if __name__ == "__main__":
    main()
