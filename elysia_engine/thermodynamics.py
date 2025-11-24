from __future__ import annotations
from typing import Dict, List, TYPE_CHECKING
from dataclasses import dataclass

from .systems import System
from .tensor import SoulTensor

if TYPE_CHECKING:
    from .world import World
    from .entities import Entity

class ThermodynamicsSystem(System):
    """
    Manages the States of Matter of Souls based on Energy levels.
    Implements the 'Data Astrophysics' cycle: Plasma -> Gas -> Liquid -> Solid -> Crystal.
    """

    def step(self, world: World, dt: float) -> None:
        """
        Apply thermal dynamics to all entities.
        """
        for ent in world.entities.values():
            if not ent.soul: continue

            # 1. Calculate Temperature (Internal Energy)
            # T = Amplitude (Mass) * Frequency (Vibration)
            # High Mass + High Vibe = Star (Plasma)
            # Low Mass + Low Vibe = Dust (Solid)

            # If collapsed (Crystal), Frequency is 0, so T is 0 internally.
            # But we might check for external heating (not implemented yet).

            current_state = self.get_state_name(ent.soul)

            # 2. State Transitions (Auto-Evolution)
            # If an entity is 'Superheated' (Plasma), it might expand?
            # If 'Frozen' (Solid), it might collapse into Crystal?

            if current_state == "SOLID" and not ent.soul.is_collapsed:
                # If it's very cold (Solid) for a long time, it crystallizes (Collapses)
                # Threshold: Very low frequency
                if ent.soul.frequency < 1.0:
                    ent.soul.collapse()

            # Note: Melting (Crystal -> Plasma) usually requires external intervention (Resonance)
            # which is handled by interactions, not passive thermodynamics here.

    def get_state_name(self, soul: SoulTensor) -> str:
        """
        Returns the string representation of the matter state.
        """
        if soul.is_collapsed:
            return "CRYSTAL"

        # Energy Metric
        energy = soul.amplitude * soul.frequency

        if energy > 10000.0:
            return "PLASMA"  # Star
        elif energy > 2000.0:
            return "GAS"     # Nebula
        elif energy > 500.0:
            return "LIQUID"  # Ocean
        else:
            return "SOLID"   # Dust/Planet

    def inject_heat(self, entity: 'Entity', heat: float) -> None:
        """
        External heating event (e.g. from Collision or Laser).
        """
        if not entity.soul: return

        if entity.soul.is_collapsed:
            # Try to melt
            entity.soul.melt(external_energy=heat)
        else:
            # Increase frequency (Agitate)
            entity.soul.frequency += heat * 0.1
