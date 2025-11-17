from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any, Dict


@dataclass
class PersonaFrame:
    tick: int
    time: float
    entity_count: int
    energy_avg: float
    momentum_avg: float
    caption: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def build_persona_frame(world_snapshot: Dict[str, Any]) -> PersonaFrame:
    entities = world_snapshot.get("entities", [])
    energy_values = [ent["efp"]["energy"] for ent in entities if "efp" in ent]
    momentum_values = [ent["efp"]["momentum"] for ent in entities if "efp" in ent]

    avg_energy = sum(energy_values) / len(energy_values) if energy_values else 0.0
    avg_momentum = (
        sum(momentum_values) / len(momentum_values) if momentum_values else 0.0
    )

    caption = (
        f"tick={world_snapshot.get('tick', 0)}, "
        f"E={avg_energy:.2f}, P={avg_momentum:.2f}, N={world_snapshot.get('entity_count', 0)}"
    )

    return PersonaFrame(
        tick=int(world_snapshot.get("tick", 0)),
        time=float(world_snapshot.get("time", 0.0)),
        entity_count=int(world_snapshot.get("entity_count", len(entities))),
        energy_avg=avg_energy,
        momentum_avg=avg_momentum,
        caption=caption,
    )
