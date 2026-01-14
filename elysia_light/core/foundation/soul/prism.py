"""
THE PRISM ENGINE: The Soul's Mirror
===================================
"We do not see the world. We see our reflection."

The Prism converts raw sensory data (Text) into Wave DNA (Rotor).
It performs the "Transduction" process.
"""

from ..nature.rotor import Rotor
from .dna import DoubleHelix

class Prism:
    """
    Refracts raw data into Rotors.
    Now aligns with the 4-Step Causal Chain.
    Phase 3: Supports Double Helix DNA Refraction.
    """

    def refract(self, raw_input) -> Rotor:
        """
        Converts Input (Text or DNA) into a Rotor.
        """
        if isinstance(raw_input, DoubleHelix):
            return self._refract_dna(raw_input)

        # Legacy String Support
        return self._refract_string(raw_input)

    def _refract_dna(self, dna: DoubleHelix) -> Rotor:
        """
        Phase 3: The Helical Interference Logic.
        Mixes Pattern and Principle to create a specific Vibration.
        """
        # 1. Principle provides the Base Frequency (The Key)
        base_freq = dna.principle.base_frequency

        # 2. Pattern modulates the Frequency (The Melody)
        # Positive sentiment shifts freq up (Light), Negative down (Heavy)
        # Shift range: +/- 50 Hz based on intensity
        modulation = dna.pattern.sentiment * dna.pattern.intensity * 50.0

        final_freq = base_freq + modulation

        # 3. Mass is derived from the "Truth Weight" (Resonance Strength)
        mass = dna.resonate_strength()

        # Name reflects intent
        name = f"Thought_{dna.principle.intent}"

        return Rotor(name, final_freq, mass)

    def _refract_string(self, raw_input: str) -> Rotor:
        """Legacy Logic"""
        seed_val = sum(ord(c) for c in raw_input)
        frequency = float(seed_val % 1000) + 100.0
        mass = len(raw_input) / 10.0
        name = raw_input[:20] + "..." if len(raw_input) > 20 else raw_input
        return Rotor(name, frequency, mass)
