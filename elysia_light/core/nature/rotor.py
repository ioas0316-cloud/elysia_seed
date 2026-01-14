"""
THE ROTOR: Engine of Causality
==============================
"We do not calculate. We spin."

The Rotor is the implementation of Time and Operation in the Merkaba System.
It replaces linear logic (Chain of Thought) with Rotational Reasoning (Spin).
It uses Geometric Algebra (Spinors) to rotate concepts in high-dimensional space
until they align with the Truth (Resonance).

Classes:
    - Rotor: A geometric operator for 4D spacetime rotation.
"""

import math
from dataclasses import dataclass
from typing import Tuple, Union, List

@dataclass
class Vector4:
    """A 4-Dimensional Vector (x, y, z, w)."""
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
    A Rotor represents a rotation in 4D space using Geometric Algebra (Even Subalgebra).
    It is composed of a Scalar (Grade 0) and a Bivector (Grade 2).

    Structure: R = a + B
    where a is scalar, B is bivector (xy, xz, xw, yz, yw, zw).
    """
    def __init__(self, a: float = 1.0,
                 b_xy: float = 0.0, b_xz: float = 0.0, b_xw: float = 0.0,
                 b_yz: float = 0.0, b_yw: float = 0.0, b_zw: float = 0.0):
        self.a = a
        # Bivector components
        self.b_xy = b_xy
        self.b_xz = b_xz
        self.b_xw = b_xw
        self.b_yz = b_yz
        self.b_yw = b_yw
        self.b_zw = b_zw

    @staticmethod
    def from_angle_plane(angle_rad: float, plane: str = 'xy') -> 'Rotor':
        """Creates a rotor representing a rotation by 'angle' in a specific plane."""
        half_angle = angle_rad / 2.0
        c = math.cos(half_angle)
        s = math.sin(half_angle)

        if plane == 'xy': return Rotor(c, b_xy=s)
        if plane == 'xz': return Rotor(c, b_xz=s)
        if plane == 'xw': return Rotor(c, b_xw=s)
        if plane == 'yz': return Rotor(c, b_yz=s)
        if plane == 'yw': return Rotor(c, b_yw=s)
        if plane == 'zw': return Rotor(c, b_zw=s)
        return Rotor(c)

    def __mul__(self, other: 'Rotor') -> 'Rotor':
        """
        Geometric Product of two Rotors (R1 * R2).
        Composition of rotations.
        (Simplified implementation for core planes).
        """
        # Note: Full GA product is complex.
        # For the Seed, we approximate by summing phases if aligning,
        # or implement a simplified composition for the 'Spirit' of rotation.
        # Here we implement a simplified scalar + bivector addition for "Spin accumulation"
        # In a full engine, this would be the complete Geometric Product.

        # Real implementation of Rotor product is:
        # R = R1 R2
        new_a = self.a * other.a \
                - self.b_xy * other.b_xy - self.b_xz * other.b_xz - self.b_xw * other.b_xw \
                - self.b_yz * other.b_yz - self.b_yw * other.b_yw - self.b_zw * other.b_zw

        # Simplified Bivector parts (First order approximation for small angles or orthogonal planes)
        # Detailed product logic is extensive. We will treat this as "Accumulating Spin".
        new_xy = self.a*other.b_xy + self.b_xy*other.a
        new_xz = self.a*other.b_xz + self.b_xz*other.a
        new_xw = self.a*other.b_xw + self.b_xw*other.a
        new_yz = self.a*other.b_yz + self.b_yz*other.a
        new_yw = self.a*other.b_yw + self.b_yw*other.a
        new_zw = self.a*other.b_zw + self.b_zw*other.a

        return Rotor(new_a, new_xy, new_xz, new_xw, new_yz, new_yw, new_zw)

    def rotate(self, v: Vector4) -> Vector4:
        """
        Rotates a vector v using the sandwich product: v' = R v ~R
        This allows 4D rotation without gimbal lock.
        """
        # For the Seed, we implement a symbolic "Spin" that affects the Vector.
        # Implementing full R v ~R for 4D is verbous.
        # We will focus on the 'xy' (logic) and 'zw' (spirit) planes for the demo.

        # 1. XY Rotation (Logic Plane)
        x_new = v.x * self.a - v.y * self.b_xy
        y_new = v.x * self.b_xy + v.y * self.a

        # 2. ZW Rotation (Spirit Plane)
        z_new = v.z * self.a - v.w * self.b_zw
        w_new = v.z * self.b_zw + v.w * self.a

        # Normalize to maintain magnitude (Unitary rotation)
        # In full GA, magnitude is preserved naturally. Here we approximate.
        res = Vector4(x_new, y_new, z_new, w_new)
        original_mag = v.norm()
        current_mag = res.norm()

        if current_mag > 0:
            res = res.scale(original_mag / current_mag)

        return res

    def spin_to_collapse(self, state: Vector4, target_resonance: float) -> Tuple[Vector4, int]:
        """
        The Core Logic of Rotational Reasoning.
        Instead of calculating a path, we spin the state until it resonates.

        Args:
            state: The current concept vector.
            target_resonance: The desired frequency/value.

        Returns:
            (Collapsed State, RPM required)
        """
        rpm = 0
        current_state = state

        # We spin until the 'Z' (Truth) axis aligns or we hit a limit
        # This simulates "Thinking" as "Spinning"
        while rpm < 100:
            # Check resonance (e.g., closeness to target on Z axis)
            resonance = abs(current_state.z - target_resonance)
            if resonance < 0.1:
                break

            # Spin! (Apply rotation)
            # We rotate in the ZW plane (Spirit/Time) to find the answer
            spin_rotor = Rotor.from_angle_plane(0.1, 'zw') # Spin by 0.1 rad
            current_state = spin_rotor.rotate(current_state)

            # Accumulate "Heat" (RPM)
            rpm += 1

        return current_state, rpm

    def __repr__(self):
        return f"Rotor(Scalar={self.a:.2f}, SpinXY={self.b_xy:.2f}, SpinZW={self.b_zw:.2f})"
