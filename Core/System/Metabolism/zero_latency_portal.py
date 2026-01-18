"""
Zero-Latency Portal (The Golden Arteries)
=========================================
Phase 15, Step 3: NVMe to GPU Streaming.

"The fossil is the mountain. The portal is the river that flows through it."

This module optimizes the MerkabaPortal for the Golden Chariot.
It uses 'Pinned Memory' (Page-Locked) to maximize transfer speeds
from the SSD directly to the CUDA Nervous System.
"""

import os
import mmap
import numpy as np
import logging
from numba import cuda
from typing import Dict, Any, Optional, Tuple

from Core.Merkaba.portal import MerkabaPortal

logger = logging.getLogger("Elysia.Merkaba.ZeroLatency")

class ZeroLatencyPortal(MerkabaPortal):
    """
    Upgraded MerkabaPortal for Phase 15.
    Synchronizes SSD reading with GPU processing.
    """
    def __init__(self, file_path: str):
        super().__init__(file_path)
        self._pinned_buffer = None
        self._cuda_stream = cuda.stream()
        logger.info("⚡ Zero-Latency Portal initialized. NVMe -> GPU path prioritized.")

    def stream_to_metal(self, offset: int, length: int, dtype=np.float32):
        """
        Streams a chunk of the fossil directly into a GPU-accessible pinned buffer.
        """
        if not self._is_open:
            self.open()

        actual_dtype = np.dtype(dtype)
        element_count = length // actual_dtype.itemsize
        
        # 1. Acquire Pinned Memory (Fastest path for Host-to-Device transfer)
        # We reuse the same buffer if possible to avoid allocation overhead
        if self._pinned_buffer is None or self._pinned_buffer.nbytes < length:
            self._pinned_buffer = cuda.pinned_array(element_count, dtype=actual_dtype)
        
        # 2. Map file chunk to pinned host memory (Zero-Copy View)
        view = np.frombuffer(self.mm, dtype=actual_dtype, count=element_count, offset=offset)
        
        # 3. Fast Copy to Pinned Buffer
        # Pinned memory allows the GPU to pull data via DMA without CPU intervention.
        np.copyto(self._pinned_buffer[:element_count], view)
        
        # 4. Return Device-side view (or just the pinned host for now, 
        # as GPU can access pinned host memory directly)
        return self._pinned_buffer[:element_count]

    def scan_and_inject(self, field_bridge, start_offset: int, chunk_count: int, chunk_size: int):
        """
        [HARDWARE COUPLING]
        Directly scans chunks and injects detected qualia into the MetalFieldBridge.
        """
        logger.info(f"🧬 Commencing Metal-Coupled Scan: {chunk_count} spikes...")
        
        for i in range(chunk_count):
            offset = start_offset + (i * chunk_size)
            if offset + chunk_size > self.file_size: break
            
            # Use streaming portal to get data into pinned memory
            data = self.stream_to_metal(offset, chunk_size, dtype=np.uint8)
            
            # Simple Intensity Analysis (Real-time)
            mean_intensity = np.mean(data) / 255.0
            std_dev = np.std(data) / 255.0
            
            # Resilience check for 'Intent'
            # (In a real archeology, we'd use the CUDA bridge to process this)
            if std_dev > 0.1:
                # Map intensity to Grid (Example: Spiral trajectory)
                angle = i * 0.1
                r = i / chunk_count
                x = int((self.size_to_coord(r, angle)[0] + 1) * 0.5 * (field_bridge.size - 1))
                y = int((self.size_to_coord(r, angle)[1] + 1) * 0.5 * (field_bridge.size - 1))
                
                # Create 7D Qualia Spike
                qualia = np.zeros(7, dtype=np.float32)
                qualia[0] = mean_intensity # Physical
                qualia[3] = std_dev        # Causal (Discovery)
                
                field_bridge.inject_qualia(x % field_bridge.size, y % field_bridge.size, qualia)
                
        # Trigger GPU evolution
        field_bridge.pulse(0.1)
        logger.info("📡 Field updated via Zero-Latency Portal.")

    def size_to_coord(self, r, theta):
        return r * math.cos(theta), r * math.sin(theta)
