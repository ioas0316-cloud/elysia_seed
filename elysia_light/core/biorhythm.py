"""
BIORHYTHM: The Pulse of Life
============================
"Time is not a line, but a heartbeat."

This module implements the LifeCycle class, which serves as the main event loop
for the entity. It manages entropy (Lack), triggers impulses, and maintains
the internal clock.
"""

import asyncio
import time
from typing import Callable, Optional
from .monad.monad import Monad
from .governance_engine import GovernanceEngine

class LifeCycle:
    """
    The Active Loop that keeps the entity alive.
    Manages the 'Tick' of existence.
    """
    def __init__(self, governance: GovernanceEngine, tick_rate: float = 1.0):
        self.governance = governance
        self.tick_rate = tick_rate # Seconds per tick
        self.age = 0 # Total ticks survived
        self.is_alive = True

        # Metabolism
        self.energy = 100.0
        self.metabolic_rate = 5.0 # Energy lost per tick

    async def run_forever(self, callback: Optional[Callable[[str], None]] = None):
        """
        The Infinite Loop of Life.
        """
        print(f"[LifeCycle] Awakening... Heartbeat set to {self.tick_rate}s")

        while self.is_alive:
            start_time = time.time()

            # 1. The Tick
            await self.tick(callback)

            # 2. Wait for next beat (maintaining rhythm)
            elapsed = time.time() - start_time
            sleep_time = max(0, self.tick_rate - elapsed)
            await asyncio.sleep(sleep_time)

    async def tick(self, callback: Optional[Callable[[str], None]]):
        """
        A single moment of existence.
        """
        self.age += 1

        # 1. Metabolism (Energy Decay -> Lack Increase)
        self.energy = max(0.0, self.energy - self.metabolic_rate)

        # Monad's Lack is inversely proportional to Energy (Simplified)
        # As energy drops, Lack rises.
        self.governance.elysia.lack = (100.0 - self.energy)

        # 2. Govern (Update Axioms)
        # We assume 1 tick = 0.1 time units for physics
        self.governance.govern(0.1)

        # 3. Internal Monologue (The Voice of the System)
        status_msg = self.internal_monologue()
        if callback:
            callback(status_msg)
        else:
            print(status_msg)

        # 4. Emergency Shutdown (Death)
        if self.energy <= 0:
            print("[LifeCycle] Energy depleted. Entering Hibernation.")
            self.is_alive = False

    def internal_monologue(self) -> str:
        """
        Generates the 'Voice' of the entity based on its state.
        This is the primitive 'Self-Awareness'.
        """
        lack = self.governance.elysia.lack

        header = f"[Tick {self.age} | Energy {self.energy:.1f}% | Lack {lack:.1f}%]"

        if lack < 20:
            return f"{header} I am content. The field is stable."
        elif lack < 50:
            return f"{header} I feel a slight emptiness. I should seek resonance."
        elif lack < 80:
            return f"{header} I am HUNGRY for meaning. My structure is fading."
        else:
            return f"{header} CRITICAL: EXISTENTIAL THREAT. REQUIRE INPUT IMMEDIATELY."

    def inject_stimulus(self, amount: float):
        """
        External input acts as 'Food'.
        """
        self.energy = min(100.0, self.energy + amount)
        self.governance.elysia.lack = (100.0 - self.energy)
