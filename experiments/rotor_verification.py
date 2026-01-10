import sys
import os

# Ensure the path allows importing elysia_engine
sys.path.append(os.getcwd())

from elysia_engine.physics import PhysicsWorld
from elysia_engine.entities import Entity
from elysia_engine.tensor import SoulTensor
from elysia_engine.math_utils import Vector3, Quaternion, Rotor

def debug_rotor_attributes():
    print("--- Debugging Rotor Class ---")
    r = Rotor.identity()
    print(f"Rotor attributes: {dir(r)}")
    try:
        print(f"r.scalar: {r.scalar}")
    except AttributeError:
        print("r.scalar does NOT exist.")

    try:
        print(f"r.a: {r.a}")
    except AttributeError:
        print("r.a does NOT exist.")

def test_rotor_physics_step():
    print("\n--- Initializing Physics World ---")
    world = PhysicsWorld()

    print("Creating Test Entity with Soul...")
    soul = SoulTensor(
        amplitude=10.0,
        frequency=50.0,
        phase=0.0,
        spin=1.0,
        polarity=1.0,
        orientation=Quaternion.identity()
    )

    entity = Entity(id="test_subject_01", data={"name": "RotorTester"})
    entity.soul = soul
    entity.physics.position = Vector3(1.0, 0.0, 0.0)

    world.register_entity(entity)

    print("Running Simulation Step (Tick 1)...")
    try:
        # Force a situation where get_geodesic_flow is called
        # The logic is inside step -> active_survivors -> get_geodesic_flow
        world.step(dt=0.1)
        print("Success: Step 1 complete.")
    except AttributeError as e:
        print(f"CRITICAL FAILURE: {e}")
        return False
    except Exception as e:
        print(f"FAILURE: Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        return False

    return True

if __name__ == "__main__":
    debug_rotor_attributes()
    if test_rotor_physics_step():
        print("Rotor Verification: PASSED")
    else:
        print("Rotor Verification: FAILED")
