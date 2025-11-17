from __future__ import annotations

from typing import Any, Dict


def log_snapshot(snapshot: Dict[str, Any]) -> None:
    tick = snapshot.get("tick")
    time_val = float(snapshot.get("time", 0.0))
    entity_count = snapshot.get("entity_count", len(snapshot.get("entities", [])))
    print(f"[tick {tick}] t={time_val:.2f} N={entity_count}")
