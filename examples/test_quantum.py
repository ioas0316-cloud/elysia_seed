
import math
import random
from elysia_engine.entities import Entity
from elysia_engine.tensor import SoulTensor
from elysia_engine.physics import PhysicsWorld, PhysicsState
from elysia_engine.math_utils import Vector3

def test_quantum_universe():
    print("--- Initializing Quantum Universe ---")
    world = PhysicsWorld()

    # Create a "Burning Star" (High Energy/Frequency)
    burning_star = Entity(
        id="burning_1",
        soul=SoulTensor(amplitude=10.0, frequency=100.0, phase=0.0),
        physics=PhysicsState(position=Vector3(0,0,0))
    )
    burning_star.f_soul = 10.0 # Will increase frequency

    # Create an "Ice Star" (Collapsed, High Mass)
    ice_star = Entity(
        id="ice_1",
        soul=SoulTensor(amplitude=500.0, frequency=0.0, phase=math.pi, is_collapsed=True),
        physics=PhysicsState(position=Vector3(2,0,0))
    )

    world.register_entity(burning_star)
    world.register_entity(ice_star)

    print(f"Initial State:")
    print(f"Burning Star: Freq={burning_star.soul.frequency}, Amp={burning_star.soul.amplitude}, Pos={burning_star.physics.position}")
    print(f"Ice Star: Collapsed={ice_star.soul.is_collapsed}, Amp={ice_star.soul.amplitude}")

    print("\n--- Simulating 100 Steps ---")
    for i in range(100):
        # Apply physics interactions
        # burning_star moves, ice_star is static (high mass usually means slow, but physics.step will move it if force is high enough)
        # We manually call step as the World loop does
        burning_star.apply_physics(None, world, dt=0.1)
        ice_star.apply_physics(None, world, dt=0.1)

        # Evolve souls
        burning_star.step(None, dt=0.1)
        ice_star.step(None, dt=0.1)

        # Check for "Melting" (Life Creation)
        # If burning star is close to ice star, it might melt it
        dist = (burning_star.physics.position - ice_star.physics.position).magnitude
        if dist < 3.0:
            # Transfer energy?
            # In our simplified model, we manually invoke melt if condition met
            # The physics engine manages movement, but 'interaction' logic like melt
            # might need a higher level system.
            # For this test, we simulate the "System" logic here.

            # Calculate energy transfer
            energy = burning_star.soul.frequency * 0.1
            ice_star.soul.melt(energy)

    print("\n--- Final State ---")
    print(f"Burning Star: Freq={burning_star.soul.frequency:.2f}, Pos={burning_star.physics.position}")
    print(f"Ice Star: Collapsed={ice_star.soul.is_collapsed}, Amp={ice_star.soul.amplitude:.2f}, Freq={ice_star.soul.frequency:.2f}")

    if not ice_star.soul.is_collapsed:
        print("SUCCESS: The Ice Star has melted into a Living Entity!")
    else:
        print("RESULT: The Ice Star remains dormant.")

    # Check Entanglement
    # Let's create two close stars
    ent_1 = Entity("e1", soul=SoulTensor(10, 50, 0), physics=PhysicsState(Vector3(10,0,0)))
    ent_2 = Entity("e2", soul=SoulTensor(10, 50, 0.1), physics=PhysicsState(Vector3(10.1,0,0)))
    world.register_entity(ent_1)
    world.register_entity(ent_2)

    # Run a step to trigger binding check
    world.check_dimensional_binding(ent_1)

    if ent_2.soul in ent_1.soul.entangled_peers:
        print("SUCCESS: Entanglement established.")

        # Test Spooky Action
        ent_1.soul.phase = 3.14
        ent_1.soul.step(0.1) # This should propagate

        print(f"Ent_1 Phase: {ent_1.soul.phase}")
        print(f"Ent_2 Phase: {ent_2.soul.phase} (Should be synced)")

        if abs(ent_1.soul.phase - ent_2.soul.phase) < 0.001:
             print("SUCCESS: Phase synchronization confirmed.")
    else:
        print("RESULT: No entanglement yet.")

if __name__ == "__main__":
    test_quantum_universe()
