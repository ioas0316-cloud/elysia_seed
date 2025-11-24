from __future__ import annotations
import copy
from typing import List, Optional, Dict, Any
from dataclasses import dataclass

from .world import World
from .systems import System
from .tensor import SoulTensor

class DreamSystem(System):
    """
    Chronos: The Timekeeper & Prophet.
    Manages time dilation and future simulation (Prophecy).
    """

    def __init__(self):
        self.time_dilation_factor: float = 1.0

    def step(self, world: World, dt: float) -> None:
        """
        Chronos watches the flow of time.
        """
        pass

    def fork_timeline(self, world: World) -> World:
        """
        Creates a perfect copy of the current world state.
        This is a 'Branching Universe'.
        """
        # We use deepcopy to ensure full isolation
        # Note: We must be careful with systems that hold external resources.
        # Ideally, systems should be stateless per step or pure data.
        new_world = copy.deepcopy(world)

        # Clean up systems in the dream world to prevent side effects (like printing or file writing)
        # We only want physics and internal logic.
        # Filter out systems that might be 'heavy' or 'IO bound' if we can identify them.
        # For now, we keep them but user must be aware.
        return new_world

    def prophecy(self, world: World, steps: int = 10, dt: float = 0.5) -> Dict[str, Any]:
        """
        Runs a simulation into the future and returns the final state.
        Does NOT affect the current world.
        Returns a summary dict of the future state.
        """
        dream_world = self.fork_timeline(world)

        # Fast-forward
        for _ in range(steps):
            dream_world.step(dt=dt)

        # Harvest results
        # We return a map of Entity ID -> Final Soul State
        results = {}
        for eid, ent in dream_world.entities.items():
            if ent.soul:
                # Capture the soul state
                results[eid] = ent.soul.as_dict()

        return {
            "final_tick": dream_world.tick,
            "entities": results
        }
