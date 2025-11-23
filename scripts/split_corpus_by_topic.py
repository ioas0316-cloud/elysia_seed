"""
Split combined corpus into coarse topics with simple heuristics.

Reads data/corpus_archive/combined.jsonl (or --input) and writes
data/corpus_archive/by_topic/<topic>.jsonl with metadata:
{"id", "file", "text", "topic", "lang"}.

No external deps; language is guessed by presence of Korean characters.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from collections import defaultdict


def guess_lang(text: str) -> str:
    if re.search(r"[가-힣]", text):
        return "ko"
    return "en"


def guess_topic(fname: str) -> str:
    name = fname.lower()
    if any(k in name for k in ["ml_", "system_design", "nlp", "readme", "hands_on_ml", "vcd"]):
        return "tech"
    if any(k in name for k in ["covid", "data.json"]):
        return "data"
    if any(k in name for k in ["shakespeare", "wuxia", "literature"]):
        return "literature"
    if any(k in name for k in ["ai", "guide", "tutorial", "intro"]):
        return "guide"
    return "misc"


def split_corpus(input_path: Path, output_root: Path) -> None:
    output_root.mkdir(parents=True, exist_ok=True)
    buckets: dict[str, list[dict]] = defaultdict(list)

    with input_path.open("r", encoding="utf-8") as f:
        for line in f:
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            fname = record.get("file", "")
            text = record.get("text", "")
            topic = guess_topic(fname)
            lang = guess_lang(text)
            buckets[topic].append(
                {
                    "id": record.get("id"),
                    "file": fname,
                    "text": text,
                    "topic": topic,
                    "lang": lang,
                }
            )

    for topic, items in buckets.items():
        out_path = output_root / f"{topic}.jsonl"
        with out_path.open("w", encoding="utf-8") as out:
            for rec in items:
                out.write(json.dumps(rec, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Split combined corpus into topic JSONL files.")
    parser.add_argument("--input", type=Path, default=Path("data/corpus_archive/combined.jsonl"))
    parser.add_argument("--output-root", type=Path, default=Path("data/corpus_archive/by_topic"))
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"Input not found: {args.input}")

    split_corpus(args.input, args.output_root)
    print(f"[corpus] wrote topics to {args.output_root}")


if __name__ == "__main__":
    main()
