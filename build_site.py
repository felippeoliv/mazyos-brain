"""
Gera um site estatico (HTML) para navegar o vault mazyos-brain (README, INDICE,
camada ouro), com a identidade visual do mazyos.com.br: fundo preto, tipografia
SF Pro Display, acento ambar (#FFC86E), botoes em pilula.

Uso:
  python3 build_site.py
Gera tudo em site/. Abra site/index.html no navegador.
"""

import glob
import json
import os
import re
import unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(BASE, "site")
CATALOGO = os.path.join(BASE, "bronze", "catalogo", "lessons.json")


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^\w\s-]", "", s).strip().lower()
    return re.sub(r"[\s_]+", "-", s)


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def find_ouro_file(modulo, titulo):
    """Encontra o arquivo ouro real no disco por comparacao normalizada,
    ja que os nomes de arquivo tiveram pontuacao removida pelos agentes."""
    mod_dir = os.path.join(BASE, "ouro", "aulas", modulo)
    target = norm(titulo)
    best, best_len = None, 0
    for path in glob.glob(os.path.join(mod_dir, "*.md")):
        fn = norm(os.path.splitext(os.path.basename(path))[0])
        if fn in target or target in fn:
            if len(fn) > best_len:
                best, best_len = path, len(fn)
    return best


# ---------------------------------------------------------------- markdown --

def parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_raw = text[3:end].strip("\n")
    body = text[end + 4:].lstrip("\n")
    fm = {}
    for line in fm_raw.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"')
    return fm, body


def inline_md(text, link_resolver):
    # codigo inline
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # wikilinks [[path|label]] ou [[path]]
    def wiki(m):
        target, label = m.group(1), m.group(2)
        if "|" in target:
            target, label = target.split("|", 1)
        if not label:
            label = target
        href = link_resolver(target.strip())
        return f'<a href="{href}">{label.strip()}</a>'
    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", wiki, text)
    # links markdown [text](url)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)
    # negrito / italico
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    return text


def md_to_html(body, link_resolver):
    lines = body.splitlines()
    out = []
    i = 0
    in_ul = in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            close_lists()
            i += 1
            continue

        if stripped == "---":
            close_lists()
            out.append("<hr>")
            i += 1
            continue

        h = re.match(r"^(#{1,4})\s+(.*)", stripped)
        if h:
            close_lists()
            level = len(h.group(1)) + 1  # h1 reservado pro titulo da pagina
            out.append(f"<h{level}>{inline_md(h.group(2), link_resolver)}</h{level}>")
            i += 1
            continue

        if stripped.startswith(">"):
            close_lists()
            block = []
            is_callout = bool(re.match(r"^>\s*\[!\w+\]", stripped))
            while i < len(lines) and lines[i].strip().startswith(">"):
                block.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            block_text = " ".join(block)
            block_text = re.sub(r"^\[!\w+\]\s*", "", block_text)
            cls = "callout" if is_callout else "quote"
            out.append(f'<blockquote class="{cls}">{inline_md(block_text, link_resolver)}</blockquote>')
            continue

        ol = re.match(r"^(\d+)\.\s+(.*)", stripped)
        if ol:
            if not in_ol:
                close_lists()
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{inline_md(ol.group(2), link_resolver)}</li>")
            i += 1
            continue

        ul = re.match(r"^[-*]\s+(.*)", stripped)
        if ul:
            if not in_ul:
                close_lists()
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_md(ul.group(1), link_resolver)}</li>")
            i += 1
            continue

        close_lists()
        out.append(f"<p>{inline_md(stripped, link_resolver)}</p>")
        i += 1

    close_lists()
    return "\n".join(out)


# -------------------------------------------------------------------- HTML --

