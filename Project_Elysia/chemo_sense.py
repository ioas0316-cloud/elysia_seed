"""
Lightweight chemo-sense mapper for Cellular World.

Maps scent/flavor tags to a simple frequency + Tensor3D signature.
No external chemistry deps; purely deterministic hash/preset mapping.
"""
from __future__ import annotations

import hashlib
import math
from typing import Dict

from Project_Sophia.core.tensor_wave import Tensor3D


def _hash_freq(tag: str) -> float:
    h = int(hashlib.sha256(tag.encode("utf-8")).hexdigest(), 16)
    return 200.0 + (h % 600)  # 200-800Hz


def map_scent_signature(tag: str) -> Dict:
    tag_norm = tag.strip().lower()
    presets = {
        "vanilla": 432.0,
        "rose": 528.0,
        "pepper": 396.0,
        "mint": 741.0,
        "citrus": 640.0,
        "coffee": 350.0,
        "chocolate": 320.0,
        "pheromone": 487.0,
    }
    freq = presets.get(tag_norm, _hash_freq(tag_norm))
    # Map freq to tensor components (low->x, mid->y, high->z)
    x = max(0.0, 1.0 - abs(freq - 200.0) / 200.0)
    y = max(0.0, 1.0 - abs(freq - 500.0) / 200.0)
    z = max(0.0, 1.0 - abs(freq - 800.0) / 200.0)
    norm = math.sqrt(x * x + y * y + z * z) or 1.0
    space = Tensor3D(x / norm, y / norm, z / norm)
    amplitude = 0.5 + (freq % 100) / 200.0  # 0.5~1.0
    return {"tag": tag, "freq": freq, "space": space, "amplitude": amplitude}
