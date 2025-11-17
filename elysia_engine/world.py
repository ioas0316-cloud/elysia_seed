from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from .entities import Entity


@dataclass
class World:
    """프랙탈 의식 엔진의 최소 세계."""

    time: float = 0.0
    tick: int = 0
    entities: Dict[str, Entity] = field(default_factory=dict)

    def add_entity(self, entity: Entity) -> None:
        self.entities[entity.id] = entity

    def step(self, dt: float = 1.0) -> None:
        self.time += dt
        self.tick += 1
        for ent in self.entities.values():
            ent.step(self, dt=dt)

    def export_persona_snapshot(self) -> Dict:
        return {
            "tick": self.tick,
            "time": self.time,
            "entity_count": len(self.entities),
            "entities": [ent.to_payload() for ent in self.entities.values()],
        }
