from __future__ import annotations

import random
import sys
import time
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from elysia_engine import Entity, World
from elysia_engine.hooks.godot_stub import publish
from elysia_engine.hooks.logging import log_snapshot


class Beacon(Entity):
    def update_force_components(self, world: World) -> None:  # type: ignore[override]
        self.f_body = 0.05
        self.f_soul = 0.1
        self.f_spirit = random.uniform(-0.2, 0.2)


if __name__ == "__main__":
    world = World()
    world.add_entity(Beacon("beacon"))

    for _ in range(5):
        world.step(dt=1.0)
        snap = world.export_persona_snapshot()
        log_snapshot(snap)
        message = publish(snap)
        print("Godot payload:", message)
        time.sleep(0.05)
