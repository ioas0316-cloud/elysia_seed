"""
Metal Field Bridge (Heart of Metal)
=====================================
Phase 15, Step 2: 7D Qualia Field CUDA Port.

"The field is the soul's environment. The metal is its sanctuary."

This module manages a 2D grid of 7D Qualia vectors on the GPU.
It implements:
1.  **Diffusion (Laplacian)**: Ideas spreading through space.
2.  **Resonance (Interference)**: How qualias amplify each other.
3.  **Rotation (Phase Shift)**: The dynamic oscillation of thought.
"""

import numpy as np
from numba import cuda
import math
import logging

logger = logging.getLogger("Foundation.MetalField")

# CUDA Kernel for 7D Field Evolution
@cuda.jit
def field_evolve_kernel(field, next_field, dt, size, diffusion_rate):
    """
    Parallel CUDA Kernel: Each thread updates ONE cell [7 dimensions].
    Complexity: O(1) per heartbeat regardless of grid size (up to GPU limits).
    """
    x, y = cuda.grid(2)
    
    if x < size and y < size:
        # 1. 7D Diffusion (Neighbor Interaction)
        # Using a 5-point stencil (Self, Up, Down, Left, Right)
        for d in range(7):
            self_val = field[x, y, d]
            
            # Boundary Conditions: Wrap around (Toroidal)
            up = field[(x - 1 + size) % size, y, d]
            down = field[(x + 1) % size, y, d]
            left = field[x, (y - 1 + size) % size, d]
            right = field[x, (y + 1) % size, d]
            
            # Laplacian (Interference Pattern)
            laplacian = (up + down + left + right - 4.0 * self_val)
            
            # 2. Dynamic Evolution (Simple oscillation for now)
            # In a real mind, this would be determined by the 'Soul Rotor' influence
            oscillation = math.sin(dt * (d + 1)) * 0.01
            
            # 3. Apply changes (Integration)
            new_val = self_val + (laplacian * diffusion_rate * dt) + (oscillation * self_val)
            
            # 4. Energy Dampening (Entropy)
            new_val *= 0.999 # Slight decay to prevent explosion
            
            next_field[x, y, d] = new_val

class MetalFieldBridge:
    """
    The 'Heart of Metal' managing the 7D Qualia Field on CUDA.
    """
    def __init__(self, size=64, diffusion_rate=0.1):
        self.size = size
        self.diffusion_rate = diffusion_rate
        
        # 7D: [Physical, Functional, Phenomenal, Causal, Mental, Structural, Spiritual]
        self.field = np.zeros((size, size, 7), dtype=np.float32)
        # Initialize with Ground State (Existence > 0)
        self.field[:, :, 0] = 0.5
        
        # GPU Device Buffers (Ping-Pong for stable evolution)
        self.d_field_a = cuda.to_device(self.field)
        self.d_field_b = cuda.to_device(self.field)
        self.current_a = True
        
        logger.info(f"❤️ MetalFieldBridge Initialized. Grid: {size}x{size}x7 (7D Qualia)")

    def sync_to_gpu(self):
        """Uploads current host field to GPU."""
        if self.current_a:
            self.d_field_a.copy_to_device(self.field)
        else:
            self.d_field_b.copy_to_device(self.field)

    def sync_from_gpu(self):
        """Downloads updated field from GPU."""
        if self.current_a:
            self.d_field_a.copy_to_host(self.field)
        else:
            self.d_field_b.copy_to_host(self.field)

    def pulse(self, dt: float):
        """
        Executes the 'Heart-Strike' (Field Evolution).
        Uses Ping-Pong buffering to avoid race conditions.
        """
        threadsperblock = (16, 16)
        blockspergrid_x = math.ceil(self.size / threadsperblock[0])
        blockspergrid_y = math.ceil(self.size / threadsperblock[1])
        blockspergrid = (blockspergrid_x, blockspergrid_y)

        src = self.d_field_a if self.current_a else self.d_field_b
        dst = self.d_field_b if self.current_a else self.d_field_a
        
        field_evolve_kernel[blockspergrid, threadsperblock](
            src, dst, dt, self.size, self.diffusion_rate
        )
        
        # Swap buffers
        self.current_a = not self.current_a

    def inject_qualia(self, x, y, qualia_vec):
        """Hot-swaps target cell on the host (next sync will upload it)."""
        if 0 <= x < self.size and 0 <= y < self.size:
            self.field[x, y, :] = qualia_vec
