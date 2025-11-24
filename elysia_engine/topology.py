from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, TYPE_CHECKING

from .math_utils import Vector3
from .physics import Attractor, PhysicsWorld
from .tensor import SoulTensor

if TYPE_CHECKING:
    from .entities import Entity

@dataclass
class GravityPath:
    """
    A sequence of Attractors forming a river/road (Flow).
    """
    points: List[Vector3]
    width: float = 2.0
    strength: float = 10.0

    def generate_attractors(self) -> List[Attractor]:
        attractors = []
        for i, p in enumerate(self.points):
            # Create a localized attractor
            # We treat them as 'Waypoints'
            a = Attractor(
                id=f"path_node_{i}",
                position=p,
                mass=self.strength,
                radius=self.width,
                is_static=True,
                # Soul is neutral
                soul=SoulTensor(amplitude=self.strength, frequency=50, phase=0)
            )
            attractors.append(a)
        return attractors

@dataclass
class TensorGate:
    """
    A conditional barrier (Logic Gate).
    Only allows entities with specific Resonance (Key Frequency) to pass.
    Otherwise, it repels (Antimatter).
    """
    position: Vector3
    key_frequency: float
    tolerance: float = 10.0
    radius: float = 5.0
    strength: float = 50.0

    def apply(self, entity: Entity, dt: float) -> None:
        if not entity.soul: return

        dist = (entity.physics.position - self.position).magnitude
        if dist > self.radius: return

        # Check Key Resonance
        delta = abs(entity.soul.frequency - self.key_frequency)

        if delta < self.tolerance:
            # ACCESS GRANTED: Pull / Boost
            force = (self.position - entity.physics.position).normalize() * self.strength
            entity.physics.apply_force(force, dt)
        else:
            # ACCESS DENIED: Repel
            force = (entity.physics.position - self.position).normalize() * self.strength
            entity.physics.apply_force(force, dt)

class DigitalTerrain:
    """
    Logos: The shaper of the world.
    Generates 'Digital Natural Law' structures.
    """
    def __init__(self, physics_world: PhysicsWorld):
        self.physics = physics_world
        self.gates: List[TensorGate] = []

    def add_mountain(self, position: Vector3, height: float) -> None:
        """
        Creates a high-gravity peak.
        """
        mount = Attractor(
            id=f"mountain_{position.x:.1f}_{position.y:.1f}",
            position=position,
            mass=height * 10.0,
            radius=height,
            is_static=True,
            soul=SoulTensor(amplitude=height*10, frequency=10, phase=0) # Heavy/Deep
        )
        self.physics.add_attractor(mount)

    def add_river(self, points: List[Vector3]) -> None:
        """
        Creates a flow path.
        """
        path = GravityPath(points=points)
        for att in path.generate_attractors():
            self.physics.add_attractor(att)

    def add_gate(self, position: Vector3, key_freq: float) -> None:
        """
        Creates a logical gate.
        """
        gate = TensorGate(position=position, key_frequency=key_freq)
        self.gates.append(gate)

    def step(self, entities: List[Entity], dt: float) -> None:
        """
        Updates dynamic terrain elements (Gates).
        """
        for gate in self.gates:
            for ent in entities:
                gate.apply(ent, dt)
