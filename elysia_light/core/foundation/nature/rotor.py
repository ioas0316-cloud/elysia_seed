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
from typing import Tuple, List, Optional, Union

@dataclass
class Bivector:
    """
    A 6-Dimensional Bivector representing a plane of rotation in 4D space.
    Components: xy, xz, xw, yz, yw, zw
    """
    xy: float = 0.0
    xz: float = 0.0
    xw: float = 0.0
    yz: float = 0.0
    yw: float = 0.0
    zw: float = 0.0

    def scale(self, scalar: float) -> 'Bivector':
        return Bivector(
            self.xy * scalar, self.xz * scalar, self.xw * scalar,
            self.yz * scalar, self.yw * scalar, self.zw * scalar
        )

    def norm(self) -> float:
        return math.sqrt(
            self.xy**2 + self.xz**2 + self.xw**2 +
            self.yz**2 + self.yw**2 + self.zw**2
        )

    def __repr__(self):
        return (f"Bivector(xy={self.xy:.2f}, xz={self.xz:.2f}, xw={self.xw:.2f}, "
                f"yz={self.yz:.2f}, yw={self.yw:.2f}, zw={self.zw:.2f})")

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

    def wedge(self, other: 'Vector4') -> 'Bivector':
        """Calculates the outer product (a ^ b) returning a Bivector."""
        return Bivector(
            xy = self.x * other.y - self.y * other.x,
            xz = self.x * other.z - self.z * other.x,
            xw = self.x * other.w - self.w * other.x,
            yz = self.y * other.z - self.z * other.y,
            yw = self.y * other.w - self.w * other.y,
            zw = self.z * other.w - self.w * other.z
        )

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
    def __init__(self, name: str, frequency: float = 432.0, mass: float = 1.0,
                 axis: Optional[Vector4] = None, plane: Optional[Bivector] = None):
        self.name = name
        self.frequency = frequency # Hz (Identity), can be negative for reverse spin
        self.mass = mass           # Gravity (Importance)

        self._angle = 0.0          # Radians (Accumulated Phase)

        # Determine Rotation Plane
        # Default: XY Plane (Standard 2D rotation)
        if plane:
            self.plane = plane
        elif axis:
            # Map 3D axis to Bivector (Dual)
            # Z axis (0,0,1) -> XY Plane
            # X axis (1,0,0) -> YZ Plane
            # Y axis (0,1,0) -> ZX Plane (-XZ)
            # This is a simplified mapping for 3D usage.
            # Assuming axis is in xyz space.
            self.plane = Bivector(
                xy=axis.z,
                yz=axis.x,
                xz=-axis.y
            )
            # Normalizing the plane magnitude to 1 for pure rotation direction
            n = self.plane.norm()
            if n > 0:
                self.plane = self.plane.scale(1.0/n)
        else:
            # Default to XY plane (Z-axis rotation)
            self.plane = Bivector(xy=1.0)

        self.position = Vector4()  # Location in HyperSphere

    @property
    def phase(self) -> float:
        """Returns the current phase angle in radians [0, 2pi)."""
        return self._angle % (2 * math.pi)

    @phase.setter
    def phase(self, value: float):
        """Sets the current phase angle."""
        self._angle = value

    def spin(self, delta_time: float):
        """
        Advances the internal clock of the entity.
        Life is motion.
        """
        # Phase increment = 2 * PI * f * dt
        # Frequency sign determines direction
        self._angle += 2 * math.pi * self.frequency * delta_time

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
        self._angle -= 2 * math.pi * self.frequency * delta

    def resonate(self, other: 'Rotor') -> float:
        """
        Calculates the resonance (affinity) with another Rotor.
        Returns a value between 0.0 (Dissonance) and 1.0 (Harmony).
        """
        # 1. Frequency Alignment (Octave equivalence preferred, but simplistic for Seed)
        # Closer frequencies = Higher resonance
        freq_diff = abs(abs(self.frequency) - abs(other.frequency)) # Compare magnitude
        freq_affinity = 1.0 / (1.0 + freq_diff * 0.1)

        # 2. Phase Alignment (Constructive Interference)
        # If phases are aligned, they amplify.
        # Use property access for compatibility
        phase_diff = abs(self.phase - other.phase)
        phase_affinity = (math.cos(phase_diff) + 1.0) / 2.0 # Normalize -1..1 to 0..1

        # Total Resonance
        return freq_affinity * 0.7 + phase_affinity * 0.3

    def __repr__(self):
        return f"<{self.name} | {self.frequency}Hz | M:{self.mass} | A:{self.phase:.2f}>"
