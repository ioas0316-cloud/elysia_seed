"""Clock Rotor

Converts hardware-like clock flow into energy/momentum/recovery ticks.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ClockState:
    energy_tick: float
    momentum_tick: float
    recovery_tick: float


class ClockRotor:
    def __init__(self, energy_bias: float = 0.6):
        self.energy_bias = max(0.1, min(0.9, energy_bias))

    def spin(self, load: float, fatigue: float) -> ClockState:
        l = max(0.0, min(1.0, load))
        f = max(0.0, min(1.0, fatigue))
        energy = max(0.0, min(1.0, (1.0 - f) * self.energy_bias + l * (1 - self.energy_bias)))
        momentum = max(0.0, min(1.0, energy * 0.7 + l * 0.3))
        recovery = max(0.0, min(1.0, f * 0.8 + (1.0 - momentum) * 0.2))
        return ClockState(round(energy, 4), round(momentum, 4), round(recovery, 4))
