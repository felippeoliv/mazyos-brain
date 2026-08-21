"""
Gera a camada PRATA do vault MazyOS: um markdown por aula, com frontmatter
e transcricao integral em blocos de ~75s com timestamp.

Le o JSON nativo do whisper-cli (transcription[].offsets.from/to em ms).

Uso:
  python gen_prata.py --dry-run
  python gen_prata.py
"""

import argparse
import json
import os
import re
import shutil

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(BASE, ".."))
PRATA = os.path.join(ROOT, "..", "prata")
CATALOGO = os.path.join(ROOT, "catalogo", "lessons.json")
PROGRESS = os.path.join(BASE, "progress.json")


def safe_title_filename(title):
    t = re.sub(r'[<>:"/\\|?*]', "", title).strip()
    return re.sub(r"\s+", " ", t)[:120]


def ts(seconds):
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def blocks_from_segments(segments, max_block=75.0, gap_break=1.5, min_block=30.0):
    blocks = []
    cur, cur_start, prev_end = [], None, None
    for s in segments:
        if cur_start is None:
            cur_start = s["start"]
        if prev_end is not None:
            dur = prev_end - cur_start
            if (s["start"] - prev_end >= gap_break and dur >= min_block) or dur >= max_block:
                blocks.append((cur_start, " ".join(cur)))
                cur, cur_start = [], s["start"]
        cur.append(s["text"].strip())
        prev_end = s["end"]
    if cur:
        blocks.append((cur_start, " ".join(cur)))
    return blocks


def load_whisper_segments(transcript_path):
    data = json.load(open(transcript_path, encoding="utf-8"))
    segments = []
    for item in data.get("transcription", []):
        segments.append({
            "start": item["offsets"]["from"] / 1000.0,
            "end": item["offsets"]["to"] / 1000.0,
            "text": item["text"],
        })
    return segments


def render(title, mod_title, mod_id, video_id, transcript_path, duration):
    segments = load_whisper_segments(transcript_path)
    lines = [
        "---",
        f'titulo: "{title}"',
        f"curso: MazyOS",
        f"modulo: {mod_title}",
        f"modulo_slug: {mod_id}",
        f'video_id: "{video_id}"',
        f"duracao: {duration or 'desconhecida'}",
        "camada: prata",
        "fonte: transcricao automatica (whisper.cpp, ggml-large-v3-turbo, local, pt)",
        f"transcript_bronze: bronze/{mod_id}/transcripts/{os.path.basename(transcript_path)}",
        "tags: [mazyos, transcricao]",
        "---",
        "",
        f"# {title}",
        "",
        "> [!info] Camada prata: transcrição integral e fiel ao áudio, em blocos com timestamp. O conhecimento destilado vive na camada ouro.",
        "",
    ]
    for start, text in blocks_from_segments(segments):
        text = re.sub(r"\s+", " ", text).strip()
        if text:
            lines.append(f"**[{ts(start)}]** {text}")
            lines.append("")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    catalogo = json.load(open(CATALOGO, encoding="utf-8"))
    progress = json.load(open(PROGRESS, encoding="utf-8")) if os.path.exists(PROGRESS) else {}

    mod_lookup = {m["module"]: m["title"] for m in catalogo["modules"]}

    if not args.dry_run and os.path.isdir(PRATA):
        shutil.rmtree(PRATA)

    written = skipped = 0
    for mod in catalogo["modules"]:
        for lesson in mod["lessons"]:
            vid = lesson.get("video_id")
            if not vid:
                continue
            p = progress.get(vid, {})
            if not p.get("transcribed"):
                print(f"[SEM TRANSCRIPT] {mod['title']} | {lesson['title']}")
                skipped += 1
                continue

            title = lesson["title"]
            out_dir = os.path.join(PRATA, mod["module"])
            out = os.path.join(out_dir, safe_title_filename(title) + ".md")

            if args.dry_run:
                print(f"{mod['module']}  <-  {title}")
            else:
                os.makedirs(out_dir, exist_ok=True)
                content = render(
                    title, mod["title"], mod["module"], vid,
                    p["transcript_path"], lesson.get("duration"),
                )
                with open(out, "w", encoding="utf-8") as f:
                    f.write(content)
                written += 1

    print(f"\narquivos gerados: {written} | sem transcript: {skipped}")


if __name__ == "__main__":
    main()
