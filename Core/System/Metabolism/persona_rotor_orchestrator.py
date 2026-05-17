"""Persona Rotor Orchestrator

Chooses active persona rotor based on clock dynamics.
"""

from __future__ import annotations

from typing import Dict


class PersonaRotorOrchestrator:
    PERSONAS = ("work", "rest", "play", "reflect")

    def select(self, energy_tick: float, momentum_tick: float, recovery_tick: float) -> Dict[str, float | str]:
        e = max(0.0, min(1.0, energy_tick))
        m = max(0.0, min(1.0, momentum_tick))
        r = max(0.0, min(1.0, recovery_tick))

        scores = {
            "work": (e * 0.5) + (m * 0.5),
            "rest": (r * 0.7) + ((1 - m) * 0.3),
            "play": (e * 0.5) + ((1 - r) * 0.5),
            "reflect": (r * 0.4) + (m * 0.2) + ((1 - e) * 0.4),
        }
        active = max(scores, key=scores.get)
        return {
            "active_persona": active,
            "active_score": round(scores[active], 4),
            **{f"score_{k}": round(v, 4) for k, v in scores.items()},
        }
