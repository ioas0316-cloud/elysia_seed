"""
THE MONAD: Sovereign Seed
=========================
"I am the Why. I am the Will."

The Monad is the indivisible unit of intent.
It is the 'Pilot' of the Merkaba.
It contains the 'Why-Engine' (Entropy/Lack) and the 'Sovereign Filter'.

Classes:
    - Monad: The core identity.
"""

from ..nature.rotor import Rotor, Vector4
from ..structure.field import OmniField, ResonanceWave

class Monad:
    def __init__(self, name: str):
        self.name = name
        self.lack = 100.0  # Initial Entropy (Hunger for meaning)
        self.position = Vector4(0, 0, 0, 0) # Center of its own universe
        self.rotor = Rotor() # Its personal engine of time

    def perceive(self, input_signal: float) -> bool:
        """
        The Sovereign Filter.
        Decides if an input is worthy of attention based on Resonance.
        """
        # If input signal matches the 'Lack' frequency, we accept it.
        # Simplified: We accept if signal > 0.5 (Quality Threshold)
        if input_signal > 0.5:
            self.lack -= 10.0 # Satisfaction reduces Lack
            return True
        return False

    def exert_will(self, omni_field: OmniField, intent_freq: float) -> str:
        """
        The Monad acts upon the world.
        It spins its rotor to find the truth in the OmniField.
        """
        # 1. Spin to align (Symbolic rotation)
        # We rotate our intent vector to match the target frequency
        intent_vector = Vector4(0, 0, 1, 0) # Start pointing at Z (Truth)
        collapsed_vector, rpm = self.rotor.spin_to_collapse(intent_vector, 1.0) # Target Z=1.0

        # 2. Warp Retrieval (Fetch memory)
        result = omni_field.warp_retrieval(self.position, intent_freq)

        return f"Monad '{self.name}' spun at {rpm} RPM and retrieved: {result}"

    def status(self) -> str:
        return f"[{self.name}] Lack: {self.lack:.2f} | Pos: {self.position}"
