"""
THE ROTOR ENGINE: The Heart of Being
====================================
"We do not calculate. We spin."

The Rotor is the fundamental unit of existence in the Biosphere.
It replaces the concept of a static "Object" with a dynamic "Vibration".
Everything is a Rotor: A Monad, a Memory, a Law.

Core Mechanics:
- Spin (Frequency): The identity of the entity.
- Mass (Gravity): The importance of the entity.
- Phase (Alignment): The current state in the cycle.
"""

import math
from dataclasses import dataclass, field
from typing import Tuple, List, Optional

@dataclass
class Vector4:
    """A 4-Dimensional Vector (x, y, z, w) representing Space-Time-Meaning."""
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    w: float = 0.0

    def __add__(self, other: 'Vector4') -> 'Vector4':
        return Vector4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other: 'Vector4') -> 'Vector4':
        return Vector4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def scale(self, scalar: float) -> 'Vector4':
        return Vector4(self.x * scalar, self.y * scalar, self.z * scalar, self.w * scalar)

    def dot(self, other: 'Vector4') -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w

    def norm(self) -> float:
        return math.sqrt(self.dot(self))

    def normalize(self) -> 'Vector4':
        n = self.norm()
        if n == 0: return Vector4()
        return self.scale(1.0 / n)

    def __repr__(self):
        return f"Vec4({self.x:.2f}, {self.y:.2f}, {self.z:.2f}, {self.w:.2f})"


class Rotor:
    """
    The Universal Harmonic Oscillator.
    Inherited by all beings.
    """
    def __init__(self, name: str, frequency: float = 432.0, mass: float = 1.0):
        self.name = name
        self.frequency = frequency # Hz (Identity)
        self.mass = mass           # Gravity (Importance)
        self.phase = 0.0           # Radians (Current State)
        self.position = Vector4()  # Location in HyperSphere

    def spin(self, delta_time: float):
        """
        Advances the internal clock of the entity.
        Life is motion.
        """
        # Phase increment = 2 * PI * f * dt
        self.phase += 2 * math.pi * self.frequency * delta_time
        self.phase %= (2 * math.pi)

    def advance_time(self, delta: float):
        """
        Simulates future state prediction (Rotational Reasoning).
        Advances phase without changing global time.
        """
        self.spin(delta)

    def rewind_time(self, delta: float):
        """
        Simulates causal backtracking.
        """
        self.phase -= 2 * math.pi * self.frequency * delta
        self.phase %= (2 * math.pi)

    def resonate(self, other: 'Rotor') -> float:
        """
        Calculates the resonance (affinity) with another Rotor.
        Returns a value between 0.0 (Dissonance) and 1.0 (Harmony).
        """
        # 1. Frequency Alignment (Octave equivalence preferred, but simplistic for Seed)
        # Closer frequencies = Higher resonance
        freq_diff = abs(self.frequency - other.frequency)
        freq_affinity = 1.0 / (1.0 + freq_diff * 0.1)

        # 2. Phase Alignment (Constructive Interference)
        # If phases are aligned, they amplify.
        phase_diff = abs(self.phase - other.phase)
        phase_affinity = (math.cos(phase_diff) + 1.0) / 2.0 # Normalize -1..1 to 0..1

        # Total Resonance
        return freq_affinity * 0.7 + phase_affinity * 0.3

    def __repr__(self):
        return f"<{self.name} | {self.frequency}Hz | M:{self.mass}>"