CSS = """
:root{
  --bg:#000; --bg-raised:#0a0a0c; --bg-card:rgba(255,255,255,.03);
  --border:rgba(255,255,255,.1); --border-soft:rgba(255,255,255,.06);
  --text:#fff; --text-2:rgba(255,255,255,.7); --text-3:rgba(255,255,255,.45);
  --accent:#ffc86e; --accent-dim:rgba(255,200,110,.14);
  --radius:14px; --radius-pill:999px;
}
*{box-sizing:border-box}
html,body{margin:0;padding:0}
body{
  background:var(--bg); color:var(--text);
  font-family:"SF Pro Display",-apple-system,"system-ui","Helvetica Neue",Helvetica,Arial,sans-serif;
  font-size:16px; line-height:1.65; -webkit-font-smoothing:antialiased;
}
a{color:var(--accent); text-decoration:none}
a:hover{text-decoration:underline}
code{
  background:rgba(255,255,255,.08); padding:.15em .4em; border-radius:6px;
  font-family:"SF Mono",Menlo,Consolas,monospace; font-size:.88em; color:var(--accent);
}
hr{border:none; border-top:1px solid var(--border-soft); margin:2.2em 0}

.layout{display:flex; min-height:100vh}

.sidebar{
  width:300px; flex:none; background:var(--bg-raised); border-right:1px solid var(--border-soft);
  padding:28px 22px; position:sticky; top:0; height:100vh; overflow-y:auto;
}
.brand{display:flex; align-items:baseline; gap:8px; margin-bottom:4px}
.brand .mark{font-weight:600; letter-spacing:-.02em}
.brand .sub{font-size:11px; letter-spacing:.12em; text-transform:uppercase; color:var(--text-3)}
.sidebar .tagline{font-size:13px; color:var(--text-3); margin:0 0 26px}

.nav-home{
  display:block; font-size:13px; font-weight:600; color:var(--text);
  padding:8px 10px; margin-bottom:18px; border-radius:8px;
}
.nav-home:hover{background:var(--bg-card); text-decoration:none}

.module{margin-bottom:4px}
.module-title{
  font-size:11px; font-weight:600; letter-spacing:.06em; text-transform:uppercase;
  color:var(--text-3); padding:10px 10px 6px;
}
.module ul{list-style:none; margin:0 0 10px; padding:0}
.module li a{
  display:block; font-size:13.5px; color:var(--text-2); padding:7px 10px;
  border-radius:8px; line-height:1.4;
}
.module li a:hover{background:var(--bg-card); color:var(--text); text-decoration:none}
.module li a.active{background:var(--accent-dim); color:var(--accent)}
.module li a.disabled{color:var(--text-3); pointer-events:none; font-style:italic}

.main{flex:1; min-width:0}
.content{max-width:760px; margin:0 auto; padding:64px 40px 120px}

.eyebrow{
  font-size:12px; font-weight:600; letter-spacing:.1em; text-transform:uppercase;
  color:var(--accent); margin:0 0 14px;
}
h1.page-title{
  font-size:42px; font-weight:500; letter-spacing:-.02em; line-height:1.1; margin:0 0 18px;
}
.meta-bar{
  display:flex; flex-wrap:wrap; gap:8px; margin-bottom:36px;
}
.meta-chip{
  font-size:11.5px; color:var(--text-3); border:1px solid var(--border-soft);
  border-radius:var(--radius-pill); padding:4px 12px;
}

.content h2{font-size:23px; font-weight:600; letter-spacing:-.01em; margin:2.2em 0 .6em}
.content h3{font-size:18px; font-weight:600; margin:1.8em 0 .5em; color:var(--text)}
.content h4{font-size:15px; font-weight:600; margin:1.4em 0 .4em; color:var(--text-2)}
.content p{color:var(--text-2); margin:0 0 1em}
.content li{color:var(--text-2); margin-bottom:.4em}
.content ul,.content ol{padding-left:1.4em; margin:0 0 1.2em}
.content strong{color:var(--text); font-weight:600}

blockquote{
  margin:1.4em 0; padding:16px 20px; border-radius:var(--radius);
  border:1px solid var(--border-soft); background:var(--bg-card);
}
blockquote.callout{border-color:var(--accent-dim); background:rgba(255,200,110,.06)}
blockquote.callout p, blockquote.callout{color:var(--text-2)}
blockquote.quote{font-style:italic; color:var(--text-2); border-left:2px solid var(--accent)}
blockquote p{margin:0}

.pill-link{
  display:inline-block; border:1px solid var(--border); border-radius:var(--radius-pill);
  padding:9px 20px; font-size:13px; font-weight:600; color:var(--text); margin-top:8px;
}
.pill-link:hover{border-color:var(--accent); color:var(--accent); text-decoration:none}

.home-hero{margin-bottom:56px}
.home-hero h1{font-size:56px; font-weight:500; letter-spacing:-.03em; line-height:1.04; margin:0 0 20px}
.home-hero p.lead{font-size:17px; color:var(--text-2); max-width:560px; margin:0 0 28px}

.card-grid{display:grid; grid-template-columns:1fr 1fr; gap:14px; margin:28px 0 44px}
@media (max-width:640px){.card-grid{grid-template-columns:1fr}}
.card{
  border:1px solid var(--border-soft); border-radius:var(--radius); padding:20px;
  background:var(--bg-card);
}
.card .k{font-size:11px; letter-spacing:.08em; text-transform:uppercase; color:var(--text-3); margin-bottom:6px}
.card .v{font-size:26px; font-weight:600; color:var(--accent)}

.module-section{margin-bottom:40px}
.module-section h2{font-size:20px}
.lesson-row{
  display:flex; justify-content:space-between; align-items:center; gap:16px;
  padding:13px 0; border-bottom:1px solid var(--border-soft);
}
.lesson-row a{color:var(--text); font-size:14.5px; font-weight:500}
.lesson-row .dur{color:var(--text-3); font-size:12.5px; white-space:nowrap; font-family:"SF Mono",Menlo,monospace}

footer.page-footer{
  margin-top:60px; padding-top:20px; border-top:1px solid var(--border-soft);
  font-size:12.5px; color:var(--text-3);
}
"""


