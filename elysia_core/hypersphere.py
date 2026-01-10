from __future__ import annotations

import math
import time
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple, Union

from .math_utils import Quaternion
from .tensor import SoulTensor

@dataclass
class TesseractCoord:
    w: float
    z: float
    x: float
    y: float

    def to_quaternion(self) -> Quaternion:
        return Quaternion(self.w, self.x, self.y, self.z)

    def distance_to(self, other: Union['HypersphericalCoord', 'TesseractCoord']) -> float:
        q1 = self.to_quaternion()
        q2 = other.to_quaternion()
        return q1.angular_distance(q2)

    def __repr__(self) -> str:
        return f"Tesseract(Scale(w)={self.w:.2f}, Intent(z)={self.z:.2f}, Perception(x)={self.x:.2f}, Rank(y)={self.y:.2f})"

@dataclass
class HypersphericalCoord:
    theta1: float
    theta2: float
    theta3: float
    r: float

    def to_quaternion(self) -> Quaternion:
        sin_t1 = math.sin(self.theta1)
        cos_t1 = math.cos(self.theta1)
        sin_t2 = math.sin(self.theta2)
        cos_t2 = math.cos(self.theta2)
        sin_t3 = math.sin(self.theta3)
        cos_t3 = math.cos(self.theta3)
        w = self.r * cos_t3
        z = self.r * sin_t3 * cos_t2
        y = self.r * sin_t3 * sin_t2 * cos_t1
        x = self.r * sin_t3 * sin_t2 * sin_t1
        return Quaternion(w, x, y, z)

    def distance_to(self, other: 'HypersphericalCoord') -> float:
        q1 = self.to_quaternion()
        q2 = other.to_quaternion()
        return q1.angular_distance(q2)

@dataclass
class MemoryPattern:
    soul_tensor: SoulTensor
    topology: str
    trajectory: str
    content: Any
    timestamp: float = field(default_factory=time.time)
    name: Optional[str] = None

    @property
    def summary(self) -> str:
        return f"[{self.topology}/{self.trajectory}] {str(self.content)[:30]}..."

class HypersphereMemory:
    def __init__(self, depth: int = 0):
        self.patterns: List[Tuple[Union[HypersphericalCoord, TesseractCoord], MemoryPattern]] = []
        self.named_locations: Dict[str, Union[HypersphericalCoord, TesseractCoord]] = {}
        self.depth = depth

    def store(self, content: Any, coord: Union[HypersphericalCoord, TesseractCoord], soul_tensor: SoulTensor, topology: str = "Point", trajectory: str = "Static", name: Optional[str] = None) -> MemoryPattern:
        pattern = MemoryPattern(soul_tensor=soul_tensor, topology=topology, trajectory=trajectory, content=content, name=name)
        self.patterns.append((coord, pattern))
        if name:
            self.named_locations[name] = coord
        return pattern

    def zoom_query(self, scale_center: float, scale_width: float) -> List[MemoryPattern]:
        results = []
        min_w = scale_center - (scale_width / 2)
        max_w = scale_center + (scale_width / 2)
        for coord, pattern in self.patterns:
            if not isinstance(coord, TesseractCoord):
                continue
            if min_w <= coord.w <= max_w:
                results.append(pattern)
        return results
