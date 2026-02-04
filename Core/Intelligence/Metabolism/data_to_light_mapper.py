"""
Data-to-Light Mapper v2 (The Prismatic Converter)
=================================================
Core.Intelligence.Metabolism.data_to_light_mapper

"We do not assign meaning. We reveal phase."

This module is now a thin wrapper around MetalTrinaryLogic,
providing convenience methods for different data types.
The actual conversion is done by deriving trinary state from bit patterns.
"""

import numpy as np
import logging
from typing import List

from Core.Foundation.Nature.metal_trinary_logic import (
    MetalTrinaryLogic, TrinaryField, LIGHT, VOID, REFRACT
)

logger = logging.getLogger("Intelligence.DataToLight")

class DataToLightMapper:
    """
    Converts raw signals into Trinary Light Fields.
    Uses MetalTrinaryLogic for true bit-pattern based conversion.
    """
    
    def __init__(self):
        self.logic = MetalTrinaryLogic()
        logger.info("💡 DataToLightMapper v2 Initialized (Bit-Pattern Mode).")
    
    def text_to_light(self, text: str) -> np.ndarray:
        """Converts text to trinary via byte-level bit pattern analysis."""
        return self.logic.text_to_trits(text)
    
    def bytes_to_light(self, data: bytes) -> np.ndarray:
        """Direct byte stream conversion."""
        return self.logic.stream_to_trits(data)
    
    def semantic_to_light(self, scores: List[float]) -> np.ndarray:
        """
        Converts semantic analysis scores (e.g., from NLP models) to Trinary.
        For continuous values, we use a physical threshold approach.
        """
        light_field = []
        for score in scores:
            if score > 0.3:
                light_field.append(LIGHT)
            elif score < -0.3:
                light_field.append(REFRACT)
            else:
                light_field.append(VOID)
        return np.array(light_field, dtype=np.int8)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    mapper = DataToLightMapper()
    
    # Test: Text to Light via Bit Patterns
    sample_text = "Hello! Is this working?"
    light = mapper.text_to_light(sample_text)
    print(f"Text: '{sample_text}'")
    print(f"Light Field: {light}")
    print(f"  -> LIGHT count: {np.sum(light == LIGHT)}")
    print(f"  -> REFRACT count: {np.sum(light == REFRACT)}")
    print(f"  -> VOID count: {np.sum(light == VOID)}")
    
    void_ratio = np.sum(light == VOID) / len(light)
    print(f"\n  Anti-gravity Efficiency: {void_ratio:.1%} of data is transparent (VOID)")
