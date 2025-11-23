"""
Lightweight chemo-sense mapping for Elysia.

Maps scent/flavor names or SMILES strings to Tensor3D + FrequencyWave.
Avoids heavy deps; uses simple heuristics and hash fallback.
"""
from __future__ import annotations

import hashlib
import math
from dataclasses import dataclass
from typing import Optional, Dict

from .math_utils import Vector3
from .tensor import SoulTensor
from .physics import PhysicsState


@dataclass
class ChemoSignature:
    name: str
    soul: SoulTensor
    physics: PhysicsState
    note: str


def _hash_to_freq(value: str) -> float:
    h = int(hashlib.sha256(value.encode("utf-8")).hexdigest(), 16)
    return 200.0 + (h % 600)  # 200-800Hz range


def _make_soul(freq: float, intensity: float) -> SoulTensor:
    # Map frequency to axes: low->X, mid->Y, high->Z
    x = max(0.0, 1.0 - abs(freq - 200.0) / 200.0)
    y = max(0.0, 1.0 - abs(freq - 500.0) / 200.0)
    z = max(0.0, 1.0 - abs(freq - 800.0) / 200.0)
    # Normalize vector
    norm = math.sqrt(x * x + y * y + z * z) or 1.0
    x, y, z = x / norm, y / norm, z / norm
    amplitude = 5.0 + intensity * 5.0
    phase = (freq % 360.0) * math.pi / 180.0
    spin = 1.0 if freq >= 500 else -1.0
    return SoulTensor(amplitude=amplitude, frequency=freq, phase=phase, spin=spin)


def map_chemo(tag: str) -> ChemoSignature:
    """
    Maps a scent/flavor tag (name or SMILES) to a ChemoSignature.
    Known tags are mapped to preset frequencies; unknown tags use hash fallback.
    """
    tag_norm = tag.strip().lower()

    presets: Dict[str, float] = {
        "vanilla": 432.0,
        "rose": 528.0,
        "pepper": 396.0,
        "mint": 741.0,
        "citrus": 640.0,
        "coffee": 350.0,
        "chocolate": 320.0,
        "pheromone": 487.0,
    }

    freq = presets.get(tag_norm) or _hash_to_freq(tag_norm)
    intensity = 0.8 if tag_norm in presets else 0.5
    soul = _make_soul(freq, intensity)

    # Place it in a simple spiral based on freq
    radius = 1.0 + intensity
    physics = PhysicsState()
    physics.position = Vector3(radius * math.cos(freq), 0.0, radius * math.sin(freq))
    physics.mass = soul.amplitude * 0.1

    note = f"Mapped '{tag}' to freq={freq:.1f}Hz, intensity={intensity:.2f}"
    return ChemoSignature(name=tag_norm, soul=soul, physics=physics, note=note)