def page_shell(title, active_href, body_html, depth=0):
    prefix = "../" * depth
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · MazyOS Brain</title>
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<div class="layout">
{render_sidebar(active_href, prefix)}
<div class="main"><div class="content">
{body_html}
</div></div>
</div>
</body>
</html>"""


def render_sidebar(active_href, prefix):
    catalogo = json.load(open(CATALOGO, encoding="utf-8"))
    parts = ['<nav class="sidebar">']
    parts.append('<div class="brand"><span class="mark">MazyOS</span><span class="sub">Brain</span></div>')
    parts.append('<p class="tagline">Base de conhecimento do curso</p>')
    home_cls = "active" if active_href == "index.html" else ""
    parts.append(f'<a class="nav-home {home_cls}" href="{prefix}index.html">&larr; Visão geral</a>')

    for mod in catalogo["modules"]:
        parts.append('<div class="module">')
        parts.append(f'<div class="module-title">{mod["title"]}</div><ul>')
        for lesson in mod["lessons"]:
            slug = slugify(lesson["title"])
            href = f'{prefix}aulas/{mod["module"]}/{slug}.html'
            active = "active" if href.replace(prefix, "") == active_href else ""
            if lesson.get("video_id"):
                parts.append(f'<li><a class="{active}" href="{href}">{lesson["title"]}</a></li>')
            else:
                parts.append(f'<li><a class="disabled" href="#">{lesson["title"]} (texto)</a></li>')
        parts.append("</ul></div>")
    parts.append("</nav>")
    return "\n".join(parts)


def build_lesson_pages():
    catalogo = json.load(open(CATALOGO, encoding="utf-8"))
    count = 0
    for mod in catalogo["modules"]:
        mod_dir = os.path.join(SITE, "aulas", mod["module"])
        os.makedirs(mod_dir, exist_ok=True)
        for lesson in mod["lessons"]:
            if not lesson.get("video_id"):
                continue
            ouro_path = find_ouro_file(mod["module"], lesson["title"])
            if not ouro_path:
                print("faltando:", mod["module"], lesson["title"])
                continue
            raw = open(ouro_path, encoding="utf-8").read()
            fm, body = parse_frontmatter(raw)
            # remove o "# Titulo" inicial do corpo (ja renderizamos como h1.page-title)
            body = re.sub(r"^#\s+.*\n+", "", body, count=1)

            def resolver(target, mod=mod):
                return f"../{mod['module']}/{slugify(target.split('/')[-1])}.html" if "ouro/aulas" in target else "#"

            html_body = md_to_html(body, resolver)

            duracao = lesson.get("duration")
            fonte_prata = fm.get("fonte_prata", "")
            meta_chips = f'<span class="meta-chip">{mod["title"]}</span>'
            if duracao:
                meta_chips += f'<span class="meta-chip">{duracao}</span>'
            meta_chips += '<span class="meta-chip">Camada ouro</span>'

            page = f"""<p class="eyebrow">{mod["title"]}</p>
