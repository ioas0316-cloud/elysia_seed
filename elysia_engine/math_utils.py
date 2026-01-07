from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Union


@dataclass
class Vector3:
    """A 3D vector class for spatial calculations."""
    
    x: float
    y: float
    z: float

    @property
    def magnitude(self) -> float:
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> Vector3:
        """Return a unit vector in the same direction."""
        m = self.magnitude
        if m == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / m, self.y / m, self.z / m)

    def __add__(self, other: Vector3) -> Vector3:
        """Add two vectors."""
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector3) -> Vector3:
        """Subtract two vectors."""
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: Union[int, float]) -> Vector3:
        """Multiply vector by a scalar."""
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: Union[int, float]) -> Vector3:
        """Right multiply vector by a scalar."""
        return self.__mul__(scalar)

    def dot(self, other: Vector3) -> float:
        """Calculate the dot product with another vector."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: Vector3) -> Vector3:
        """Calculate the cross product with another vector."""
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def distance_to(self, other: Vector3) -> float:
        """Calculate the distance to another vector."""
        return (self - other).magnitude

    def lerp(self, other: Vector3, t: float) -> Vector3:
        """
        Linear interpolation between this vector and another.
        
        Args:
            other: Target vector
            t: Interpolation factor (0-1)
            
        Returns:
            Interpolated vector
        """
        return Vector3(
            self.x + (other.x - self.x) * t,
            self.y + (other.y - self.y) * t,
            self.z + (other.z - self.z) * t,
        )

    def __repr__(self) -> str:
        return f"Vec3({self.x:.3f}, {self.y:.3f}, {self.z:.3f})"


@dataclass
class Quaternion:
    """A quaternion class for rotations."""
    
    w: float
    x: float
    y: float
    z: float

    @staticmethod
    def identity() -> Quaternion:
        """Return the identity quaternion (no rotation)."""
        return Quaternion(1.0, 0.0, 0.0, 0.0)

    @staticmethod
    def from_axis_angle(axis: Vector3, angle_rad: float) -> Quaternion:
        """
        Create a quaternion from an axis and angle.
        
        Args:
            axis: Rotation axis (will be normalized)
            angle_rad: Rotation angle in radians
            
        Returns:
            Quaternion representing the rotation
        """
        half_angle = angle_rad * 0.5
        s = math.sin(half_angle)
        u = axis.normalize()
        return Quaternion(
            w=math.cos(half_angle),
            x=u.x * s,
            y=u.y * s,
            z=u.z * s,
        )

    def normalize(self) -> Quaternion:
        """Return a normalized quaternion."""
        m = math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)
        if m == 0:
            return Quaternion.identity()
        return Quaternion(self.w / m, self.x / m, self.y / m, self.z / m)

    def conjugate(self) -> Quaternion:
        """Return the conjugate of this quaternion."""
        return Quaternion(self.w, -self.x, -self.y, -self.z)

    def __mul__(self, other: Quaternion) -> Quaternion:
        """Multiply two quaternions (compose rotations)."""
        return Quaternion(
            w=self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z,
            x=self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y,
            y=self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x,
            z=self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w,
        )

    def rotate(self, v: Vector3) -> Vector3:
        """
        Rotate a vector by this quaternion.
        
        Args:
            v: Vector to rotate
            
        Returns:
            Rotated vector
        """
        u = Vector3(self.x, self.y, self.z)
        s = self.w

        uv_dot = u.dot(v)
        term1 = u * (2.0 * uv_dot)

        uu_dot = u.dot(u)
        term2 = v * (s * s - uu_dot)

        cross_uv = u.cross(v)
        term3 = cross_uv * (2.0 * s)

        return term1 + term2 + term3

    def dot(self, other: Quaternion) -> float:
        """Calculate the dot product with another quaternion."""
        return self.w * other.w + self.x * other.x + self.y * other.y + self.z * other.z

    def angular_distance(self, other: Quaternion) -> float:
        """
        Calculate the angular distance to another quaternion.

        Returns the angle in radians (0 to pi).
        Uses the formula: angle = acos((q1 . q2) / (|q1| * |q2|))

        Note: We normalize the inputs to handle non-unit quaternions (Depth != 1).
        We use acos(dot) treating them as 4D vectors for angular separation.
        """
        # Calculate magnitudes squared
        mag_sq1 = self.w**2 + self.x**2 + self.y**2 + self.z**2
        mag_sq2 = other.w**2 + other.x**2 + other.y**2 + other.z**2

        if mag_sq1 == 0 or mag_sq2 == 0:
            return 0.0 # Origin has 0 distance to everything angularly? Or undefined. Let's say 0.

        denom = math.sqrt(mag_sq1 * mag_sq2)

        d = self.dot(other) / denom

        # Clamp to avoid numerical errors
        d = max(-1.0, min(1.0, d))
        return math.acos(d)

    def __repr__(self) -> str:
        return f"Quat({self.w:.3f}, {self.x:.3f}, {self.y:.3f}, {self.z:.3f})"
