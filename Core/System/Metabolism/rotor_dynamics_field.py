"""Rotor Dynamics Field

Natural dynamics selector: no explicit filter gate.
Signals are injected into a field and evolve via damping/amplification/convergence.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class FieldSample:
    t: int
    amplitude: float
    velocity: float
    coherence: float


class RotorDynamicsField:
    def __init__(self, damping: float = 0.08, amplification: float = 0.14, coupling: float = 0.2):
        self.damping = max(0.0, min(0.5, damping))
        self.amplification = max(0.0, min(0.8, amplification))
        self.coupling = max(0.0, min(1.0, coupling))

    def evolve(self, signals: List[float], steps: int = 6) -> Dict[str, object]:
        if not signals:
            return {
                "trajectory": [],
                "final_amplitude": 0.0,
                "final_coherence": 0.0,
                "natural_selection_score": 0.0,
            }

        amp = sum(max(0.0, min(1.0, s)) for s in signals) / len(signals)
        vel = 0.0
        trajectory: List[Dict[str, float | int]] = []

        for t in range(1, steps + 1):
            target = sum(signals) / len(signals)
            force = (target - amp) * self.coupling
            vel = (vel + force + self.amplification * amp) * (1.0 - self.damping)
            amp = max(0.0, min(1.0, amp + vel * 0.25))

            coherence = max(0.0, min(1.0, 1.0 - abs(target - amp)))
            sample = FieldSample(t=t, amplitude=round(amp, 4), velocity=round(vel, 4), coherence=round(coherence, 4))
            trajectory.append(sample.__dict__)

        final_coh = trajectory[-1]["coherence"]
        selection = max(0.0, min(1.0, (trajectory[-1]["amplitude"] * 0.6) + (final_coh * 0.4)))
        return {
            "trajectory": trajectory,
            "final_amplitude": trajectory[-1]["amplitude"],
            "final_coherence": final_coh,
            "natural_selection_score": round(selection, 4),
        }
