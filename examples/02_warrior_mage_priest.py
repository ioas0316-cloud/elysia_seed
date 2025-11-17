from __future__ import annotations

import math
import sys
import time
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from elysia_engine import Entity, World
from elysia_engine.persona import build_persona_frame


class Warrior(Entity):
    def __init__(self, id: str):
        super().__init__(id=id, role="warrior")

    def update_force_components(self, world: World) -> None:  # type: ignore[override]
        self.f_body = math.sin(world.time / 3.0)
        self.f_soul = 0.1
        self.f_spirit = 0.05


class Mage(Entity):
    def __init__(self, id: str):
        super().__init__(id=id, role="mage")

    def update_force_components(self, world: World) -> None:  # type: ignore[override]
        self.f_soul = math.sin(world.time / 5.0)
        self.f_body = 0.1
        self.f_spirit = 0.2


class Priest(Entity):
    def __init__(self, id: str):
        super().__init__(id=id, role="priest")

    def update_force_components(self, world: World) -> None:  # type: ignore[override]
        self.f_spirit = math.sin(world.time / 9.0)
        self.f_body = 0.05
        self.f_soul = 0.15


if __name__ == "__main__":
    world = World()
    world.add_entity(Warrior("warrior_1"))
    world.add_entity(Mage("mage_1"))
    world.add_entity(Priest("priest_1"))

    for _ in range(20):
        world.step(dt=1.0)
        snap = world.export_persona_snapshot()
        frame = build_persona_frame(snap).to_dict()
        print(f"[tick {snap['tick']:03d}] {frame}")
        time.sleep(0.05)
