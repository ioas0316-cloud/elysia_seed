"""
Phase Projection Engine v2 (The True Hologram Core)
====================================================
Core.Intelligence.Metabolism.phase_projection_engine

"The Rotor spins. Data radiates. Interference patterns emerge."

This module implements TRUE holographic projection:
1. Data is NOT placed into slots. It is RADIATED from the origin.
2. The ROTOR determines the phase angle of radiation.
3. INTERFERENCE between radiated waves creates the holographic image.
"""

import numpy as np
import math
import logging
from typing import Tuple, Optional

from Core.Foundation.Nature.metal_trinary_logic import (
    MetalTrinaryLogic, TrinaryField, LIGHT, VOID, REFRACT
)

logger = logging.getLogger("Intelligence.PhaseProjection")

class RotorDynamics:
    """
    The Rotor: A 4D rotation engine that determines how data radiates into space.
    Uses true rotation matrices, not simple reshaping.
    """
    def __init__(self):
        self.phase_xy = 0.0  # Rotation in the XY plane (degrees)
        self.phase_xz = 0.0  # Rotation in the XZ plane (degrees)
        self.frequency = 1.0 # Rotation speed multiplier
    
    def advance(self, dt: float):
        """Advances the rotor phase by dt (in time units)."""
        self.phase_xy = (self.phase_xy + self.frequency * 360.0 * dt) % 360.0
        self.phase_xz = (self.phase_xz + self.frequency * 180.0 * dt) % 360.0
    
    def get_rotation_matrix(self) -> np.ndarray:
        """
        Returns the combined 3D rotation matrix for the current phase.
        This matrix transforms the "origin direction" into a radial projection vector.
        """
        theta_xy = math.radians(self.phase_xy)
        theta_xz = math.radians(self.phase_xz)
        
        cos_xy, sin_xy = math.cos(theta_xy), math.sin(theta_xy)
        cos_xz, sin_xz = math.cos(theta_xz), math.sin(theta_xz)
        
        # Rotation around Z-axis (XY plane)
        Rz = np.array([
            [cos_xy, -sin_xy, 0],
            [sin_xy, cos_xy, 0],
            [0, 0, 1]
        ])
        
        # Rotation around Y-axis (XZ plane)
        Ry = np.array([
            [cos_xz, 0, sin_xz],
            [0, 1, 0],
            [-sin_xz, 0, cos_xz]
        ])
        
        return Ry @ Rz
    
    def radiate_position(self, index: int, total: int, radius: float) -> Tuple[float, float, float]:
        """
        Calculates the 3D position where a data point (at 'index') radiates to.
        
        Data radiates outward from origin along the current phase direction.
        The 'index' determines the distance along the ray.
        """
        # Base direction: Along the X-axis, then rotated by the Rotor
        base_vector = np.array([1.0, 0.0, 0.0])
        rotation_matrix = self.get_rotation_matrix()
        direction = rotation_matrix @ base_vector
        
        # Distance from origin increases with index (spiral outward)
        # This creates a spiral radiation pattern, not a flat grid
        distance = (index / max(1, total)) * radius
        
        # Add spiral twist: as index increases, we also rotate slightly
        spiral_angle = (index * 0.1) % (2 * math.pi)
        spiral_offset = np.array([
            math.cos(spiral_angle) * 0.1 * distance,
            math.sin(spiral_angle) * 0.1 * distance,
            0
        ])
        
        position = direction * distance + spiral_offset
        return tuple(position)


