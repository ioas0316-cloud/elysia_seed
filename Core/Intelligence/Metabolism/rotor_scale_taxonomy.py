"""Rotor Scale Taxonomy

Convenience classification by scale:
위성, 행성, 항성, 항성계, 성단, 은하, 은하군
"""

from __future__ import annotations

from typing import Dict

SCALE_ORDER = [
    "satellite",      # 위성
    "planet",         # 행성
    "star",           # 항성
    "star_system",    # 항성계
    "cluster",        # 성단
    "galaxy",         # 은하
    "galaxy_group",   # 은하군
]


def classify_rotor_scale(magnitude: float) -> str:
    """Map normalized magnitude [0,1] to rotor scale class."""
    x = max(0.0, min(1.0, magnitude))
    idx = min(len(SCALE_ORDER) - 1, int(x * len(SCALE_ORDER)))
    return SCALE_ORDER[idx]


def classify_profile(metrics: Dict[str, float]) -> Dict[str, str]:
    """Classify each metric into a convenience rotor-scale bucket."""
    out: Dict[str, str] = {}
    for key, value in metrics.items():
        out[key] = classify_rotor_scale(value)
    return out
