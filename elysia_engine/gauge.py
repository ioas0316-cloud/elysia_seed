from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Optional

from .math_utils import Vector3


@dataclass
class ForceConstants:
    """
    기본 상수 모음. 필요하면 World나 System에서 덮어쓴다.
    """
    gravity_G: float = 1.0          # 중력 상수
    coulomb_k: float = 8.99e3       # 축약된 쿨롱 상수 (스케일링 편의용)
    strong_strength: float = 50.0   # 강한핵력 세기
    strong_range: float = 2.0       # 강한핵력 유효 거리
    weak_strength: float = 5.0      # 약한핵력 세기
    weak_range: float = 3.0         # 약한핵력 유효 거리


@dataclass
class ChargeProfile:
    """
    양자/고전 힘 계산에 사용되는 최소 프로필.
    - mass: 중력/관성
    - charge: 전자기력 (양/음)
    - color_charge: 강한핵력 색상(단순 스칼라 매칭으로 시작)
    - spin: 스핀/위상 보정용
    """
    mass: float = 1.0
    charge: float = 0.0
    color_charge: float = 0.0
    spin: float = 1.0
    phase: float = 0.0
    frequency: float = 1.0

    @staticmethod
    def from_soul_tensor(soul: "SoulTensor") -> "ChargeProfile":  # type: ignore[name-defined]
        """
        SoulTensor를 ChargeProfile로 투영.
        - amplitude -> mass
        - polarity -> charge 부호
        - frequency -> 위상/주파수
        - spin -> spin
        """
        from .tensor import SoulTensor  # local import to avoid cycle

        if not isinstance(soul, SoulTensor):
            raise TypeError("Expected SoulTensor")

        return ChargeProfile(
            mass=max(0.1, soul.amplitude),
            charge=soul.polarity,
            color_charge=soul.frequency * 0.01,  # frequency를 색상 대용으로 사용 (스케일 축소)
            spin=soul.spin,
            phase=soul.phase,
            frequency=soul.frequency,
        )


@dataclass
class StarState:
    """
    별 상태(불타는 별 / 얼음별) 간단 표현.
    """
    temperature: float = 1000.0  # 고온일수록 활성
    burning_threshold: float = 500.0

    def is_burning(self) -> bool:
        return self.temperature >= self.burning_threshold

    def is_frozen(self) -> bool:
        return self.temperature < 50.0

    @staticmethod
    def from_soul_tensor(soul: "SoulTensor") -> "StarState":  # type: ignore[name-defined]
        """
        SoulTensor 활성도를 별 온도로 매핑.
        Frequency가 높을수록 뜨겁게, Collapse면 얼어붙은 것으로 본다.
        """
        from .tensor import SoulTensor  # local import to avoid cycle

        if not isinstance(soul, SoulTensor):
            raise TypeError("Expected SoulTensor")

        base_temp = soul.frequency * 10.0
        if soul.is_collapsed:
            base_temp *= 0.1
        # Amplitude가 클수록 추가 발열
        base_temp += soul.amplitude
        return StarState(temperature=base_temp)


class QuantumForceField:
    """
    4대 힘을 통합 계산하는 경량 유틸.
    """

    def __init__(self, constants: Optional[ForceConstants] = None) -> None:
        self.constants = constants or ForceConstants()

    def _direction(self, p1: Vector3, p2: Vector3) -> tuple[Vector3, float]:
        diff = p2 - p1
        dist = diff.magnitude
        if dist < 1e-6:
            return Vector3(0, 0, 0), 1e-6
        return diff.normalize(), dist

    def gravity(self, pos1: Vector3, pos2: Vector3, c1: ChargeProfile, c2: ChargeProfile) -> Vector3:
        dir_vec, dist = self._direction(pos1, pos2)
        magnitude = self.constants.gravity_G * c1.mass * c2.mass / (dist * dist)
        return dir_vec * magnitude

    def electromagnetic(self, pos1: Vector3, pos2: Vector3, c1: ChargeProfile, c2: ChargeProfile) -> Vector3:
        dir_vec, dist = self._direction(pos1, pos2)
        # Coulomb with simple phase-based modulation (동상은 감쇠, 위상차는 증폭)
        base = self.constants.coulomb_k * c1.charge * c2.charge / (dist * dist)
        phase_delta = abs(c1.phase - c2.phase)
        phase_delta = min(phase_delta, 2 * math.pi - phase_delta)
        phase_factor = 0.5 + 0.5 * math.cos(phase_delta)
        return dir_vec * (base * phase_factor)

    def strong(self, pos1: Vector3, pos2: Vector3, c1: ChargeProfile, c2: ChargeProfile) -> Vector3:
        dir_vec, dist = self._direction(pos1, pos2)
        if dist > self.constants.strong_range:
            return Vector3(0, 0, 0)
        color_alignment = 1.0 - abs(c1.color_charge - c2.color_charge)
        color_alignment = max(0.0, color_alignment)
        # Yukawa-style decay
        magnitude = self.constants.strong_strength * color_alignment * math.exp(-dist)
        return dir_vec * magnitude

    def weak(self, pos1: Vector3, pos2: Vector3, c1: ChargeProfile, c2: ChargeProfile) -> Vector3:
        dir_vec, dist = self._direction(pos1, pos2)
        if dist > self.constants.weak_range:
            return Vector3(0, 0, 0)
        # Weak interaction uses spin mismatch as trigger
        spin_factor = abs(c1.spin - c2.spin) + 0.1
        magnitude = self.constants.weak_strength * spin_factor * math.exp(-dist)
        return dir_vec * magnitude

    def total_force(self, pos1: Vector3, pos2: Vector3, c1: ChargeProfile, c2: ChargeProfile) -> Vector3:
        """
        네 힘을 모두 합산. 전자기/중력의 부호에 따라 상쇄 또는 증폭된다.
        """
        f_g = self.gravity(pos1, pos2, c1, c2)
        f_em = self.electromagnetic(pos1, pos2, c1, c2)
        f_s = self.strong(pos1, pos2, c1, c2)
        f_w = self.weak(pos1, pos2, c1, c2)
        return f_g + f_em + f_s + f_w
