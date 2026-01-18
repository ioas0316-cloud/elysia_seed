"""
Metal Rotor Bridge (The Iron Bridge)
=====================================
Phase 15, Step 1: Hardware Direct Coupling.

This module uses Numba CUDA to move Rotor physics directly onto the GPU.
It allows for parallel rotation of thousands of rotors in a single 
'Hardware Heartbeat', bypassing the Python Interpreter loop.
"""

import numpy as np
from numba import cuda
import math
import logging

logger = logging.getLogger("Foundation.MetalRotor")

# CUDA Kernel for parallel Rotor updates
@cuda.jit
def rotor_update_kernel(angles, current_rpms, target_rpms, accelerations, idle_rpms, dt, n):
    """
    Parallel CUDA Kernel: Each thread updates ONE rotor.
    O(1) time complexity for any number of rotors (up to GPU thread limits).
    """
    idx = cuda.grid(1)
    if idx < n:
        # 1. RPM Interpolation
        target = target_rpms[idx]
        current = current_rpms[idx]
        accel = accelerations[idx]
        
        if current != target:
            diff = target - current
            change = accel * dt
            if abs(diff) < change:
                current_rpms[idx] = target
            else:
                if diff > 0:
                    current_rpms[idx] += change
                else:
                    current_rpms[idx] -= change
        
        # 2. Angle Update
        current_rpm = current_rpms[idx]
        if current_rpm != 0:
            degrees = (current_rpm / 60.0) * 360.0 * dt
            angles[idx] = (angles[idx] + degrees) % 360.0

class MetalRotorBridge:
    """
    The 'Iron Bridge' connecting Python Intent to CUDA Reality.
    Manages GPU-side buffers for all active Rotors.
    """
    def __init__(self, max_rotors=10000):
        self.max_rotors = max_rotors
        
        # GPU Host-side Arrays (Pinned memory for fast transfer)
        self.angles = np.zeros(max_rotors, dtype=np.float32)
        self.current_rpms = np.zeros(max_rotors, dtype=np.float32)
        self.target_rpms = np.zeros(max_rotors, dtype=np.float32)
        self.accelerations = np.zeros(max_rotors, dtype=np.float32)
        self.idle_rpms = np.zeros(max_rotors, dtype=np.float32)
        
        # GPU Device-side Buffers
        self.d_angles = cuda.to_device(self.angles)
        self.d_current_rpms = cuda.to_device(self.current_rpms)
        self.d_target_rpms = cuda.to_device(self.target_rpms)
        self.d_accelerations = cuda.to_device(self.accelerations)
        self.d_idle_rpms = cuda.to_device(self.idle_rpms)
        
        self.active_count = 0
        logger.info(f"🦾 MetalRotorBridge Initialized. GPU Capacity: {max_rotors} Rotors.")

    def sync_to_gpu(self):
        """Uploads current states to GPU."""
        self.d_angles.copy_to_device(self.angles)
        self.d_current_rpms.copy_to_device(self.current_rpms)
        self.d_target_rpms.copy_to_device(self.target_rpms)
        self.d_accelerations.copy_to_device(self.accelerations)
        self.d_idle_rpms.copy_to_device(self.idle_rpms)

    def sync_from_gpu(self):
        """Downloads updated states from GPU."""
        self.d_angles.copy_to_host(self.angles)
        self.d_current_rpms.copy_to_host(self.current_rpms)

    def pulse(self, dt: float):
        """
        Executes the 'Metal Heartbeat'.
        Launches the CUDA kernel to update all rotors in parallel.
        """
        if self.active_count == 0:
            return

        threads_per_block = 256
        blocks_per_grid = (self.active_count + (threads_per_block - 1)) // threads_per_block
        
        rotor_update_kernel[blocks_per_grid, threads_per_block](
            self.d_angles, 
            self.d_current_rpms, 
            self.d_target_rpms, 
            self.d_accelerations, 
            self.d_idle_rpms, 
            dt, 
            self.active_count
        )

    def register_rotor(self, angle, current_rpm, target_rpm, accel, idle_rpm):
        """Adds a rotor to the metal pool."""
        if self.active_count >= self.max_rotors:
            logger.error("❌ MetalRotorBridge capacity exceeded!")
            return -1
        
        idx = self.active_count
        self.angles[idx] = angle
        self.current_rpms[idx] = current_rpm
        self.target_rpms[idx] = target_rpm
        self.accelerations[idx] = accel
        self.idle_rpms[idx] = idle_rpm
        
        self.active_count += 1
        return idx
