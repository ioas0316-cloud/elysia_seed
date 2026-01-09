import sys
import os
import math
sys.path.append(os.getcwd())

from elysia_engine.physics import PhysicsWorld, Attractor
from elysia_engine.entities import Entity, PhysicsState
from elysia_engine.tensor import SoulTensor
from elysia_engine.math_utils import Vector3, Quaternion

def run_perception_test():
    print("\n" + "="*50)
    print("👁️ [Elysia] Testing Human Sensory Perception")
    print("="*50 + "\n")

    world = PhysicsWorld()

    # 1. Setup Entity (Observer)
    observer = Entity(
        id="human_observer",
        physics=PhysicsState(position=Vector3(0,0,0)),
        soul=SoulTensor(
            amplitude=10.0,
            frequency=100.0,
            phase=0.0,
            orientation=Quaternion.identity() # Facing +Z
        )
    )
    world.register_entity(observer)

    # 2. Setup Field Targets using Attractors to paint the field

    # "The Garden" (Resonant, Clear, Light, Balanced)
    # Freq=100 (Resonant), Mass=Normal, Spin=0
    garden = Attractor(
        id="garden",
        position=Vector3(0,0,5),
        mass=10.0, # Light Touch
        soul=SoulTensor(amplitude=10.0, frequency=100.0, phase=0.0)
    )

    # "The Storm" (Dissonant, Heavy, Spinning)
    # Freq=0 (Dissonant), Mass=Huge (Heavy Touch), Spin=High
    storm = Attractor(
        id="storm",
        position=Vector3(0,0,-5),
        mass=1000.0, # Heavy Touch
        soul=SoulTensor(amplitude=1000.0, frequency=0.0, phase=0.0, spin=10.0)
    )

    world.add_attractor(garden)
    world.add_attractor(storm)

    # Update field to propagate values
    world.update_field()

    print("🧪 Scenario 1: Gazing at The Garden")
    # Facing +Z
    senses_1 = world.perceive(observer, range_dist=5.0)

    print(f"   [Vision] Clarity: {senses_1.visual_clarity:.2f}")
    print(f"   [Hearing] Resonance: {senses_1.auditory_resonance:.2f}")
    print(f"   [Touch] Pressure: {senses_1.haptic_pressure:.2f}")
    print(f"   [Balance] Vertigo: {senses_1.vestibular_balance:.2f}")
    print(f"   [Narrative] \"{senses_1.narrative}\"")

    if senses_1.auditory_resonance > 0.9:
        print("   ✅ SUCCESS: High Harmony detected.")
    else:
        print("   ❌ FAILURE: Harmony too low.")

    print("\n🧪 Scenario 2: Gazing at The Storm")
    # Rotate Observer to face -Z
    rot_back = Quaternion.from_axis_angle(Vector3(0,1,0), math.pi)
    observer.soul.orientation = rot_back

    senses_2 = world.perceive(observer, range_dist=5.0)

    print(f"   [Vision] Clarity: {senses_2.visual_clarity:.2f}")
    print(f"   [Hearing] Resonance: {senses_2.auditory_resonance:.2f}")
    print(f"   [Touch] Pressure: {senses_2.haptic_pressure:.2f}")
    print(f"   [Balance] Vertigo: {senses_2.vestibular_balance:.2f}")
    print(f"   [Narrative] \"{senses_2.narrative}\"")

    if senses_2.haptic_pressure > 5.0 and senses_2.vestibular_balance > 0.1:
        print("   ✅ SUCCESS: Heavy Pressure and Vertigo detected.")
    else:
        print("   ❌ FAILURE: Storm not feeling heavy/spinning enough.")

    print("\n" + "="*50)

if __name__ == "__main__":
    run_perception_test()
