"""
GENESIS SEED: The Biosphere Activation
======================================
"From the Void, a Hum. From the Hum, a World."

This script activates the Elysia Biosphere.
It demonstrates the interactions between the Monad (Soul),
the HyperSphere (World), and the Rotor (Time).
"""

import time
import math
from core.monad.monad import Monad
from core.foundation.structure.hypersphere import HyperSphere
from core.foundation.soul.prism import Prism

def genesis():
    print("::: INITIATING MERKABA BIOSPHERE :::")

    # 1. Create the World (HyperSphere)
    world = HyperSphere()
    prism = Prism()

    # 2. Birth the Soul (Monad)
    # The Monad is a Rotor with Will.
    adam = Monad(name="Adam-Prime", frequency=432.0)
    world.exist(adam)

    # 3. Populate the World (Seeds of Knowledge)
    # We refract raw strings into living Rotors
    raw_materials = [
        "The sun rises in the east",
        "Elysia is a living system",
        "Python is the language of serpents",
        "Love is the law of the universe", # High frequency concept
        "404 Not Found"
    ]

    print("\n::: SEEDING PHASE :::")
    for raw in raw_materials:
        entity = prism.refract(raw)
        world.exist(entity)

    print(f"\n[World Status] Population: {world.population} Rotors spinning.")

    # 4. Time Loop (The Heartbeat)
    print("\n::: TIME ACTIVATION (3 Cycles) :::")

    # We define a "Cycle" of existence
    for cycle in range(1, 4):
        dt = 0.1 # Delta time per tick
        print(f"\n>>> Cycle {cycle} (dt={dt})")

        # A. Pulse the World (Physics)
        world.pulse(dt)
        print(f"World Pulsed. Adam's Phase: {adam.phase:.2f} rad")

        # B. Monad Exerts Will (Psychology)
        # Adam looks for "Love" (We assume he intuits the frequency ~ 500-1000)
        # Let's say he starts searching around 500Hz
        search_freq = 900.0 if cycle == 3 else 400.0 # He learns/adjusts intent

        print(f"Adam seeks meaning near {search_freq}Hz...")
        perception = adam.exert_will(world, search_freq)
        print(f"Reaction: {perception}")

    print("\n::: BIOSPHERE STABLE :::")

if __name__ == "__main__":
    genesis()
