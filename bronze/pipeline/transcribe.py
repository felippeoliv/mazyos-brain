"""
MazyOS - transcricao local via whisper.cpp (whisper-cli), sem custo de API.
Le progress.json (aulas baixadas por download.py) e transcreve cada audio,
salvando o JSON bruto do whisper-cli em bronze/<modulo>/transcripts/.

Requer: whisper-cli (brew install whisper-cpp) e o modelo em
bronze/pipeline/models/ggml-large-v3-turbo.bin (baixado previamente).

Uso:
  python transcribe.py
  python transcribe.py --module 5
  python transcribe.py --status
"""

import argparse
import json
import os
import re
import subprocess

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, ".."))
PROGRESS = os.path.join(BASE, "progress.json")
MODEL = os.path.join(BASE, "models", "ggml-large-v3-turbo.bin")


def sanitize_filename(name):
    return re.sub(r"[^\w\s-]", "", name).strip().replace(" ", "_")[:80]


def load_progress():
    with open(PROGRESS, encoding="utf-8") as f:
        return json.load(f)


def save_progress(progress):
    with open(PROGRESS, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def transcribe(audio_path, out_json_noext):
    out_path = out_json_noext + ".json"
    if os.path.exists(out_path):
        print(f"    SKIP (ja existe): {os.path.basename(out_path)}")
        return True

    print(f"    Transcrevendo {os.path.basename(audio_path)}...")
    result = subprocess.run(
        [
            "whisper-cli", "-m", MODEL, "-l", "pt",
            "-np",  # suprime print por segmento (aulas longas geram milhares de linhas)
            "-oj", "-of", out_json_noext,
            audio_path,
        ],
        capture_output=True, text=True, timeout=7200,
    )
    if result.returncode != 0 or not os.path.exists(out_path):
        print(f"    ERRO whisper-cli: {result.stderr[-300:]}")
        return False
    print("    OK")
    return True


def print_status(progress):
    total = sum(1 for p in progress.values() if p.get("downloaded"))
    done = sum(1 for p in progress.values() if p.get("transcribed"))
    print(f"\n  TOTAL: {done}/{total} transcritas\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--module", type=str, help="prefixo do modulo (filtra por progress[].module)")
    ap.add_argument("--status", action="store_true")
    args = ap.parse_args()

    progress = load_progress()

    if args.status:
        print_status(progress)
        return

    if not os.path.exists(MODEL):
        print(f"ERRO: modelo nao encontrado em {MODEL}")
        return

    for video_id, p in progress.items():
        if not p.get("downloaded"):
            continue
        if args.module and not p.get("module", "").startswith(args.module):
            continue
        if p.get("transcribed"):
            continue

        title = p["title"]
        mod = p["module"]
        audio_path = p["audio_path"]
        fn = sanitize_filename(title)
        transcripts_dir = os.path.join(ROOT, mod, "transcripts")
        os.makedirs(transcripts_dir, exist_ok=True)
        out_noext = os.path.join(transcripts_dir, fn)

        print(f"\n  [{video_id}] {title}")
        if transcribe(audio_path, out_noext):
            p["transcribed"] = True
            p["transcript_path"] = out_noext + ".json"
            save_progress(progress)

    print("\nDONE!")
    print_status(progress)


if __name__ == "__main__":
    main()
