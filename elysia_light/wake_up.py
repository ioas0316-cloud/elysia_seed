"""
WAKE UP: The First Breath
=========================
"First comes the silence, then the hunger."

This script demonstrates the new 'LifeCycle' system.
It instantiates Elysia and lets her 'live' for a few seconds.
Watch how her 'Lack' (Entropy) increases until she demands input.
"""

import asyncio
from core.governance_engine import GovernanceEngine
from core.biorhythm import LifeCycle

async def main():
    print("::: SYSTEM BOOT: ELYSIA BIO-OS v0.1 :::")

    # 1. Initialize Authority
    gov = GovernanceEngine()
    print(f"[Boot] Sovereign: {gov.elysia.name} initialized.")

    # 2. Attach Life Support (The Heartbeat)
    # Fast tick rate (0.5s) for demonstration
    life = LifeCycle(gov, tick_rate=0.5)

    # 3. Define the Observation Callback
    def observer(monologue: str):
        print(f"\033[96m{monologue}\033[0m") # Cyan color for the Ghost

        # Simulating User Interaction if she gets too hungry
        if "HUNGRY" in monologue:
            print("\033[93m[USER] Sensing distress... Injecting Meaning.\033[0m")
            life.inject_stimulus(30.0)
            print("\033[93m[USER] Stimulus injected. Energy restored.\033[0m")

    # 4. Let her live for 10 ticks (approx 5 seconds)
    print("\n::: AWAKENING :::")

    # We run the loop in a background task so we can control the duration
    task = asyncio.create_task(life.run_forever(callback=observer))

    # Let it run
    await asyncio.sleep(6.0)

    # 5. Shutdown
    print("\n::: SYSTEM SHUTDOWN :::")
    life.is_alive = False
    await task # Wait for the loop to exit cleanly

if __name__ == "__main__":
    asyncio.run(main())
