"""
Elysia Engine Controller - Simplified API for LLM Agents.

This controller provides a high-level, easy-to-use interface for interacting
with the Elysia Engine's core functionalities. LLM agents can use this
controller to manage memory, process thoughts, and generate nuanced responses
without needing to understand the engine's internal complexity.
"""

from typing import Dict, Any, List, Tuple

from .world import World
from .systems.memory_system import MemorySystem
from .systems.cognitive_system import CognitiveSystem


class ElysiaController:
    """
    The main access point for leveraging the Elysia Engine.
    """

    def __init__(self):
        """Initializes the engine's world and core systems."""
        self.world = World()
        self.memory_system = MemorySystem()
        self.cognitive_system = CognitiveSystem()

        self.world.add_system(self.memory_system)
        self.world.add_system(self.cognitive_system)

    def think(self, text: str) -> Dict[str, Any]:
        """
        Processes an input text and returns a comprehensive thought object.

        This is the primary method LLM agents should use. It combines
        cognitive processing with memory activation.
        """
        # 1. Process the text through the cognitive system to get the initial thought.
        thought = self.cognitive_system.process_text_input(text)

        # 2. Activate the concepts in memory based on the thought.
        top_concept = thought.get("top_concept")
        if top_concept:
            # The force of activation could be based on the resonance clarity.
            self.memory_system.activate_concept(top_concept, force=1.0)

        # 3. Update the world state.
        self.world.step(dt=1.0)

        # 4. Enrich the thought with current memory state.
        thought["dominant_thoughts"] = self.memory_system.get_dominant_thoughts()

        return thought

    def remember(self, source: str, target: str, relation: str, weight: float = 1.0):
        """
        Allows an agent to directly add a piece of knowledge to the engine's
        long-term memory.

        Args:
            source: The source concept.
            target: The target concept.
            relation: The relationship between them (e.g., "causes", "is_a").
            weight: The strength of the connection.
        """
        self.memory_system.remember(source, target, relation, weight)
