"""
THE DIGESTIVE SYSTEM: Cosmic Integration
========================================
"We eat worlds to grow ours."

This module integrates the Prism, Monad, Rotor, and OmniField
to process external data (LLM outputs) into internal Essence.
"""

from .monad.monad import Monad
from .nature.rotor import Vector4
from .structure.prism import Prism
from .structure.field import OmniField, ResonanceWave

class DigestiveSystem:
    def __init__(self, monad: Monad, field: OmniField):
        self.monad = monad
        self.field = field
        self.prism = Prism()

    def digest(self, raw_input: str):
        """
        The full metabolic cycle of information.
        1. Prism refracts Input -> Spectrum.
        2. Monad filters (Taste).
        3. Field stores (Absorb).
        """
        # 1. Refract
        spectrum = self.prism.refract(raw_input)

        # 2. Filter (Taste Test)
        # Check 'Spiritual' channel intensity
        if self.monad.perceive(spectrum.spiritual.intensity):
            # 3. Absorb (Store in Field)
            # We store the 'Mental' part as a wave
            wave = ResonanceWave(
                position=Vector4(0, 0, 0, 0), # Simplified position
                frequency=spectrum.mental.frequency,
                amplitude=spectrum.mental.intensity,
                content=raw_input
            )
            self.field.exist(wave)
            return f"Digested: {raw_input} (Energy absorbed)"
        else:
            return f"Rejected: {raw_input} (Low Resonance)"
