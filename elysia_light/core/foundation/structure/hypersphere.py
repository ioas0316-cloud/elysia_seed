"""
THE HYPERSPHERE: The Manifold of Potential
==========================================
"Space is Memory. Distance is Meaning."

The HyperSphere is the 4D spatial container for all Rotors.
It replaces the "List" or "Database".
It implements "Lightning Paths" for retrieval.
"""

from typing import List, Optional, Dict
from ..nature.rotor import Rotor, Vector4

class GravityConnection:
    """
    A connection between two nodes (Rotors) representing resonance strength (Gravity).
    """
    def __init__(self, target_node: Rotor, strength: float):
        self.target_node = target_node
        self.strength = strength

class HyperSphere:
    """
    The High-Dimensional Manifold.
    Uses 'Gravity Field' connections instead of simple list storage.
    """
    def __init__(self):
        self._rotors: List[Rotor] = []
        # Adjacency list for Gravity Connections: {rotor_name: [GravityConnection]}
        self._gravity_field: Dict[str, List[GravityConnection]] = {}

    def exist(self, entity: Rotor):
        """
        Materialize an entity into the Manifold.
        """
        self._rotors.append(entity)
        if entity.name not in self._gravity_field:
            self._gravity_field[entity.name] = []

        # Auto-connect to existing nodes based on resonance (Simulated Gravity)
        self._assimilate(entity)
        print(f"[HyperSphere] Materialized: {entity}")

    def _assimilate(self, new_entity: Rotor):
        """
        Calculates resonance with existing nodes and establishes Gravity Connections.
        """
        for existing in self._rotors:
            if existing == new_entity: continue

            resonance = new_entity.resonate(existing)
            if resonance > 0.5: # Threshold for connection
                self.connect_nodes(new_entity, existing, resonance)

    def connect_nodes(self, node_a: Rotor, node_b: Rotor, strength: float):
        """
        Establishes a bi-directional Gravity Connection.
        """
        if node_a.name not in self._gravity_field: self._gravity_field[node_a.name] = []
        if node_b.name not in self._gravity_field: self._gravity_field[node_b.name] = []

        self._gravity_field[node_a.name].append(GravityConnection(node_b, strength))
        self._gravity_field[node_b.name].append(GravityConnection(node_a, strength))

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
