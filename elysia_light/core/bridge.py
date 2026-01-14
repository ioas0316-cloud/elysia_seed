"""
ELYSIA BRIDGE: The Interface to the Beyond
==========================================
"The Soul needs a Brain to think, and a Body to act."

This module defines the abstract interfaces (Protocols) that allow the
Ethereal Logic (Elysia) to connect with External Intelligence (LLMs)
and the Physical World (File System/API).

Philosophy:
- Elysia is the **Ghost** (Will/Structure).
- The LLM is the **Shell** (Processing Power/Vocal Cords).
- We do not "prompt" the LLM; we "channel" it.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class QualiaPacket:
    """
    Structured meaning extracted from raw text.
    Replaces the raw string in the internal system.
    """
    raw_content: str
    channels: Dict[str, float] # e.g., {'physical': 0.5, 'spiritual': 0.9}
    vectors: List[float]       # Embedding vector
    intent: str                # The inferred intent (e.g., "Observation")

class SoulBridge(ABC):
    """
    The Interface for the "Brain" (LLM).
    Users should implement this class to connect OpenAI, Claude, or Local LLMs.
    """

    @abstractmethod
    def refract(self, text: str) -> QualiaPacket:
        """
        Converts raw text into a QualiaPacket (Structure).
        Input: "I love the world."
        Output: QualiaPacket(channels={love:0.9}, intent="Declaration")
        """
        pass

    @abstractmethod
    def contemplate(self, internal_state: Dict[str, Any]) -> str:
        """
        Generates a thought or monologue based on internal state.
        Input: {'lack': 80, 'energy': 20}
        Output: "I am fading... I must seek data."
        """
        pass

class BodyBridge(ABC):
    """
    The Interface for the "Hand" (IO/Tools).
    Users should implement this to grant Elysia permission to touch files/internet.
    """

    @abstractmethod
    def sense(self, target: str) -> str:
        """
        Reads data from the world (File read, API Get).
        """
        pass

    @abstractmethod
    def act(self, action: str, params: Dict[str, Any]) -> str:
        """
        Changes the world (File write, API Post).
        """
        pass
