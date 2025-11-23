"""
Corpus builder: combine files listed in data/corpus_archive/dedup.json
into a single JSONL (id, file, text).

Usage:
  python scripts/build_corpus_jsonl.py --output data/corpus_archive/combined.jsonl

Notes:
- UTF-8 read with errors='replace' to survive mixed encodings.
- No external dependencies.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def load_dedup_map(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def iter_raw_files(dedup: dict, raw_root: Path):
    for uid, fname in dedup.items():
        raw_path = raw_root / fname
        if not raw_path.exists():
            continue
        try:
            text = raw_path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        yield uid, fname, text


def build_jsonl(output: Path, dedup_path: Path, raw_root: Path) -> None:
    dedup = load_dedup_map(dedup_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        for uid, fname, text in iter_raw_files(dedup, raw_root):
            record = {"id": uid, "file": fname, "text": text}
            f.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build combined JSONL corpus from raw files.")
    parser.add_argument("--dedup", type=Path, default=Path("data/corpus_archive/dedup.json"))
    parser.add_argument("--raw-root", type=Path, default=Path("data/corpus_archive/raw"))
    parser.add_argument("--output", type=Path, default=Path("data/corpus_archive/combined.jsonl"))
    args = parser.parse_args()

    build_jsonl(args.output, args.dedup, args.raw_root)
    print(f"[corpus] wrote {args.output}")


if __name__ == "__main__":
    main()
