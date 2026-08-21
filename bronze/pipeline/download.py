"""
MazyOS - download de audio das aulas via Bunny Stream (Kirvano).
Le bronze/catalogo/lessons.json (video_id ja capturado via browser) e baixa
o audio de cada aula com ffmpeg, exigindo o header Referer (hotlink protection
da Bunny CDN). Nao transcreve.

Uso:
  python download.py                 # todas as aulas com video
  python download.py --module 5      # so um modulo (prefixo do module id)
  python download.py --status
"""

import argparse
import json
import os
import re
import subprocess
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, ".."))
CATALOGO = os.path.join(ROOT, "catalogo", "lessons.json")
PROGRESS = os.path.join(BASE, "progress.json")
REFERER = "https://app.kirvano.com/"


def sanitize_filename(name):
    return re.sub(r"[^\w\s-]", "", name).strip().replace(" ", "_")[:80]


def load_catalogo():
    with open(CATALOGO, encoding="utf-8") as f:
        return json.load(f)


def load_progress():
    if os.path.exists(PROGRESS):
        with open(PROGRESS, encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_progress(progress):
    with open(PROGRESS, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def download_audio(video_id, cdn_host, out_path):
    if os.path.exists(out_path):
        print(f"    SKIP (ja existe): {os.path.basename(out_path)}")
        return True
    url = f"https://{cdn_host}/{video_id}/playlist.m3u8"
    print(f"    Baixando {video_id}...")
    result = subprocess.run(
        [
            "ffmpeg", "-y",
            "-headers", f"Referer: {REFERER}",
            "-i", url,
            "-vn", "-acodec", "libmp3lame", "-ab", "128k", "-ar", "16000",
            out_path,
        ],
        capture_output=True, text=True, timeout=1800,
    )
    if result.returncode != 0 or not os.path.exists(out_path):
        print(f"    ERRO ffmpeg: {result.stderr[-300:]}")
        return False
    size_mb = os.path.getsize(out_path) / 1024 / 1024
    print(f"    OK: {size_mb:.1f}MB")
    return True


def print_status(data, progress):
    print(f"\n{'='*60}\n  MAZYOS - PROGRESSO DE DOWNLOAD\n{'='*60}\n")
    total = done = 0
    for mod in data["modules"]:
        vids = [l for l in mod["lessons"] if l.get("video_id")]
        if not vids:
            continue
        n = len(vids)
        d = sum(1 for l in vids if progress.get(l["video_id"], {}).get("downloaded"))
        total += n
        done += d
        print(f"  {mod['title']:45s} {d}/{n}")
    print(f"\n  TOTAL: {done}/{total} baixados\n{'='*60}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--module", type=str, help="prefixo do module id (ex: '5' para calls-gravadas)")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    data = load_catalogo()
    progress = load_progress()

    if args.status:
        print_status(data, progress)
        return

    cdn_host = data["cdn_host"]

    for mod in data["modules"]:
        mod_id = mod["module"]
        if args.module and not mod_id.startswith(args.module):
            continue

        vids = [l for l in mod["lessons"] if l.get("video_id")]
        if not vids:
            continue

        print(f"\n{'='*60}\nMODULO: {mod['title']}\n{'='*60}")
        audio_dir = os.path.join(ROOT, mod_id, "audio")
        os.makedirs(audio_dir, exist_ok=True)

        for lesson in vids:
            title = lesson["title"]
            vid = lesson["video_id"]
            fn = sanitize_filename(title)
            out_path = os.path.join(audio_dir, f"{fn}.mp3")

            print(f"\n  [{vid}] {title}")
            p = progress.get(vid, {})
            if p.get("downloaded"):
                print("    ja baixado")
                continue

            if download_audio(vid, cdn_host, out_path):
                progress[vid] = {"downloaded": True, "module": mod_id, "title": title, "audio_path": out_path}
                save_progress(progress)

    print("\nDONE!")
    print_status(data, progress)


if __name__ == "__main__":
    main()
