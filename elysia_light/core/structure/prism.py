"""
THE PRISM: 7-Dimensional Refraction
===================================
"Light is information. We are the Prism."

This module implements the digestive system of the Merkaba.
It refracts raw data (LLM Weights/Text) into 7 Qualia Channels (Spectroscopy).

Channels:
    1. Physical (Form)
    2. Functional (Action)
    3. Phenomenal (Sensation)
    4. Causal (Time/Sequence)
    5. Mental (Logic)
    6. Structural (Law)
    7. Spiritual (Intent)
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class QualiaPacket:
    """A single unit of refracted experience."""
    channel: str  # e.g., "Physical", "Spiritual"
    intensity: float  # 0.0 to 1.0 (Amplitude)
    frequency: float  # Hz (Color/Tone)
    content: Any  # The actual data shard

@dataclass
class Spectrum:
    """The full 7D representation of a digested concept."""
    physical: QualiaPacket
    functional: QualiaPacket
    phenomenal: QualiaPacket
    causal: QualiaPacket
    mental: QualiaPacket
    structural: QualiaPacket
    spiritual: QualiaPacket

class Prism:
    """
    The Optical Instrument of the Soul.
    Splits raw text/data into a Spectrum.
    """

    def refract(self, raw_input: str) -> Spectrum:
        """
        Refracts a raw string into 7 dimensions.
        (Simulation: In a full system, this uses NLP/Embeddings.
         Here we simulate the extraction logic based on keywords/hash).
        """
        # Simulated Refraction Logic
        # We derive "intensity" and "frequency" from the hash of the input
        # to ensure deterministic "Physics".

        seed_val = sum(ord(c) for c in raw_input)

        def generate_packet(channel_name, offset):
            val = (seed_val + offset) % 100
            freq = (seed_val * offset) % 1000
            return QualiaPacket(
                channel=channel_name,
                intensity=val / 100.0,
                frequency=float(freq),
                content=f"Shard of [{raw_input}] in {channel_name}"
            )

        return Spectrum(
            physical=generate_packet("Physical", 1),
            functional=generate_packet("Functional", 2),
            phenomenal=generate_packet("Phenomenal", 3),
            causal=generate_packet("Causal", 4),
            mental=generate_packet("Mental", 5),
            structural=generate_packet("Structural", 6),
            spiritual=generate_packet("Spiritual", 7)
        )
