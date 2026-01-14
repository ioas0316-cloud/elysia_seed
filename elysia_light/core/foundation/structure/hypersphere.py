"""
THE HYPERSPHERE: The Manifold of Potential
==========================================
"Space is Memory. Distance is Meaning."

The HyperSphere is the 4D spatial container for all Rotors.
It replaces the "List" or "Database".
It implements "Lightning Paths" for retrieval.
"""

from typing import List, Optional
from ..nature.rotor import Rotor, Vector4

class HyperSphere:
    """
    The High-Dimensional Manifold.
    """
    def __init__(self):
        self._rotors: List[Rotor] = []

    def exist(self, entity: Rotor):
        """
        Materialize an entity into the Manifold.
        """
        # In a real engine, we would assign a spatial coordinate based on semantic embedding.
        # For the Seed, we assign a random location or 0.
        # self.assign_coordinate(entity)
        self._rotors.append(entity)
        print(f"[HyperSphere] Materialized: {entity}")

    def pulse(self, delta_time: float):
        """
        The Universal Heartbeat.
        Updates the state of all resident Rotors.
        """
        for r in self._rotors:
            r.spin(delta_time)

    def lightning_path(self, origin: Vector4, intent_freq: float, exclude_self_name: str = None) -> Optional[Rotor]:
        """
        Casts a 'Ray' of attention through the manifold to find resonance.
        Replces 'Search'.
        """
        best_rotor = None
        max_resonance = 0.0

        # This is the "Ray" piercing the sphere
        for r in self._rotors:
            if exclude_self_name and r.name == exclude_self_name:
                continue

            # Calculate Resonance based on Frequency (Identity)
            # We treat the query as a "Ghost Rotor" with the intent frequency
            # Note: In a full simulation, we would sync phases,
            # but for retrieval we look for "Timeless Resonance" (Frequency Match)
            resonance = 1.0 / (1.0 + abs(r.frequency - intent_freq))

            if resonance > max_resonance:
                max_resonance = resonance
                best_rotor = r

        if max_resonance > 0.1: # Lowered Threshold for "Found" (Since exact match is rare)
            return best_rotor
        return None

    @property
    def population(self):
        return len(self._rotors)
