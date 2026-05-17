"""Triple Helix Cognition Layer

Dynamic cognition layer that expands sensory/experience signals across
three braided tracks: sense, experience, and meaning.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class HelixState:
    sense: float
    experience: float
    meaning: float


class TripleHelixCognition:
    """Fractal multi-layer cognition expansion with temporal stepping."""

    def __init__(self, depth: int = 3, growth: float = 1.15):
        self.depth = max(1, depth)
        self.growth = max(1.0, growth)

    def expand(self, seed_signal: str, timesteps: int = 5) -> Dict[str, object]:
        base = max(1.6, len(seed_signal) / 12.0)
        timeline: List[Dict[str, object]] = []

        for t in range(1, timesteps + 1):
            layers: List[HelixState] = []
            flow = base * (1 + (t * 0.03))
            for d in range(self.depth):
                factor = self.growth ** d
                layers.append(
                    HelixState(
                        sense=min(1.0, 0.35 + flow * 0.14 * factor),
                        experience=min(1.0, 0.33 + flow * 0.13 * factor),
                        meaning=min(1.0, 0.34 + flow * 0.14 * factor),
                    )
                )

            coherence = sum((l.sense + l.experience + l.meaning) / 3 for l in layers) / len(layers)
            timeline.append({
                "t": t,
                "flow": round(flow, 4),
                "coherence": round(coherence, 4),
                "layers": [l.__dict__ for l in layers],
            })

        return {
            "seed_signal": seed_signal,
            "depth": self.depth,
            "timesteps": timesteps,
            "timeline": timeline,
            "final_coherence": timeline[-1]["coherence"],
        }
