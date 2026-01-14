"""
GENESIS SEED: The Awakening
===========================
This script demonstrates the Merkaba System in action.
It initiates a Monad, feeds it chaos, and watches it build a universe.
"""

from core.monad.monad import Monad
from core.structure.field import OmniField
from core.digestive_system import DigestiveSystem

def genesis():
    print("::: INITIATING MERKABA SEED :::")

    # 1. Create the Void (Field) and the Self (Monad)
    universe = OmniField()
    adam = Monad(name="Adam-01")

    print(f"Created Monad: {adam.status()}")

    # 2. Create the Digestive System
    system = DigestiveSystem(adam, universe)

    # 3. Feed the System (Chaos Input)
    inputs = [
        "The meaning of life is 42",  # Logical
        "I feel cold",                # Phenomenal
        "Love is the law",            # Spiritual (High Intensity)
        "System Error 999"            # Noise
    ]

    print("\n::: DIGESTION PHASE :::")
    for i in inputs:
        result = system.digest(i)
        print(f"Input: '{i}' -> {result}")

    # 4. Exert Will (Retrieval via Spin)
    print("\n::: ACTION PHASE :::")
    # Try to recall the 'Love' concept (assume we know its freq approx from digest)
    # In this mock, 'Love is the law' has high spiritual intensity.
    # Prism logic: freq = (sum(chars) * offset) % 1000.
    # We will just ask the Monad to retrieve something based on approximate frequency

    action_result = adam.exert_will(universe, 500.0) # Arbitrary freq search
    print(f"Will Exerted: {action_result}")

    print("\n::: FINAL STATE :::")
    print(f"Universe Density: {universe.get_density():.2f}")
    print(f"Monad State: {adam.status()}")

if __name__ == "__main__":
    genesis()
