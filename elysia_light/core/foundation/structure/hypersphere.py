"""
THE HYPERSPHERE: The Manifold of Potential
==========================================
"Space is Memory. Distance is Meaning."

The HyperSphere is the 4D spatial container for all Rotors.
It replaces the "List" or "Database".
It implements "Lightning Paths" for retrieval.
"""

from typing import List, Optional, Dict, Union, Generator
import math
import copy
from ..nature.rotor import Rotor, Vector4

# Fractal Constants (The Laws of the World)
FREQ_BAND_WIDTH = 10.0
PHASE_SECTORS = 8

class OperationMode:
    """
    The Binary Rotor Modes.
    Dimensional Reduction using Bitmasks (Constraint Logic).

    1 = Fixed/Locked Axis (Constraint)
    0 = Flowing/Free Axis (Freedom)

    Format: [SpaceZ, SpaceY, SpaceX, Time] (Metaphorical)
    """
    POINT = "1111" # Lock All (Fact/Data) -> Precision: Infinite
    LINE  = "0001" # Lock Space, Flow Time (Story/Stream) -> Precision: Frequency Band
    PLANE = "0011" # Lock Core, Flow Time + Neighbors (Context/Harmony) -> Precision: Cluster
    SPACE = "0111" # Lock Center, Flow All (World/Simulation) -> Precision: Field

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
    Phase 4.5 Upgrade: Fractal Bitmask Engine.
    """
    def __init__(self):
        # Key: "FreqBand_PhaseSector" -> Rotor
        self._phase_map: Dict[str, Rotor] = {}
        self.abyss_count = 0

    def _get_bucket_key(self, frequency: float, phase: float) -> str:
        """
        Quantizes Frequency and Phase into discrete buckets.
        """
        freq_band = int(frequency // FREQ_BAND_WIDTH) * int(FREQ_BAND_WIDTH)

        # Normalize phase to 0..2pi
        norm_phase = phase % (2 * math.pi)
        sector_width = (2 * math.pi) / PHASE_SECTORS
        sector = int(norm_phase // sector_width)

        return f"F{freq_band}_P{sector}"

    def absorb(self, entity: Rotor):
        """
        Stores memory in a specific Phase Bucket. O(1).
        """
        ghost = copy.deepcopy(entity)
        ghost.name = f"Ghost_{entity.name}"

        key = self._get_bucket_key(ghost.frequency, ghost.phase)
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
        Wrapper for operate(POINT).
        """
        result = self.operate(probe, mode=OperationMode.POINT)
        return result if isinstance(result, Rotor) else None

    def operate(self, probe: Rotor, mode: str = OperationMode.POINT) -> Union[Optional[Rotor], List[Rotor]]:
        """
        The Elysia Fractal Bitmask Engine.
        Uses Bitmasks to determine the "Zoom Level" of reality retrieval.

        Args:
            probe: The Rotor acting as the query key.
            mode: OperationMode (POINT/LINE/PLANE/SPACE).
        """
        # Common: Determine base frequency band
        base_freq_band = int(probe.frequency // FREQ_BAND_WIDTH) * int(FREQ_BAND_WIDTH)

        # 1. POINT Mode (1111) - Exact Match
        if mode == OperationMode.POINT:
            key = self._get_bucket_key(probe.frequency, probe.phase)
            if key in self._phase_map:
                match = self._phase_map[key]
                if probe.name not in match.name:
                    return match
            return None

        # 2. Fractal Scan Logic (LINE, PLANE, SPACE)
        # Determine Scan Radius (Frequency Band Width)
        # LINE (0001): Radius 0 (Just this band)
        # PLANE (0011): Radius 1 (Neighbors)
        # SPACE (0111): Radius 5 (Wide Field)

        scan_radius = 0
        if mode == OperationMode.PLANE:
            scan_radius = 1
        elif mode == OperationMode.SPACE:
            scan_radius = 5

        stream = []

        # Iterate Frequency Bands (Spatial Zoom)
        start_band_idx = (base_freq_band // int(FREQ_BAND_WIDTH)) - scan_radius
        end_band_idx = (base_freq_band // int(FREQ_BAND_WIDTH)) + scan_radius

        for band_idx in range(start_band_idx, end_band_idx + 1):
            current_freq_band = band_idx * int(FREQ_BAND_WIDTH)

            # Iterate Phase Sectors (Time Flow) - Always Full Cycle for Streams
            for sector in range(PHASE_SECTORS):
                key = f"F{current_freq_band}_P{sector}"

                if key in self._phase_map:
                    memory = self._phase_map[key]
                    if probe.name not in memory.name:
                        stream.append(memory)

        # Sort by Phase to maintain Temporal Causality (Film Roll effect)
        # Secondary sort by Frequency to group harmonies
        stream.sort(key=lambda r: (r.phase, r.frequency))

        return stream

    @property
    def population(self):
        return len(self._phase_map)
