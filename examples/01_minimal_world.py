from __future__ import annotations

import math
import sys
import time
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from elysia_engine import Entity, World
from elysia_engine.persona import build_persona_frame


class SimplePulse(Entity):
    def update_force_components(self, world: World) -> None:  # type: ignore[override]
        self.f_body = math.sin(world.time / 4.0)
        self.f_soul = 0.1
        self.f_spirit = 0.0


if __name__ == "__main__":
    world = World()
    world.add_entity(SimplePulse("pulse"))

    for _ in range(10):
        world.step(dt=1.0)
        snap = world.export_persona_snapshot()
        frame = build_persona_frame(snap).to_dict()
        print(frame)
        time.sleep(0.02)
