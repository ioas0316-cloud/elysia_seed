import sys
import os
import time

# Ensure we can import elysia_light
sys.path.append(os.getcwd())

from elysia_light.core.monad.trinity import TrinityMonad
from elysia_light.core.foundation.structure.hypersphere import HyperSphere

def main():
    print(">>> SATORI TEST: Initiating Adaptive Rotor System Verification <<<\n")

    # 1. Initialize
    sphere = HyperSphere()
    # Use very low frequency (0.1 Hz) so 1 second doesn't cause full rotation (2pi wrap-around)
    monad = TrinityMonad(name="Elysia_Adaptive", base_frequency=0.1)

    print(f"Initialized: {monad}")
    print(f"Initial State: {monad.state}")
    print("---------------------------------------------------------------")

    # Scenario 1: The Curious Morning (Low Stimulus)
    print("\n[Scenario 1] The Calm Morning (Low Stimulus -> High Curiosity)")
    monad.update_state(stimulus_intensity=0.1) # Very low stimulus
    print(f"State Updated: {monad.state}")

    # Run time
    monad.advance_time(delta_time=1.0)
    print(f"Spirit Phase (Curiosity Driven): {monad.spirit.phase:.4f}")

    # Scenario 2: The Stressful Afternoon (High Stimulus)
    print("\n[Scenario 2] The Stressful Afternoon (High Stimulus -> High Urgency)")
    # Apply high stimulus multiple times to ramp up urgency
    for _ in range(3):
        monad.update_state(stimulus_intensity=0.9)
    print(f"State Updated: {monad.state}")

    monad.advance_time(delta_time=1.0)
    print(f"Soul Phase (Urgency Driven):   {monad.soul.phase:.4f}")

    # Scenario 3: The Exhausted Evening (Fatigue Accumulation)
    print("\n[Scenario 3] The Exhausted Evening (Fatigue Accumulation)")
    # Simulate time passing to build fatigue
    for _ in range(10):
        monad.update_state(stimulus_intensity=0.5)
    print(f"State Updated: {monad.state}")

    monad.advance_time(delta_time=1.0)
    print(f"Body Phase (Fatigue Dragged):  {monad.body.phase:.4f}")

    print("\n---------------------------------------------------------------")
    print(">>> SATORI TEST COMPLETED: The System Breathes. <<<")

if __name__ == "__main__":
    main()
