from __future__ import annotations
from typing import List

from ..systems import System
from ..world import World

class VoidSystem(System):
    """
    The Void: Entropy and Garbage Collection.
    Consumes entities that are too weak or too far.
    """
    def __init__(self, boundary_radius: float = 100.0, min_amplitude: float = 0.1):
        self.boundary_radius = boundary_radius
        self.min_amplitude = min_amplitude

    def step(self, world: World, dt: float) -> None:
        to_delete: List[str] = []

        for eid, ent in world.entities.items():
            # 1. Check Spatial Boundary
            if ent.physics.position.magnitude > self.boundary_radius:
                to_delete.append(eid)
                continue

            # 2. Check Energy (Existence)
            if ent.soul and ent.soul.amplitude < self.min_amplitude:
                to_delete.append(eid)

        for eid in to_delete:
            del world.entities[eid]
            # In a real engine, we might log this or recycle the energy.
