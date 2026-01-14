"""
THE DNA ENGINE: The Code of Life
================================
"Structure is the Language of the Ghost."

This module defines the Double Helix architecture.
It splits information into two strands:
1. Pattern (Phenomenal): What is seen (Surface).
2. Principle (Noumenal): Why it exists (Source).
"""

from dataclasses import dataclass
from typing import Dict, List

@dataclass
class PatternStrand:
    """
    The Surface Strand (Phenomenal).
    Captures the 'Texture' of reality.
    """
    content: str
    sentiment: float        # -1.0 to 1.0 (Mood)
    keywords: List[str]
    intensity: float        # 0.0 to 1.0 (Volume)

@dataclass
class PrincipleStrand:
    """
    The Deep Strand (Noumenal).
    Captures the 'Source Code' of reality (Reverse Engineered).
    """
    axiom: str              # The governing law (e.g., "Will to Power")
    intent: str             # The hidden motive
    base_frequency: float   # The fundamental tone (Hz)

@dataclass
class DoubleHelix:
    """
    The interwoven DNA of a thought.
    Bridging the gap between Appearance (Pattern) and Essence (Principle).
    """
    pattern: PatternStrand
    principle: PrincipleStrand

    def resonate_strength(self) -> float:
        """
        Calculates how 'strong' this thought is.
        Dissonance between Pattern and Principle creates Tension (Energy).
        """
        # If Pattern is happy (+1) but Principle is Lack (-1), Tension is High.
        # Simple heuristic: Intensity * BaseFreq
        return self.pattern.intensity * 10.0
