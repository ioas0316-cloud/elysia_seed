"""
Curiosity one-shot driver.

Pipeline:
- (optional) record a curiosity request
- (optional) ingest a reviewed text file
- resolve requests -> knowledge.jsonl
- sync knowledge into the KG

Usage:
python scripts/curiosity_run_all.py --concept "topic" --file path/to/clean.txt --detail "context note"

You can skip steps with the provided flags.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import curiosity_apply_ingest
import curiosity_loop
import curiosity_sync_to_kg


def main() -> None:
    parser = argparse.ArgumentParser(description="Run curiosity pipeline end-to-end.")
    parser.add_argument("--concept", required=True, help="topic/concept to learn")
    parser.add_argument("--detail", default="", help="extra detail for the request record")
    parser.add_argument(
        "--file",
        type=Path,
        help="reviewed UTF-8 text to ingest for the concept (optional if already ingested)",
    )
    parser.add_argument("--skip-request", action="store_true", help="do not append to requests.jsonl")
    parser.add_argument("--skip-ingest", action="store_true", help="do not append to ingested.jsonl")
    parser.add_argument("--skip-sync", action="store_true", help="stop after knowledge.jsonl is produced")
    args = parser.parse_args()

    if not args.skip_request:
        curiosity_loop.do_request(args.concept, args.detail)
    if args.file and not args.skip_ingest:
        curiosity_loop.do_ingest(args.concept, args.file)

    curiosity_apply_ingest.apply()

    if not args.skip_sync:
        curiosity_sync_to_kg.sync()

    print("[curiosity-run] complete.")


if __name__ == "__main__":
    main()
