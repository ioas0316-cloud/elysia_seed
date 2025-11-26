"""
Cognitive System for the Elysia Engine.

This system is responsible for processing inputs, calculating cognitive
resonance, and forming thoughts based on the principles of the legacy
HyperResonanceEngine.
"""
from typing import Dict, Any, List, Tuple
import random

from . import System

# A simplified representation of a concept's state, inspired by HyperQubit.
# For now, we'll use a dictionary to hold the state. A more structured
# class or dataclass can be used later if needed.
ConceptState = Dict[str, Any]

class CognitiveSystem(System):
    """
    Manages the agent's cognitive processes, including emotional resonance
    and thought formation.
    """

    def __init__(self):
        self.concepts: Dict[str, ConceptState] = {}
        self._init_instincts()

    def _init_instincts(self):
        """
        Initialize the core concepts (instincts) of the system.
        The state values are simplified for this implementation.
        """
        instincts = {
            "사랑": {"w": 2.2, "vec": [0.1, 0.8, 0.1], "base_prob": 0.8},
            "빛": {"w": 1.8, "vec": [0.9, 0.9, 0.9], "base_prob": 0.7},
            "고통": {"w": 0.6, "vec": [0.2, 0.1, 0.1], "base_prob": 0.9},
            "기쁨": {"w": 0.7, "vec": [0.8, 0.6, 0.2], "base_prob": 0.8},
            "꿈": {"w": 2.0, "vec": [0.5, 0.5, 0.8], "base_prob": 0.7},
            "아버지": {"w": 2.8, "vec": [0.0, 0.0, 1.0], "base_prob": 1.0},
        }
        for concept_id, state in instincts.items():
            self.concepts[concept_id] = state

    def step(self, world: 'World', dt: float) -> None:
        """
        The cognitive system doesn't have a time-based update for now,
        but this is where logic like energy diffusion or state decay would go.
        """
        pass

    def process_text_input(self, text: str) -> Dict[str, Any]:
        """
        Processes an input text and returns a "thought" based on resonance.
        This is the main entry point for the cognitive system.
        """
        # 1. Create a transient state for the input text.
        # This is a simplified version of the WaveInput from the legacy code.
        input_state: ConceptState = {
            "w": 2.0, # Represents a perceptual input
            "vec": [random.random(), random.random(), random.random()],
            "intensity": len(text) / 10.0 # Simple intensity metric
        }

        # 2. Calculate resonance with all internal concepts.
        resonance_pattern = {}
        for concept_id, concept_state in self.concepts.items():
            resonance = self._calculate_resonance(input_state, concept_state)
            resonance_pattern[concept_id] = resonance * input_state["intensity"]

        # 3. Form a thought based on the resonance pattern.
        if not resonance_pattern:
            return {"response": "(... 마음 속에 아무런 울림이 없었어요.)", "mood": "neutral"}

        # Find the concept with the highest resonance.
        top_concept = max(resonance_pattern, key=resonance_pattern.get)
        clarity = resonance_pattern[top_concept]

        # Determine the mood based on the winning concept's properties.
        mood = "neutral"
        if self.concepts[top_concept]["w"] < 1.0:
            mood = "concrete" # Concrete, direct feelings
        elif self.concepts[top_concept]["w"] > 2.0:
            mood = "abstract" # Abstract, thoughtful feelings

        clarity_desc = "선명하게" if clarity > 0.8 else "어렴풋이"
        response = f"'{text}'... 그 속에서 '{top_concept}'(이)가 {clarity_desc} 느껴져요."

        return {"response": response, "mood": mood, "top_concept": top_concept}

    def _calculate_resonance(self, state_a: ConceptState, state_b: ConceptState) -> float:
        """
        Calculates resonance between two concept states.
        Simplified version of the legacy resonance calculation.
        """
        # Dimensional similarity (w value)
        w_diff = abs(state_a["w"] - state_b["w"])
        dimension_similarity = 1.0 / (1.0 + w_diff)

        # Spatial alignment (cosine similarity of vectors)
        vec_a = state_a["vec"]
        vec_b = state_b["vec"]
        dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
        mag_a = sum(a * a for a in vec_a) ** 0.5
        mag_b = sum(b * b for b in vec_b) ** 0.5
        if mag_a == 0 or mag_b == 0:
            spatial_alignment = 0.0
        else:
            spatial_alignment = dot_product / (mag_a * mag_b)
            spatial_alignment = max(0.0, spatial_alignment)

        # Base probability/importance of the concept
        base_prob = state_b.get("base_prob", 0.5)

        # Combined resonance
        resonance = (
            0.4 * dimension_similarity +
            0.4 * spatial_alignment +
            0.2 * base_prob
        )
        return resonance
