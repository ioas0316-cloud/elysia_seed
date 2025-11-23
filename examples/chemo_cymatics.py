"""
Chemo-Cymatics demo:
Maps a scent/flavor tag to a ChemoSignature and prints its Tensor/Soul info.
No external deps required.
"""
from __future__ import annotations

import argparse

from elysia_engine.chemo import map_chemo
from elysia_engine.cymatics import frequency_to_pattern
from examples.cymatics_ascii import render_pattern  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser(description="Chemo-Cymatics demo")
    parser.add_argument("--tag", type=str, default="vanilla", help="scent/flavor tag (name or SMILES-ish)")
    args = parser.parse_args()

    sig = map_chemo(args.tag)
    print(f"[Chemo] {sig.note}")
    print(f" SoulTensor: amp={sig.soul.amplitude:.2f}, freq={sig.soul.frequency:.2f}, phase={sig.soul.phase:.2f}, spin={sig.soul.spin}")
    print(f" Position: {sig.physics.position}, mass={sig.physics.mass:.2f}")

    pattern = frequency_to_pattern(sig.soul.frequency, phase=sig.soul.phase)
    art = render_pattern(pattern, width=60, height=20)
    print("\n[Cymatics Projection]")
    print(art)
    print("\nLegend: 'o'=path, digits=gates")


if __name__ == "__main__":
    main()
