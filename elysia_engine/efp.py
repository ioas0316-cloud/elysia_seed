from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass
class EFPState:
    """최소 E/F/P 내핵."""

    energy: float = 0.0
    force: float = 0.0
    momentum: float = 0.0

    def step(self, dt: float = 1.0, decay: float = 0.95) -> None:
        """간단한 적분/감쇠 모델."""

        self.momentum = decay * self.momentum + self.force * dt
        self.energy += self.force * dt

    def as_dict(self) -> dict:
        return asdict(self)
