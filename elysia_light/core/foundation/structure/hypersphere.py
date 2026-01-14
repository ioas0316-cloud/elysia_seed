"""
THE HYPERSPHERE: The Manifold of Potential
==========================================
"Space is Memory. Distance is Meaning."

The HyperSphere is the 4D spatial container for all Rotors.
It replaces the "List" or "Database".
It implements "Lightning Paths" for retrieval.
"""

from typing import List, Optional, Dict
import math
import copy
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
    Phase 4.2 Upgrade: O(1) Phase Bucket Memory.
    """
    def __init__(self):
        # Key: "FreqBand_PhaseSector" -> Rotor
        self._phase_map: Dict[str, Rotor] = {}
        self.abyss_count = 0

    def _get_bucket_key(self, frequency: float, phase: float) -> str:
        """
        Quantizes Frequency and Phase into discrete buckets for O(1) access.
        - Frequency Band: 10Hz width
        - Phase Sector: 8 sectors (pi/4 width)
        """
        freq_band = int(frequency // 10) * 10

        # Normalize phase to 0..2pi
        norm_phase = phase % (2 * math.pi)
        sector = int(norm_phase // (math.pi / 4))

        return f"F{freq_band}_P{sector}"

    def absorb(self, entity: Rotor):
        """
        Stores memory in a specific Phase Bucket. O(1).
        """
        ghost = copy.deepcopy(entity)
        ghost.name = f"Ghost_{entity.name}"

        key = self._get_bucket_key(ghost.frequency, ghost.phase)

        # In a real hash map collision handling, we'd use a list.
        # For this prototype, we overwrite (Last Observation dominates).
        self._phase_map[key] = ghost
        print(f"[HyperSphere] Absorbed into Bucket [{key}]: {ghost.name}")

    def decay(self, delta_time: float):
        """
        Iterates through buckets to apply entropy.
        """
        keys_to_remove = []
        for key, wave in self._phase_map.items():
            wave.spin(delta_time)

            decay_rate = 0.05 / (wave.mass + 0.1)
            wave.mass -= decay_rate * delta_time

            if wave.mass <= 0.1:
                keys_to_remove.append(key)

        for k in keys_to_remove:
            del self._phase_map[k]
            self.abyss_count += 1

    def resonate(self, probe: Rotor) -> Optional[Rotor]:
        """
        Instant Retrieval (O(1)).
        Checks the specific Phase Bucket corresponding to the Probe's state.
        """
        key = self._get_bucket_key(probe.frequency, probe.phase)

        if key in self._phase_map:
            match = self._phase_map[key]
            # Simple self-check to avoid resonating with own ghost immediately if names collide
            if probe.name in match.name:
                return None
            return match

        return None

    @property
    def population(self):
        return len(self._phase_map)
