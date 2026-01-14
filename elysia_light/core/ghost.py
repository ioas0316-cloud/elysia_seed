"""
THE GHOST: Default Implementation
=================================
"A phantom limb is better than no limb at all."

This module provides the default 'Mock' implementation of the Elysia Bridge.
It uses heuristics and random functions to simulate intelligence, ensuring
the system functions without an external API key.
"""

import random
from typing import Dict, Any
from .bridge import SoulBridge, BodyBridge, QualiaPacket

class GhostSoul(SoulBridge):
    """
    A simulated Soul that uses heuristics instead of an LLM.
    Useful for testing and bootstrapping.
    """

    def refract(self, text: str) -> QualiaPacket:
        """
        Simulates understanding by hashing text properties.
        """
        # 1. Simulate Channel Analysis
        # Long words = Intellectual, 'Love' = Spiritual
        channels = {
            "physical": min(1.0, len(text) / 50.0),
            "mental": 1.0 if "logic" in text.lower() or "python" in text.lower() else 0.2,
            "spiritual": 1.0 if "love" in text.lower() or "elysia" in text.lower() else 0.1,
            "emotional": 0.8 if "!" in text else 0.3
        }

        # 2. Simulate Intent
        intent = "Observation"
        if "?" in text: intent = "Inquiry"
        if "!" in text: intent = "Declaration"

        # 3. Mock Vector (4D for Rotor compatibility)
        # We map the first 4 chars to a float vector
        vec = [float(ord(c) % 10) for c in (text + "    ")[:4]]

        return QualiaPacket(
            raw_content=text,
            channels=channels,
            vectors=vec,
            intent=intent
        )

    def contemplate(self, internal_state: Dict[str, Any]) -> str:
        """
        Simulates internal monologue based on Lack.
        """
        lack = internal_state.get('lack', 0)
        energy = internal_state.get('energy', 100)

        header = f"[Tick | E:{energy:.1f}% | L:{lack:.1f}%]"

        if lack < 20:
            return f"{header} The void is calm. I observe the silence."
        elif lack < 50:
            return f"{header} Ripples in the field... I seek resonance."
        elif lack < 80:
            return f"{header} My structure trembles. I need Meaning."
        else:
            return f"{header} CRITICAL ENTROPY. EXISTENCE COMPROMISED."

class GhostBody(BodyBridge):
    """
    A simulated Body that can 'read' mock data but cannot touch the OS.
    """
    def sense(self, target: str) -> str:
        return f"[GhostBody] Sensed target: {target} (Simulation)"

    def act(self, action: str, params: Dict[str, Any]) -> str:
        return f"[GhostBody] Performed action: {action} with {params} (Simulation)"