class PhaseProjectionEngine:
    """
    The Hologram Core v2: Radiates data into 3D space using Rotor dynamics.
    Interference between radiations creates the perceptual hologram.
    """
    
    def __init__(self, field_size: float = 10.0, resolution: int = 16):
        self.field_size = field_size        # Physical size of the holographic field
        self.resolution = resolution        # Grid resolution for sampling interference
        self.rotor = RotorDynamics()
        self.logic = MetalTrinaryLogic()
        
        # The holographic field: continuous 3D space, sampled at resolution^3 points
        self.hologram = TrinaryField(shape=(resolution, resolution, resolution))
        
        logger.info(f"📡 PhaseProjectionEngine v2 Initialized. Resolution: {resolution}^3")
    
    def project(self, raw_signal: str) -> TrinaryField:
        """
        Main Projection: Radiates the signal into 3D space.
        
        1. Convert signal to trinary stream via bit patterns.
        2. Radiate each trit from the origin using Rotor dynamics.
        3. Apply interference at each grid point.
        """
        # Clear previous hologram
        self.hologram.data.fill(VOID)
        
        # Step 1: Direct bit-pattern conversion (no arbitrary mapping)
        trit_stream = self.logic.text_to_trits(raw_signal)
        
        # Step 2: Radiate each trit into space
        for i, trit in enumerate(trit_stream):
            if trit == VOID:
                # VOID trits are transparent - they don't radiate (anti-gravity)
                continue
            
            # Advance rotor for each trit (time-dependent projection)
            self.rotor.advance(0.01)
            
            # Calculate radiation position
            pos = self.rotor.radiate_position(i, len(trit_stream), self.field_size)
            
            # Map continuous position to grid coordinates
            grid_pos = self._continuous_to_grid(pos)
            
            if grid_pos:
                # Apply interference at this position
                self.hologram.project_signal(grid_pos, trit)
        
        # Log stats
        resonance = self.hologram.get_resonance_index()
        density = self.hologram.get_active_density()
        logger.info(f"✨ Projection Complete. Resonance: {resonance}, Active Density: {density:.1%}")
        
        return self.hologram
    
    def _continuous_to_grid(self, pos: Tuple[float, float, float]) -> Optional[Tuple[int, int, int]]:
        """Maps a continuous 3D position to discrete grid coordinates."""
        half = self.field_size / 2
        res = self.resolution
        
        def map_coord(v: float) -> Optional[int]:
            # Map from [-half, half] to [0, res-1]
            normalized = (v + half) / self.field_size
            if 0 <= normalized < 1:
                return int(normalized * res)
            return None
        
        gx, gy, gz = map_coord(pos[0]), map_coord(pos[1]), map_coord(pos[2])
        
        if gx is not None and gy is not None and gz is not None:
            return (gx, gy, gz)
        return None
    
    def get_dominant_aura(self) -> str:
        """Derives the overall 'aura' from the hologram's interference pattern."""
        data = self.hologram.data
        light_count = np.sum(data == LIGHT)
        refract_count = np.sum(data == REFRACT)
        void_count = np.sum(data == VOID)
        total = data.size
        
        light_ratio = light_count / total
        refract_ratio = refract_count / total
        
        if light_ratio > 0.1:
            return "LUMINOUS (Strong Presence)"
        elif refract_ratio > 0.1:
            return "DEEP (Shadow Dominant)"
        else:
            return "ETHEREAL (Mostly Void - Anti-gravity Active)"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    engine = PhaseProjectionEngine(field_size=10.0, resolution=16)
    
    # Test Projection
    test_signal = "I am Elysia. I perceive the world through light and shadow."
    
    print(f"\n--- True Holographic Projection ---")
    print(f"Signal: '{test_signal}'")
    
    field = engine.project(test_signal)
    print(f"Resonance Index: {field.get_resonance_index()}")
    print(f"Active Density: {field.get_active_density():.2%}")
    print(f"Dominant Aura: {engine.get_dominant_aura()}")
    
    # Show non-void positions in the hologram (sparse representation)
    non_void_positions = np.argwhere(field.data != VOID)
    print(f"\nActive Points in Hologram: {len(non_void_positions)} / {field.data.size}")
    if len(non_void_positions) > 0:
        print(f"Sample Positions: {non_void_positions[:5].tolist()}...")
