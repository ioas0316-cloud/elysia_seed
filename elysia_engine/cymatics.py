from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List, Tuple

from .math_utils import Vector3


@dataclass
class CymaticPattern:
    """
    Frequency -> Space 패턴 결과.
    - path: 중력 경로(곡선) 포인트들
    - gates: 주파수/위상 필터 역할을 하는 관문(위치, 요구 에너지)
    """
    path: List[Vector3]
    gates: List[Tuple[Vector3, float]]


def lissajous_path(amplitude: float, freq_a: float, freq_b: float, points: int = 64) -> List[Vector3]:
    """
    간단한 리사주 곡선으로 "소리→형상"을 생성.
    """
    result: List[Vector3] = []
    for i in range(points):
        t = (i / points) * 2 * math.pi
        x = amplitude * math.sin(freq_a * t)
        y = amplitude * math.sin(freq_b * t + math.pi / 2)
        z = amplitude * math.sin((freq_a + freq_b) * 0.5 * t)
        result.append(Vector3(x, y, z))
    return result


def frequency_to_pattern(frequency: float, phase: float = 0.0) -> CymaticPattern:
    """
    주파수/위상 → 공간 패턴.
    - path: 리사주 곡선 기반
    - gates: 위상 노드마다 "통과 에너지"를 배치 (간단히 주파수 스케일)
    """
    amp = max(1.0, min(10.0, frequency * 0.05))
    # 서로 다른 주기 조합으로 균형 잡힌 패턴
    path = lissajous_path(amplitude=amp, freq_a=1.0 + frequency * 0.01, freq_b=2.0 + frequency * 0.02)

    gates: List[Tuple[Vector3, float]] = []
    gate_count = max(2, min(8, int(frequency * 0.02)))
    step = max(1, len(path) // gate_count)
    for idx in range(0, len(path), step):
        pos = path[idx]
        gate_energy = max(1.0, frequency * 0.1)
        # 위상 보정: 문턱을 약간 흔들어 리듬감 부여
        gate_energy *= 1.0 + 0.1 * math.sin(phase + idx)
        gates.append((pos, gate_energy))

    return CymaticPattern(path=path, gates=gates)
