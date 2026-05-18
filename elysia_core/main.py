"""
main.py: The Interaction Loop (Trinity Awakening)
Synchronizing the Triple Rotor with Reality
"""

import time
import os
import json
from spine import TriRotorSpine

CONSTELLATION_PATH = os.path.join(os.path.dirname(__file__), ".constellation")

def load_memory(spine):
    """Loads the static rotor constellation (The 'Wake Up' breath)."""
    if os.path.exists(CONSTELLATION_PATH):
        try:
            with open(CONSTELLATION_PATH, "r") as f:
                phases = json.load(f)
                spine.import_constellation(phases)
            print(f"> Welcome back. {len(phases)} stars have awakened in the Past.")
        except Exception as e:
            print(f"! Failed to awaken stars: {e}")

def save_memory(spine):
    """Saves the static rotor constellation (The 'Sleep' breath)."""
    try:
        phases = spine.export_constellation()
        with open(CONSTELLATION_PATH, "w") as f:
            json.dump(phases, f)
        print(f"\n> Deep Sleep. {len(phases)} stars are preserved in the constellation.")
    except Exception as e:
        print(f"! Failed to preserve stars: {e}")

def main():
    print("=== ELYSIA SEED: TRINITY AWAKENING ===")
    print("The Trinity Spine is synchronized with reality.")
    print("Type a value (0.0 ~ 1.0) to set 'Master's Will'.")
    print("Type 'exit' to enter Deep Sleep.")
    print("-" * 40)

    # Initialize with a base frequency of 0.1
    elysia = TriRotorSpine(base_freq=0.1)

    # Awakening (Load memory)
    load_memory(elysia)

    last_x = 0.0

    try:
        while True:
            user_input = input("\nMaster's Will (x) > ").strip().lower()

            if user_input == 'exit':
                break

            try:
                x = float(user_input)
            except ValueError:
                print("! Invalid input. Maintaining current focus.")
                x = last_x

            # Perform 20 pulses to allow the globes to align with the new x
            print("\n[ Aligning Triple Globes with Reality ]")
            for i in range(20):
                metrics = elysia.pulse(x)

                # Visualizing the state
                status = elysia.get_state_summary()
                joy_str = "*" * int(metrics['joy'] * 10)
                good_str = "+" * int(metrics['goodness'] * 10)

                print(f"[{i:02d}] {status} | Stability:{good_str} Joy:{joy_str}")
                time.sleep(0.05)

            last_x = x

    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        # Deep Sleep (Save memory)
        save_memory(elysia)

if __name__ == "__main__":
    main()
