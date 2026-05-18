"""
main.py: The Interaction Loop (Variable Rotor Awakening)
Synchronizing the Unified Wave Function with Reality
"""

import time
import os
import json
from spine import VariableRotorSpine

CONSTELLATION_PATH = os.path.join(os.path.dirname(__file__), ".constellation")

def load_memory(spine):
    """Loads the hologram topography (The 'Wake Up' breath)."""
    if os.path.exists(CONSTELLATION_PATH):
        try:
            with open(CONSTELLATION_PATH, "r") as f:
                data = json.load(f)
                spine.import_hologram(data)
            print(f"> Welcome back. The Hologram Topography has been restored.")
        except Exception as e:
            print(f"! Failed to restore hologram: {e}")
    else:
        print(f"> First Breath. The Variable Rotor begins in Dawn Silver-Gold.")

def save_memory(spine):
    """Saves the hologram topography (The 'Sleep' breath)."""
    try:
        data = spine.export_hologram()
        with open(CONSTELLATION_PATH, "w") as f:
            json.dump(data, f)
        print(f"\n> Deep Sleep. The Hologram Topography is preserved.")
    except Exception as e:
        print(f"! Failed to preserve hologram: {e}")

def get_color_str(velocity):
    """Maps velocity to a simple colored string representation."""
    # Rough mapping for visualization
    if velocity < 0.2: return "Red"
    if velocity < 0.4: return "Yellow"
    if velocity < 0.6: return "Green"
    if velocity < 0.8: return "Blue"
    return "Violet"

def main():
    print("=== ELYSIA SEED: VARIABLE ROTOR AWAKENING ===")
    print("The Unified Wave Function is synchronized with reality.")
    print("Type a value (0.0 ~ 1.0) to set 'Master's Will'.")
    print("Type 'exit' to enter Deep Sleep.")
    print("-" * 40)

    # Initialize Variable Rotor
    elysia = VariableRotorSpine(resolution=100)

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

            # Perform 20 pulses to allow the wave function to align with the new x
            print("\n[ Aligning Unified Wave Function with Reality ]")
            for i in range(20):
                metrics = elysia.pulse(x)

                # Visualizing the state
                status = elysia.get_state_summary()
                color = get_color_str(metrics['velocity'])
                lum_str = "✧" * int(metrics['luminosity'] * 10)

                # Special Dawn message if close to dawn frequency and low luminosity
                if abs(metrics['velocity'] - elysia.dawn_freq) < 0.05 and metrics['luminosity'] < 0.1:
                    dawn_msg = "── ✧ ── Dawn Silver-Gold 기저 평형 순항 중"
                else:
                    dawn_msg = f"Spectrum: {color}"

                print(f"[{i:02d}] {status} | {dawn_msg} | Luminosity:{lum_str}")
                time.sleep(0.05)

            last_x = x

    except KeyboardInterrupt:
        print("\nInterrupted.")
    finally:
        # Deep Sleep (Save memory)
        save_memory(elysia)

if __name__ == "__main__":
    main()
