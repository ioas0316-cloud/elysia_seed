"""Phase Boundary Learning

Learns boundary through phase inversion and phase-difference restoration.
When inner/outer streams are both perceived, boundary state is updated.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class BoundaryState:
    boundary_clarity: float
    inversion_stability: float
    restoration_coherence: float


class PhaseBoundaryLearner:
    """Topological reverse-learning prototype for sovereign boundary formation."""

    def __init__(self, sensitivity: float = 0.5):
        self.sensitivity = max(0.1, min(1.0, sensitivity))

    def learn(self, inner_stream: List[float], outer_stream: List[float], timesteps: int = 4) -> Dict[str, object]:
        n = min(len(inner_stream), len(outer_stream))
        if n == 0:
            state = BoundaryState(0.0, 0.0, 0.0)
            return {"timeline": [], "final": state.__dict__}

        timeline = []
        for t in range(1, timesteps + 1):
            ratio = t / timesteps
            diffs = [abs(inner_stream[i] - outer_stream[i]) for i in range(n)]
            mean_diff = sum(diffs) / n

            inversion = [1.0 - min(1.0, d) for d in diffs]
            inversion_stability = sum(inversion) / n

            restoration = [
                max(0.0, 1.0 - (abs((inner_stream[i] + outer_stream[i]) * 0.5 - inner_stream[i]) * self.sensitivity))
                for i in range(n)
            ]
            restoration_coherence = sum(restoration) / n

            boundary_clarity = max(0.0, min(1.0, (mean_diff * 0.6) + (restoration_coherence * 0.4 * ratio)))
            timeline.append(
                {
                    "t": t,
                    "boundary_clarity": round(boundary_clarity, 4),
                    "inversion_stability": round(inversion_stability, 4),
                    "restoration_coherence": round(restoration_coherence, 4),
                }
            )

        final = BoundaryState(
            boundary_clarity=timeline[-1]["boundary_clarity"],
            inversion_stability=timeline[-1]["inversion_stability"],
            restoration_coherence=timeline[-1]["restoration_coherence"],
        )
        return {
            "timesteps": timesteps,
            "timeline": timeline,
            "final": final.__dict__,
        }
