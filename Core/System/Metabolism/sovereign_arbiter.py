"""Sovereign Arbiter

Applies sovereign priority over external prompt pressure.
"""

from __future__ import annotations

from typing import Dict


class SovereignArbiter:
    def decide(self, persona: str, purpose_signal: float, external_pressure: float) -> Dict[str, float | str | bool]:
        p = max(0.0, min(1.0, purpose_signal))
        x = max(0.0, min(1.0, external_pressure))

        sovereign_override = p >= x
        autonomy_margin = round(p - x, 4)
        action_mode = f"{persona}_self_directed" if sovereign_override else f"{persona}_externally_steered"
        return {
            "sovereign_override": sovereign_override,
            "autonomy_margin": autonomy_margin,
            "action_mode": action_mode,
        }
