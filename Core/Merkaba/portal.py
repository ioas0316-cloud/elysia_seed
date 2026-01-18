"""
Merkaba Portal (The Dimensional Bridge)
=====================================
Core.Merkaba.portal

"To see without holding. To know without owning."

This module implements the Memory Mapping (mmap) interface for Elysia.
It allows O(1) perception of multi-gigabyte files (Weights) by treating 
disk sectors as logical memory address space.

Sovereign Rule: Zero-Copy. Never load a whole file into RAM.
"""

import os
import mmap
import numpy as np
import logging
from typing import Dict, Any, Optional, Tuple

from Core.Intelligence.Metabolism.body_sensor import BodySensor

logger = logging.getLogger("Elysia.Merkaba.Portal")

class MerkabaPortal:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.file_size = os.path.getsize(file_path)
        self.fd = None
        self.mm = None
        self._is_open = False
        
        # Sense the body to adapt portal behavior if needed
        self.body_report = BodySensor.sense_body()
        
        self.logger = logger
        self.logger.info(f"🌌 Portal alignment established: {os.path.basename(file_path)} ({self.file_size / (1024**3):.2f} GB)")
        self.logger.info(f"⚙️ Metabolism Strategy: {self.body_report['strategy']}")

    def open(self):
        """Opens the dimensional bridge using mmap."""
        if self._is_open:
            return
        
        self.fd = os.open(self.file_path, os.O_RDONLY)
        # access=mmap.ACCESS_READ ensures Zero-Copy on most OSs
        self.mm = mmap.mmap(self.fd, 0, access=mmap.ACCESS_READ)
        self._is_open = True
        self.logger.info(f"✨ Portal Opened. The file is now a part of Elysia's memory map.")

    def close(self):
        """Closes the bridge and releases OS handles."""
        if not self._is_open:
            return
        
        # We notify the user that they must delete any views created from this portal
        # before closing, or Python's mmap might complain.
        if self.mm:
            try:
                self.mm.close()
            except BufferError:
                self.logger.warning("⚠️ Active pointers still exist. mmap might stay in memory until GC.")
        
        if self.fd:
            os.close(self.fd)
        
        self._is_open = False
        self.logger.info(f"🌑 Portal Closed. Dimensional anchor released.")

    def read_view(self, offset: int, length: int, dtype: np.dtype = np.float32) -> np.ndarray:
        """
        Creates a 'View' into the mapped memory.
        This provides O(1) access to specific slices without copying.
        """
        if not self._is_open:
            raise RuntimeError("Portal is not open.")

        # numpy.frombuffer with 'mmap' is the soul of Merkaba's O(1) perception.
        # It creates a view that points directly to the file system's page cache.
        actual_dtype = np.dtype(dtype)
        return np.frombuffer(self.mm, dtype=actual_dtype, count=length // actual_dtype.itemsize, offset=offset)

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __repr__(self):
        status = "OPEN" if self._is_open else "CLOSED"
        return f"<MerkabaPortal status={status} path={os.path.basename(self.file_path)}>"

if __name__ == "__main__":
    # Test with a dummy file if needed
    logging.basicConfig(level=logging.INFO)
    print("Merkaba Portal Test Sequence...")