<h1 class="page-title">{lesson["title"]}</h1>
<div class="meta-bar">{meta_chips}</div>
{html_body}
<footer class="page-footer">Transcrição integral em <code>{fonte_prata}</code> &middot; áudio original em <code>bronze/{mod["module"]}/audio/</code></footer>
"""
            slug = slugify(lesson["title"])
            active_href = f'aulas/{mod["module"]}/{slug}.html'
            html = page_shell(lesson["title"], active_href, page, depth=2)
            with open(os.path.join(mod_dir, slug + ".html"), "w", encoding="utf-8") as f:
                f.write(html)
            count += 1
    return count


def build_index():
    catalogo = json.load(open(CATALOGO, encoding="utf-8"))
    readme = open(os.path.join(BASE, "README.md"), encoding="utf-8").read()
    fm, body = parse_frontmatter(readme)
    body = re.sub(r"^#\s+.*\n+", "", body, count=1)

    total_lessons = sum(1 for m in catalogo["modules"] for l in m["lessons"] if l.get("video_id"))

    cards = f"""<div class="card-grid">
  <div class="card"><div class="k">Aulas em vídeo</div><div class="v">{total_lessons}</div></div>
  <div class="card"><div class="k">Duração total</div><div class="v">~10h</div></div>
  <div class="card"><div class="k">Módulos</div><div class="v">{len(catalogo["modules"])}</div></div>
  <div class="card"><div class="k">Transcrição</div><div class="v">100% local</div></div>
</div>"""

    modules_html = []
    for mod in catalogo["modules"]:
        rows = []
        for lesson in mod["lessons"]:
            if lesson.get("video_id"):
                slug = slugify(lesson["title"])
                href = f'aulas/{mod["module"]}/{slug}.html'
                dur = lesson.get("duration", "")
                rows.append(f'<div class="lesson-row"><a href="{href}">{lesson["title"]}</a><span class="dur">{dur}</span></div>')
            else:
                rows.append(f'<div class="lesson-row"><span style="color:var(--text-3);font-style:italic">{lesson["title"]} (texto, sem vídeo)</span></div>')
        modules_html.append(f'<div class="module-section"><h2>{mod["title"]}</h2>{"".join(rows)}</div>')

    def resolver(target):
        return "#"

    body_html = md_to_html(body, resolver)

    page = f"""<p class="eyebrow">MazyOS &middot; Sistema Operacional</p>
<div class="home-hero">
<h1>Base de conhecimento<br>do curso, destilada.</h1>
<p class="lead">23 aulas transcritas localmente e processadas em três camadas &mdash; do áudio cru ao conhecimento pronto pra consultar. Comece pelos módulos abaixo.</p>
{cards}
</div>
{''.join(modules_html)}
<hr>
<h2>Sobre esta base</h2>
{body_html}
"""
    html = page_shell("Visão geral", "index.html", page, depth=0)
    with open(os.path.join(SITE, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)


def main():
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    with open(os.path.join(SITE, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(CSS)
    n = build_lesson_pages()
    build_index()
    print(f"Site gerado em {SITE} ({n} aulas + index.html)")


if __name__ == "__main__":
    main()
