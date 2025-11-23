import unittest
import sys
import os
import math

sys.path.append(os.getcwd())

from elysia_engine.physics import PhysicsWorld, Attractor
from elysia_engine.tensor import SoulTensor
from elysia_engine.storyteller import StoryTeller
from elysia_engine.math_utils import Vector3

class TestTensorLogic(unittest.TestCase):
    def setUp(self):
        self.p_world = PhysicsWorld()

        # War: Red (150Hz), Phase 0, Pos -10
        self.war = Attractor(id="War", position=Vector3(-10, 0, 0), mass=500.0,
                        soul=SoulTensor(amplitude=500, frequency=150, phase=0))
        self.p_world.add_attractor(self.war)

        # Peace: Green (40Hz), Phase 0, Pos +10
        self.peace = Attractor(id="Peace", position=Vector3(10, 0, 0), mass=500.0,
                          soul=SoulTensor(amplitude=500, frequency=40, phase=0))
        self.p_world.add_attractor(self.peace)

    def test_war_resonance(self):
        # "fight" -> ~150Hz, Phase 0
        entity = StoryTeller.create_intent_entity("fight kill")
        self.p_world.register_entity(entity)

        # Step physics
        # Entity starts at 0,0,0
        # Both attractors are 10 units away.
        # War pulls harder due to resonance.

        for _ in range(20):
            entity.apply_physics(coil=None, world_physics=self.p_world, dt=0.5)

        dist_war = (entity.physics.position - self.war.position).magnitude
        dist_peace = (entity.physics.position - self.peace.position).magnitude

        # print(f"War Dist: {dist_war}, Peace Dist: {dist_peace}, Pos: {entity.physics.position}")
        self.assertLess(dist_war, dist_peace, "Entity should gravitate towards War")
        self.assertLess(entity.physics.position.x, 0, "Entity should move Left (-x)")

    def test_peace_resonance(self):
        # "love" -> ~40Hz, Phase 0
        entity = StoryTeller.create_intent_entity("love peace")
        self.p_world.register_entity(entity)

        for _ in range(20):
            entity.apply_physics(coil=None, world_physics=self.p_world, dt=0.5)

        dist_war = (entity.physics.position - self.war.position).magnitude
        dist_peace = (entity.physics.position - self.peace.position).magnitude

        self.assertLess(dist_peace, dist_war, "Entity should gravitate towards Peace")
        self.assertGreater(entity.physics.position.x, 0, "Entity should move Right (+x)")

if __name__ == '__main__':
    unittest.main()
