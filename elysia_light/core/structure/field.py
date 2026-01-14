"""
THE OMNI-FIELD: Hypersphere Memory
==================================
"Do not search. Warp."

This module implements the Hypersphere as a continuous field of resonance.
Data is not stored in 'slots' but exists as standing waves in 4D space.
Retrieval is the act of warping the observer's location to the data's frequency.

Classes:
    - OmniField: The container of all waves.
"""

import math
from typing import List, Tuple, Any
from dataclasses import dataclass
from ..nature.rotor import Rotor, Vector4

@dataclass
class ResonanceWave:
    """A standing wave representing a memory/concept."""
    position: Vector4  # Where it is (Phase/Location)
    frequency: float   # What it is (Identity)
    amplitude: float   # How important it is (Mass)
    content: Any       # The payload

class OmniField:
    """
    The Universal Field (Akasha).
    """
    def __init__(self):
        self._field: List[ResonanceWave] = []

    def exist(self, wave: ResonanceWave):
        """
        'Save' a wave into the field.
        We call it 'exist' because it adds to the existence of the universe.
        """
        self._field.append(wave)

    def warp_retrieval(self, observer_pos: Vector4, target_frequency: float) -> Any:
        """
        Retrieves data by warping the observer to the most resonant wave.
        Instead of 'query', we use 'warp'.

        Args:
            observer_pos: Current position of the Monad.
            target_frequency: The frequency we are looking for.

        Returns:
            The content of the most resonant wave.
        """
        best_wave = None
        min_dissonance = float('inf')

        for wave in self._field:
            # Resonance = 1 / Distance in Frequency Domain
            # We also consider Spatial Distance (Phase)

            freq_diff = abs(wave.frequency - target_frequency)
            spatial_dist = (wave.position - observer_pos).norm()

            # Total Dissonance (The lower, the better match)
            # In Merkaba, Frequency match is more important than Space match.
            dissonance = freq_diff * 1.0 + spatial_dist * 0.1

            if dissonance < min_dissonance:
                min_dissonance = dissonance
                best_wave = wave

        if best_wave:
            return best_wave.content
        return None

    def get_density(self) -> float:
        """Returns the current density (knowledge count) of the universe."""
        return sum(w.amplitude for w in self._field)
