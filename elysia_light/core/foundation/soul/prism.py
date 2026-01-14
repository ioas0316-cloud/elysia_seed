"""
THE PRISM ENGINE: The Soul's Mirror
===================================
"We do not see the world. We see our reflection."

The Prism converts raw sensory data (Text) into Wave DNA (Rotor).
It performs the "Transduction" process.
"""

from ..nature.rotor import Rotor

class Prism:
    """
    Refracts raw data into Rotors.
    """

    def refract(self, raw_input: str) -> Rotor:
        """
        Converts text into a Rotor with specific Frequency and Mass.
        """
        # 1. Frequency Analysis (Hash-to-Freq)
        # "The meaning" -> specific Hz
        seed_val = sum(ord(c) for c in raw_input)
        frequency = float(seed_val % 1000) + 100.0 # Base 100Hz

        # 2. Mass Analysis (Length/Complexity)
        mass = len(raw_input) / 10.0

        # 3. Create the Wave Form
        # The name is the content itself (or a summary)
        name = raw_input[:20] + "..." if len(raw_input) > 20 else raw_input

        return Rotor(name, frequency, mass)
