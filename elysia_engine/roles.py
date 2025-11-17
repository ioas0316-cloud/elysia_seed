from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RoleProfile:
    name: str
    w_body: float
    w_soul: float
    w_spirit: float

    @property
    def normalized(self) -> "RoleProfile":
        total = self.w_body + self.w_soul + self.w_spirit
        if total == 0:
            return self
        return RoleProfile(
            name=self.name,
            w_body=self.w_body / total,
            w_soul=self.w_soul / total,
            w_spirit=self.w_spirit / total,
        )


ROLE_PROFILES = {
    "warrior": RoleProfile("warrior", w_body=0.7, w_soul=0.2, w_spirit=0.1),
    "mage": RoleProfile("mage", w_body=0.2, w_soul=0.6, w_spirit=0.2),
    "priest": RoleProfile("priest", w_body=0.2, w_soul=0.2, w_spirit=0.6),
}
