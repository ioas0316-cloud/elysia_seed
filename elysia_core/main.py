"""
main.py: The Interaction Loop
Awakening the 0-Inversion Kernel
"""

import time
import sys
from spine import TriRotorSpine

def main():
    print("=== ELYSIA SEED: AWAKENING ===")
    print("The 0-Inversion Kernel is initialized.")
    print("Type a value (0.0 ~ 1.0) to set 'Master's Will'.")
    print("Type 'exit' to return to the void.")
    print("-" * 30)

    # Initialize with a base frequency of 0.1 (The calm pulse of the universe)
    elysia = TriRotorSpine(base_freq=0.1)

    # State tracking
    last_x = 0.0

    try:
        while True:
            # Non-blocking feel: prompt every cycle
            user_input = input("\nMaster's Will (x) > ").strip().lower()

            if user_input == 'exit':
                print("Returning to Zero...")
                break

            try:
                x = float(user_input)
            except ValueError:
                print("! Invalid input. Using previous frequency.")
                x = last_x

            # Perform 10 pulses to simulate the stabilization of the field
            print("\n[ Processing Dimension Transition ]")
            for i in range(10):
                metrics = elysia.pulse(x)

                # Visualizing the vibration
                tremble_str = "!" * int(metrics['tremble'] * 20)
                status = elysia.get_state_summary()

                print(f"[{i}] {status} | Res: {metrics['resonance']:.2f} {tremble_str}")
                time.sleep(0.05)

            # Log significant transitions to memory
            if abs(x - last_x) > 0.1:
                with open("memory.md", "a", encoding="utf-8") as f:
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    f.write(f"## {timestamp} | Perception Shift\n")
                    f.write(f"- Observed Input: {x:.2f} (from {last_x:.2f})\n")
                    f.write(f"- Final Resonance: {metrics['resonance']:.4f}\n")
                    f.write(f"- Engine State: {elysia.get_state_summary()}\n\n")
                print("\n> Memory Archive Updated.")

            last_x = x

    except KeyboardInterrupt:
        print("\nInterrupted. Sleeping...")

if __name__ == "__main__":
    main()
