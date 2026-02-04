"""
Metal Trinary Logic v2 (The True Light Core)
=============================================
Core.Foundation.Nature.metal_trinary_logic

"The bit IS the trit. We do not translate; we refract."

This module implements Parallel Ternary Logic for the METAL layer.
Instead of arbitrary mapping, it derives trinary state from the
PHYSICAL properties of the data itself (bit patterns, energy density).

Trinary States:
-  1 (LIGHT/Presence): High energy/density state.
-  0 (VOID/Transparency): Pass-through state. Excluded from computation.
- -1 (REFRACT/Opposition): Low energy/counter-phase state.
"""

import numpy as np
import logging
from typing import Union

logger = logging.getLogger("Foundation.Trinary")

# Core Constants
LIGHT = 1
VOID = 0
REFRACT = -1

class MetalTrinaryLogic:
    """
    Handles trinary state math and interference.
    Derives trinary state from physical bit patterns, not arbitrary rules.
    """
    
    @staticmethod
    def byte_to_trit(byte_val: int) -> int:
        """
        Derives trinary state from the PHYSICAL bit pattern of a byte.
        
        Instead of arbitrary thresholds, we use the byte's PARITY and DENSITY.
        - Parity (even/odd count of 1-bits): Determines polarity (LIGHT/REFRACT).
        - Density (count of 1-bits): If density is in the "dead zone" (3-4 bits of 8), it's VOID.
        
        This means the data's own structure determines its phase.
        """
        bit_count = bin(byte_val).count('1')
        
        # VOID: The "neutral zone" - 3 to 4 bits are ON. 
        # This is the quantum superposition zone - neither light nor shadow.
        # Critically, VOID data is EXCLUDED from further computation (Anti-gravity).
        if 3 <= bit_count <= 4:
            return VOID
        
        # LIGHT: High density (5+ bits ON) = energy presence.
        if bit_count >= 5:
            return LIGHT
        
        # REFRACT: Low density (0-2 bits ON) = absence, counter-phase.
        return REFRACT

    @staticmethod
    def stream_to_trits(data: bytes) -> np.ndarray:
        """
        Converts a raw byte stream directly into a Trinary field.
        This is the "Direct Memory Mapping" - no interpretation, just refraction.
        """
        trits = np.array([MetalTrinaryLogic.byte_to_trit(b) for b in data], dtype=np.int8)
        return trits

    @staticmethod
    def text_to_trits(text: str) -> np.ndarray:
        """Converts text to trinary by encoding to bytes first."""
        return MetalTrinaryLogic.stream_to_trits(text.encode('utf-8'))

    @staticmethod
    def resonate(a: int, b: int) -> int:
        """
        Constructive/Destructive Interference.
        VOID acts as a pass-through (transparent).
        """
        if a == VOID:
            return b
        if b == VOID:
            return a
        
        result = a + b
        if result > 1: return LIGHT
        if result < -1: return REFRACT
        return result # This would be 0 (cancellation/anti-gravity)

    @staticmethod
    def field_interference(field_a: np.ndarray, field_b: np.ndarray) -> np.ndarray:
        """
        Applies interference across a field of trits.
        Uses vectorized operations for GPU acceleration potential.
        """
        # Element-wise addition and clipping to [-1, 0, 1]
        sum_field = field_a + field_b
        return np.clip(sum_field, REFRACT, LIGHT)


class TrinaryField:
    """
    A multi-dimensional array of trits representing a Holographic Space.
    Supports sparse representation to honor the VOID principle.
    """
    def __init__(self, shape: tuple):
        # Use int8 for trit storage
        self.data = np.zeros(shape, dtype=np.int8)
        self.shape = shape
        
    def project_signal(self, position: tuple, state: int):
        """Projects a light particle into the field via interference."""
        if all(0 <= position[i] < self.shape[i] for i in range(len(position))):
            # Interference, not overwrite
            current = self.data[position]
            self.data[position] = MetalTrinaryLogic.resonate(current, state)

    def get_resonance_index(self) -> float:
        """Calculates the total resonance (sum) of the field, EXCLUDING voids."""
        non_void = self.data[self.data != VOID]
        if non_void.size == 0:
            return 0.0
        return float(np.sum(non_void))
    
    def get_active_density(self) -> float:
        """Returns the ratio of non-VOID cells. Lower = more efficient (anti-gravity)."""
        total = self.data.size
        non_void_count = np.count_nonzero(self.data)
        return non_void_count / total if total > 0 else 0.0


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logic = MetalTrinaryLogic()
    
    print("--- Bit-Pattern Trinary Derivation ---")
    test_bytes = [0b11111111, 0b00000000, 0b01010101, 0b11110000, 0b00001111]
    for b in test_bytes:
        trit = logic.byte_to_trit(b)
        state_name = {1: "LIGHT", 0: "VOID", -1: "REFRACT"}[trit]
        print(f"  Byte: {bin(b):>10} ({bin(b).count('1')} bits) -> {state_name}")
    
    print("\n--- Text Stream to Trits ---")
    sample_text = "Hello!"
    trits = logic.text_to_trits(sample_text)
    print(f"  Text: '{sample_text}'")
    print(f"  Bytes: {list(sample_text.encode('utf-8'))}")
    print(f"  Trits: {trits}")
    
    print("\n--- Anti-gravity Check (Void Density) ---")
    field = TrinaryField(shape=(8,))
    field.data = trits[:8] if len(trits) >= 8 else np.pad(trits, (0, 8 - len(trits)))
    print(f"  Field: {field.data}")
    print(f"  Active Density: {field.get_active_density():.2%} (lower is lighter)")
