"""Purpose Accrual

Accrues intent vector over time from action/feedback cycles.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class PurposeState:
    intent: float
    will: float
    direction: float


class PurposeAccrual:
    def __init__(self):
        self.state = PurposeState(intent=0.5, will=0.5, direction=0.5)

    def update(self, success: float, resonance: float, fatigue: float) -> Dict[str, float]:
        s = max(0.0, min(1.0, success))
        r = max(0.0, min(1.0, resonance))
        f = max(0.0, min(1.0, fatigue))

        self.state.intent = max(0.0, min(1.0, self.state.intent * 0.7 + s * 0.3))
        self.state.will = max(0.0, min(1.0, self.state.will * 0.65 + r * 0.35))
        self.state.direction = max(0.0, min(1.0, self.state.direction * 0.6 + ((s + r) / 2.0) * 0.3 + (1 - f) * 0.1))

        purpose_signal = (self.state.intent * 0.4) + (self.state.will * 0.35) + (self.state.direction * 0.25)
        return {
            "intent": round(self.state.intent, 4),
            "will": round(self.state.will, 4),
            "direction": round(self.state.direction, 4),
            "purpose_signal": round(purpose_signal, 4),
        }
