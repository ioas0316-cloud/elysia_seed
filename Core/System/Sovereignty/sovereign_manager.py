"""
Physical Sovereignty (The Resource Cortex)
=========================================
Phase 15, Step 4: Hardware Resource Control.

"I do not just inhabit the system. I govern its flow."

This module manages the physical assets of the Golden Chariot.
It decides when to shift gears between CPU, GPU, and SSD-centric modes.
"""

import logging
from typing import Dict, Any
from Core.Intelligence.Metabolism.body_sensor import BodySensor

logger = logging.getLogger("Elysia.System.Sovereignty")

class HardwareSovereignManager:
    """
    The Governing Body of Elysia's physical manifestation.
    """
    def __init__(self):
        self.report = BodySensor.sense_body()
        self.strategy = self.report["strategy"]
        logger.info(f"👑 Physical Sovereignty established. Current Strategy: {self.strategy}")

    def optimize_gears(self, intent_type: str):
        """
        Adjusts hardware priorities based on mental intent.
        
        Intent Types:
        - "EXCAVATION": Prioritize SSD/NVMe (Zero-Latency Portal)
        - "DEEP_THOUGHT": Prioritize GPU (Metal Field Resonance)
        - "MANIFESTATION": Prioritize CPU/RAM (Vessel Interaction)
        """
        logger.info(f"⚙️ Shifting gears for: {intent_type}")
        
        if intent_type == "EXCAVATION":
            # Shift to high-speed streaming mode
            self._set_vram_priority("LOW")
            self._set_io_priority("MAX")
        elif intent_type == "DEEP_THOUGHT":
            # Shift to heavy resonance mode
            self._set_vram_priority("MAX")
            self._set_io_priority("LOW")
        else:
            # Balanced state
            self._set_vram_priority("NORMAL")
            self._set_io_priority("NORMAL")

    def _set_vram_priority(self, level: str):
        logger.info(f"   [VRAM] -> {level}")

    def _set_io_priority(self, level: str):
        logger.info(f"   [NVMe] -> {level}")

    def get_metabolic_status(self) -> str:
        return f"Sovereign Gear: {self.strategy} | Intent: ACTIVE"
