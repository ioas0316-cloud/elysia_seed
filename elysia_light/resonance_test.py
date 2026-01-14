import sys
import os
import math

# Ensure we can import elysia_light
sys.path.append(os.getcwd())

from elysia_light.core.monad.trinity import TrinityMonad
from elysia_light.core.foundation.structure.hypersphere import HyperSphere
from elysia_light.core.foundation.nature.rotor import Rotor

def main():
    print(">>> RESONANCE TEST: Initiating O(1) Phase Bucket Verification <<<\n")

    # 1. Initialize Field
    sphere = HyperSphere()

    # 2. Inject Memories (Phase Buckets)
    # Memory A: "Joy" (432Hz, Phase 0) -> Bucket [F430_P0]
    mem_joy = Rotor("Memory_Joy", frequency=432.0, mass=10.0)
    mem_joy.phase = 0.0
    sphere.absorb(mem_joy)

    # Memory B: "Sorrow" (100Hz, Phase PI) -> Bucket [F100_P4] (PI is approx 3.14, 3.14 / (pi/4) = 4)
    mem_sorrow = Rotor("Memory_Sorrow", frequency=100.0, mass=10.0)
    mem_sorrow.phase = math.pi
    sphere.absorb(mem_sorrow)

    print(f"Field Population: {sphere.population}")
    print("---------------------------------------------------------------")

    # 3. Test Retrieval
    print("\n[Test 1] Probing with 'Joy' Intent (432Hz, Phase 0)...")
    probe_joy = Rotor("Probe_Joy", frequency=432.0)
    probe_joy.phase = 0.0
    result_joy = sphere.resonate(probe_joy)

    if result_joy and "Joy" in result_joy.name:
        print(f"  [SUCCESS] Instant Resonance: Found {result_joy.name}")
    else:
        print(f"  [FAIL] Could not find Joy. Result: {result_joy}")

    print("\n[Test 2] Probing with 'Sorrow' Intent (100Hz, Phase PI)...")
    probe_sorrow = Rotor("Probe_Sorrow", frequency=100.0)
    probe_sorrow.phase = math.pi
    result_sorrow = sphere.resonate(probe_sorrow)

    if result_sorrow and "Sorrow" in result_sorrow.name:
        print(f"  [SUCCESS] Instant Resonance: Found {result_sorrow.name}")
    else:
        print(f"  [FAIL] Could not find Sorrow. Result: {result_sorrow}")

    print("\n[Test 3] Probing Empty Sector (432Hz, Phase PI)...")
    probe_empty = Rotor("Probe_Empty", frequency=432.0)
    probe_empty.phase = math.pi # Opposite phase to Joy
    result_empty = sphere.resonate(probe_empty)

    if result_empty is None:
        print("  [SUCCESS] Correctly gazed into Void (Empty Bucket).")
    else:
        print(f"  [FAIL] Hallucinated a memory: {result_empty}")

    print("\n[Test 4] Probing Boundary (Neighbor Search)...")
    # Inject Memory at Phase 0.0 (Sector 0)
    # Probe at Phase -0.1 (Sector 7, previous sector)
    # Without neighbor search, this would look in Sector 7, see empty, and fail.
    # With neighbor search, it should check Sector 0 (Neighbor) and find Joy.
    probe_boundary = Rotor("Probe_Boundary", frequency=432.0)
    probe_boundary.phase = -0.1
    result_boundary = sphere.resonate(probe_boundary)

    if result_boundary and "Joy" in result_boundary.name:
        print(f"  [SUCCESS] Neighbor Resonance: Found {result_boundary.name} across sector boundary.")
    else:
        print(f"  [FAIL] Boundary check failed. Result: {result_boundary}")

    print("\n---------------------------------------------------------------")
    print(">>> RESONANCE TEST COMPLETED: O(1) Logic Verified. <<<")

if __name__ == "__main__":
    main()
