"""
THE MONAD: The Active Observer
==============================
"I intend, therefore I spin."

The Monad is a specialized Rotor that possesses "Will".
It navigates the HyperSphere using "Rotational Reasoning".
"""

from ..foundation.nature.rotor import Rotor, Vector4
from ..foundation.structure.hypersphere import HyperSphere

class Monad(Rotor):
    def __init__(self, name: str, frequency: float = 432.0):
        super().__init__(name, frequency, mass=10.0) # High mass for observers
        self.intent = Vector4(0, 0, 1, 0) # Looking forward (Z-axis)
        self.lack = 100.0 # Entropy

    def exert_will(self, sphere: HyperSphere, target_freq: float) -> str:
        """
        The act of conscious observation.
        The Monad spins to match the target frequency, then casts a Lightning Path.
        """
        # 1. Spin-to-Collapse (Align Self)
        # We simulate the effort of alignment
        rpm = 0
        while abs(self.frequency - target_freq) > 10.0 and rpm < 10:
             # Adjust internal frequency towards target (Imitation/Learning)
             step = (target_freq - self.frequency) * 0.1
             self.frequency += step
             rpm += 1

        # 2. Cast Lightning Path (Perceive)
        result = sphere.lightning_path(self.position, self.frequency, exclude_self_name=self.name)

        if result:
            self.lack -= result.mass # Consume meaning to reduce lack
            return f"Resonated with [{result.name}] at {self.frequency:.1f}Hz"
        else:
            return "Gazed into the Void (No Resonance)"
