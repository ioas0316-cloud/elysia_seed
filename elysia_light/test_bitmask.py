
import math
import sys
import os

# Add the parent directory to sys.path to allow imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from elysia_light.core.foundation.nature.rotor import Rotor
from elysia_light.core.foundation.structure.hypersphere import HyperSphere, OperationMode, FREQ_BAND_WIDTH

def test_fractal_bitmask():
    sphere = HyperSphere()

    print("=== Testing Fractal Bitmask Engine ===")

    # 1. Setup Memories
    # Central Melody (Freq 520)
    sphere.absorb(Rotor("Melody_1", frequency=520, mass=1.0)) # Phase 0 implicitly

    r2 = Rotor("Melody_2", frequency=520, mass=1.0); r2.phase = 1.0
    sphere.absorb(r2)

    # Harmony (Freq 530 - Neighbor)
    h1 = Rotor("Harmony_1", frequency=530, mass=1.0); h1.phase = 0.0 # Same time as Melody_1
    sphere.absorb(h1)

    # Background/Ambient (Freq 400 - Distant)
    b1 = Rotor("Ambient_Bird", frequency=400, mass=1.0); b1.phase = 2.0
    sphere.absorb(b1)

    print(f"\nPopulation: {sphere.population}")

    # 2. Test POINT Mode (1111) - Exact
    print("\n--- Testing POINT Mode (1111) ---")
    probe = Rotor("Probe", frequency=520)
    res = sphere.operate(probe, mode=OperationMode.POINT) # Should get Melody_1 (Phase 0)
    if res and "Melody_1" in res.name:
        print("SUCCESS: POINT retrieved exact match.")
    else:
        print(f"FAILURE: POINT got {res}")

    # 3. Test LINE Mode (0001) - Stream Time, Fix Freq (520)
    print("\n--- Testing LINE Mode (0001) ---")
    res = sphere.operate(probe, mode=OperationMode.LINE)
    # Should get Melody_1 and Melody_2 only. NOT Harmony (530) or Ambient (400).
    names = [r.name for r in res]
    print(f"LINE Result: {names}")

    if len(names) == 2 and "Ghost_Melody_1" in names and "Ghost_Melody_2" in names:
        print("SUCCESS: LINE retrieved only central frequency stream.")
    else:
        print("FAILURE: LINE retrieval incorrect.")

    # 4. Test PLANE Mode (0011) - Stream Time + Neighbors (+/- 1 Band)
    # Probe is 520. Neighbor is 530. 400 is far away.
    print("\n--- Testing PLANE Mode (0011) ---")
    res = sphere.operate(probe, mode=OperationMode.PLANE)
    names = [r.name for r in res]
    print(f"PLANE Result: {names}")

    # Expect Melody_1, Melody_2, AND Harmony_1. NOT Ambient.
    has_melody = any("Melody" in n for n in names)
    has_harmony = any("Harmony" in n for n in names)
    has_ambient = any("Ambient" in n for n in names)

    if has_melody and has_harmony and not has_ambient:
        print("SUCCESS: PLANE retrieved Melody + Harmony (Context).")
    else:
        print("FAILURE: PLANE retrieval incorrect.")

    # 5. Test SPACE Mode (0111) - Wide Area (+/- 5 Bands)
    # Probe is 520. 400 is -120hz away.
    # Wait, 5 bands * 10 = 50hz radius.
    # 520 +/- 50 = [470, 570].
    # So Ambient (400) should still be EXCLUDED in SPACE mode with radius 5.
    # Let's add a "Scene" element within range.

    s1 = Rotor("Scene_Tree", frequency=560, mass=1.0) # +40hz difference (Inside radius 5)
    sphere.absorb(s1)

    print("\n--- Testing SPACE Mode (0111) ---")
    res = sphere.operate(probe, mode=OperationMode.SPACE)
    names = [r.name for r in res]
    print(f"SPACE Result: {names}")

    has_tree = any("Scene_Tree" in n for n in names)
    has_ambient = any("Ambient" in n for n in names)

    if has_tree and not has_ambient:
        print("SUCCESS: SPACE retrieved Scene elements within radius, excluded far ambient.")
    else:
        print("FAILURE: SPACE retrieval incorrect.")

if __name__ == "__main__":
    test_fractal_bitmask()
