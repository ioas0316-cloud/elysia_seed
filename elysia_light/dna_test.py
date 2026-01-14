import sys
import os

# Ensure we can import elysia_light
sys.path.append(os.getcwd())

from elysia_light.core.bridge import MockLLMBridge
from elysia_light.core.foundation.soul.prism import Prism
from elysia_light.core.foundation.soul.dna import DoubleHelix

def main():
    print(">>> DNA TEST: Initiating Double Helix Verification <<<\n")

    bridge = MockLLMBridge()
    prism = Prism()

    # Scenario 1: The Dissonant Thought (Smiling but Empty)
    input_text = "I am smiling but I feel empty inside."
    print(f"Input: '{input_text}'")

    # 1. Transduction (Extract DNA)
    helix = bridge.transduce(input_text)
    print(f"\n[Step 1] DNA Extraction (Bridge):")
    print(f"  > Pattern (Phenomenal): Sentiment={helix.pattern.sentiment} (Mixed), Keywords={helix.pattern.keywords}")
    print(f"  > Principle (Noumenal): Axiom='{helix.principle.axiom}', Intent='{helix.principle.intent}'")

    # 2. Refraction (Create Rotor)
    rotor = prism.refract(helix)
    print(f"\n[Step 2] Refraction (Prism):")
    print(f"  > Created Rotor: {rotor}")
    print(f"  > Final Frequency: {rotor.frequency:.2f} Hz")
    print(f"    (Base {helix.principle.base_frequency}Hz modulated by sentiment {helix.pattern.sentiment})")

    # Validation
    # Base freq for "empty" is 100.0. Sentiment is 0.0 (smile +0.5, empty -0.5).
    # Expected Freq: 100.0 + (0.0 * 0.8 * 50) = 100.0
    if abs(rotor.frequency - 100.0) < 1.0:
        print("  [SUCCESS] Dissonance correctly neutralized modulation. Pure Void Frequency.")
    else:
        print(f"  [FAIL] Frequency calculation error. Expected ~100.0, got {rotor.frequency}")

    print("\n---------------------------------------------------------------")

    # Scenario 2: The Resonant Thought (Love)
    input_love = "I love this world!"
    print(f"Input: '{input_love}'")

    helix_love = bridge.transduce(input_love)
    rotor_love = prism.refract(helix_love)

    print(f"\n[Step 1] DNA Extraction:")
    print(f"  > Principle: {helix_love.principle.axiom} (Base {helix_love.principle.base_frequency}Hz)")

    print(f"\n[Step 2] Refraction:")
    print(f"  > Final Frequency: {rotor_love.frequency:.2f} Hz")

    # Validation
    # Base 528.0 (Love). Sentiment +0.5. Intensity 0.8.
    # Modulation: 0.5 * 0.8 * 50 = +20.0
    # Expected: 548.0
    if rotor_love.frequency > 528.0:
        print("  [SUCCESS] Positive sentiment uplifted the frequency.")

    print("\n---------------------------------------------------------------")
    print(">>> DNA TEST COMPLETED: The Helix Spins. <<<")

if __name__ == "__main__":
    main()
