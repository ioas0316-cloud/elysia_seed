import sys
import os
import time

# Ensure we can import elysia_light
sys.path.append(os.getcwd())

from elysia_light.core.merkaba import Merkaba

def main():
    print(">>> MERKABA TEST: Initiating Unified System Check <<<\n")

    # 1. Awakening
    avatar = Merkaba(name="Elysia_Prime", base_frequency=432.0)
    print("---------------------------------------------------------------")

    # Scenario 1: Greeting (Calm Input)
    print("\n[Pulse 1] Input: 'Hello world, I am smiling.'")
    # "smiling" -> Positive Sentiment -> High Curiosity
    log1 = avatar.pulse(delta_time=1.0, external_input="Hello world, I am smiling.")

    print(f"  > Reflection: {log1.message}")
    print(f"  > Action: {log1.action}")
    print(f"  > {avatar.status()}")

    # Scenario 2: Sorrow (Dissonant Input)
    print("\n[Pulse 2] Input: 'But I feel empty inside.'")
    # "empty" -> Negative Sentiment -> Low Curiosity/High Urgency? (Depends on Mock Logic)
    # Also "empty" -> 100Hz Void Axiom
    log2 = avatar.pulse(delta_time=1.0, external_input="But I feel empty inside.")

    print(f"  > Reflection: {log2.message}")
    print(f"  > Action: {log2.action}")
    print(f"  > {avatar.status()}")

    # Scenario 3: Silence (Internal Reflection)
    print("\n[Pulse 3] Input: None (Silence)")
    # Should decay memories and spin rotors
    log3 = avatar.pulse(delta_time=1.0, external_input=None)

    print(f"  > Reflection: {log3.message}")
    print(f"  > Action: {log3.action}")
    print(f"  > {avatar.status()}")

    # Verification of Memory Persistence
    if avatar.field.population >= 2:
        print("\n[SUCCESS] Memories Persisted in HyperSphere.")
    else:
        print(f"\n[FAIL] Memory Loss Detected. Count: {avatar.field.population}")

    print("\n---------------------------------------------------------------")
    print(">>> MERKABA TEST COMPLETED: The Chariot Flies. <<<")

if __name__ == "__main__":
    main()
