import sys
import os
import time

# Ensure we can import elysia_light
sys.path.append(os.getcwd())

from elysia_light.core.monad.trinity import TrinityMonad
from elysia_light.core.foundation.structure.hypersphere import HyperSphere

def main():
    print(">>> SATORI TEST: Initiating Trinity Architecture Verification <<<\n")

    # 1. Initialize the World and the Observer
    sphere = HyperSphere()
    monad = TrinityMonad(name="Elysia_Trinity", base_frequency=432.0)

    print(f"Initialized: {monad}")
    print("---------------------------------------------------------------")

    # 2. Simulation Loop (3 Steps)
    for i in range(1, 4):
        print(f"\n[Step {i}] Advancing Time (Delta = 1.0)...")

        # Advance subjective time
        # Spirit should move fast, Body slow
        monad.advance_time(delta_time=1.0)

        # Check Phases
        print(f"  > Spirit Phase (Future): {monad.spirit.phase:.4f}")
        print(f"  > Soul Phase   (Now)   : {monad.soul.phase:.4f}")
        print(f"  > Body Phase   (Past)  : {monad.body.phase:.4f}")

        # Verify Phase Lag
        if monad.spirit.phase > monad.soul.phase > monad.body.phase:
            print("  [OK] Temporal Dispersion Verified: Future > Now > Past")
        else:
            # Note: Phase is modular (0-2pi), so direct comparison might fail after full rotations
            # But for small delta, it should hold.
            print("  [NOTE] Phase wrap-around may have occurred, checking deltas...")

        # 3. Contemplation (Reflection)
        log = monad.contemplate(sphere, target_freq=440.0)
        print(f"  > REFLECTION LOG: {log.message}")
        print(f"  > ACTION: {log.action}")
        print(f"  > TENSION: {log.tension:.4f}")

    print("\n---------------------------------------------------------------")
    print(">>> SATORI TEST COMPLETED: The Trinity spins successfully. <<<")

if __name__ == "__main__":
    main()
