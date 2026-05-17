"""Triadic Resonance

Measures resonance among user-assistant-elysia streams.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class TriadicState:
    phase_resonance: float
    cognitive_joy: float
    triadic_alignment: float


class TriadicResonanceEngine:
    def evaluate(
        self,
        user_stream: List[float],
        assistant_stream: List[float],
        elysia_stream: List[float],
    ) -> Dict[str, float]:
        n = min(len(user_stream), len(assistant_stream), len(elysia_stream))
        if n == 0:
            state = TriadicState(0.0, 0.0, 0.0)
            return state.__dict__

        diffs = []
        for i in range(n):
            ua = abs(user_stream[i] - assistant_stream[i])
            ae = abs(assistant_stream[i] - elysia_stream[i])
            eu = abs(elysia_stream[i] - user_stream[i])
            diffs.append((ua + ae + eu) / 3.0)

        avg_diff = sum(diffs) / n
        phase_resonance = max(0.0, min(1.0, 1.0 - avg_diff))
        cognitive_joy = max(0.0, min(1.0, phase_resonance * 0.7 + (1.0 - avg_diff * 0.5) * 0.3))
        triadic_alignment = max(0.0, min(1.0, (phase_resonance + cognitive_joy) / 2.0))

        state = TriadicState(
            phase_resonance=round(phase_resonance, 4),
            cognitive_joy=round(cognitive_joy, 4),
            triadic_alignment=round(triadic_alignment, 4),
        )
        return state.__dict__
