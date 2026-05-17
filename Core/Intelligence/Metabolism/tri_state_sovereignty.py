"""Tri-State Sovereignty Engine

Tri-state cognition:
1) defined world
2) undefined world
3) boundary self

Provides expansion while preserving sovereign continuity.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class TriState:
    defined_world: float
    undefined_world: float
    boundary_self: float


class TriStateSovereigntyEngine:
    def __init__(self, expansion_gain: float = 1.2, stability_bias: float = 0.7):
        self.expansion_gain = max(1.0, expansion_gain)
        self.stability_bias = max(0.1, min(1.0, stability_bias))

    def evaluate(self, defined_signal: float, undefined_signal: float, identity_signal: float) -> Dict[str, float]:
        defined = max(0.0, min(1.0, defined_signal))
        undefined = max(0.0, min(1.0, undefined_signal * (self.expansion_gain / 1.5)))
        boundary = max(0.0, min(1.0, (identity_signal * self.stability_bias) + (abs(defined - undefined) * (1 - self.stability_bias))))

        freedom_expansion = max(0.0, min(1.0, (defined + undefined) / 2.0))
        sovereign_stability = max(0.0, min(1.0, boundary))
        balance_gate = max(0.0, min(1.0, (freedom_expansion * 0.55) + (sovereign_stability * 0.45)))

        state = TriState(defined_world=defined, undefined_world=undefined, boundary_self=boundary)
        return {
            **state.__dict__,
            "freedom_expansion": round(freedom_expansion, 4),
            "sovereign_stability": round(sovereign_stability, 4),
            "balance_gate": round(balance_gate, 4),
        }
