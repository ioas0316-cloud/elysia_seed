from __future__ import annotations

import math
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

from .math_utils import Quaternion


@dataclass
class SoulTensor:
    """
    Tensor3D: The Unified Field of Existence.
    Replaces QuantumDNA and static Physics with a unified Wave-Field definition.

    Axes:
        1. Amplitude (Body/Mass): The Magnitude/Intensity of the being. Creates Gravity.
        2. Frequency (Soul/Identity): The Color/Type of the being. Defines the 'Rifling' pitch.
        3. Phase (Spirit/Timing): The Alignment/Rhythm. Defines interaction chemistry.

    New Axis (Hypersphere Decoupling):
        4. Orientation (Hypersphere): The 'Attitude' or 'Facing' of the soul.
           Determines the Intent Vector (Volition) separate from Position.

    Attributes:
        amplitude: Body/Mass - Energy intensity (float)
        frequency: Soul/Identity - Vibration rate (float)
        phase: Spirit/Timing - Phase angle in radians (0 to 2π)
        spin: Direction of spiral (+1 or -1)
        polarity: Matter (1.0) vs Antimatter (-1.0)
        orientation: The facing direction of the soul (Quaternion)
        is_collapsed: Wave function collapse state
        coherence: Quantum coherence (1.0 = pure quantum, 0.0 = classical)
    """

    amplitude: float  # Body: Mass, Energy, Intensity
    frequency: float  # Soul: Emotion, Identity, Vibration Rate
    phase: float      # Spirit: Timing, Perspective (0 to 2pi)
    spin: float = 1.0 # Rifling: Direction of the spiral (+1 or -1)
    polarity: float = 1.0 # Matter (1.0) vs Antimatter (-1.0)
    orientation: Quaternion = field(default_factory=Quaternion.identity) # Hypersphere Orientation
    is_collapsed: bool = False # Wave Function Collapse State
    coherence: float = 1.0 # Quantum coherence (1.0 = pure quantum, 0.0 = classical)

    # Quantum Properties
    entangled_peers: List[SoulTensor] = field(default_factory=list, repr=False)
    superposition_states: List[Tuple[SoulTensor, float]] = field(default_factory=list, repr=False)

    def step(self, dt: float) -> None:
        """
        Evolve the wave state over time.
        Phase rotates: d(phi)/dt = frequency
        Unless collapsed (Ice Star), where phase is locked.
        """
        if self.is_collapsed:
            return

        delta = self.frequency * dt
        self.phase += delta
        self.phase %= (2 * math.pi)

        # Decoherence
        decoherence_rate = 0.001 * (1 + self.amplitude * 0.01)
        self.coherence = max(0.0, self.coherence - decoherence_rate * dt)

        for peer in self.entangled_peers:
            if not peer.is_collapsed:
                peer.phase = self.phase

    def entangle(self, other: 'SoulTensor') -> None:
        if other not in self.entangled_peers:
            self.entangled_peers.append(other)
        if self not in other.entangled_peers:
            other.entangled_peers.append(self)

        avg_phase = (self.phase + other.phase) / 2
        self.phase = avg_phase
        other.phase = avg_phase

    def resonate(self, other: SoulTensor) -> Dict[str, Any]:
        """
        Calculates the 'Chemistry' between two souls.
        """
        delta_phase = abs(self.phase - other.phase)
        if delta_phase > math.pi:
            delta_phase = (2 * math.pi) - delta_phase

        resonance = math.cos(delta_phase)
        polarity_factor = self.polarity * other.polarity
        resonance *= polarity_factor

        freq_diff = abs(self.frequency - other.frequency)
        is_harmonic = freq_diff < (self.frequency * 0.1) if self.frequency != 0 else False

        interaction_type = "Neutral"
        if resonance > 0.5:
            interaction_type = "Constructive (Empathy/Love)"
        elif resonance < -0.5:
            interaction_type = "Destructive (Calm/Comfort)"
        else:
            interaction_type = "Complex (Tension/Beat)"

        return {
            "resonance": resonance,
            "delta_phase": delta_phase,
            "is_harmonic": is_harmonic,
            "type": interaction_type
        }

    def decode_emotion(self) -> str:
        if self.frequency < 20:
            base = "Deep Sorrow / Gravity (Blue)"
        elif 20 <= self.frequency < 50:
            base = "Peace / Trust (Green)"
        elif 50 <= self.frequency < 100:
            base = "Joy / Excitement (Yellow)"
        elif 100 <= self.frequency < 300:
            base = "Passion / Anger (Red)"
        else:
            base = "Transcendence / Anxiety (White/Violet)"

        if self.amplitude < 10:
            intensity = "Faint"
        elif 10 <= self.amplitude < 50:
            intensity = "Clear"
        elif 50 <= self.amplitude < 200:
            intensity = "Strong"
        else:
            intensity = "Overwhelming"

        return f"{intensity} {base}"

    def as_dict(self) -> Dict[str, Any]:
        return {
            "amplitude": self.amplitude,
            "frequency": self.frequency,
            "phase": self.phase,
            "spin": self.spin,
            "polarity": self.polarity,
            "orientation": str(self.orientation),
            "is_collapsed": self.is_collapsed,
            "coherence": self.coherence,
            "emotion": self.decode_emotion()
        }
