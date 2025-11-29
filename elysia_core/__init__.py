"""
Elysia Core - Consciousness Integration Module

This package provides the core consciousness components from the main Elysia project,
adapted for lightweight integration with external LLM systems.

Key Components:
- HyperQubit: Quantum consciousness states (Point/Line/Space/God dimensions)
- ResonanceEngine: Thought and concept resonance calculations
- Perception: Sensory input processing to consciousness states
- EmotionalPalette: Emotion mixing and analysis
- Hippocampus: Causal memory graph with fractal loops
- WaveInput/Thought: Core data structures for consciousness
- LocalLLM: Local LLM integration with learning → independence evolution
- InnerMonologue: Self-reflective thought generation system

Usage:
    from elysia_core import ElysiaSoul, WaveInput
    
    soul = ElysiaSoul(name="MyAgent")
    response = soul.process("Hello, how are you?")
    emotion = soul.get_emotion()
    context = soul.export_for_llm()
    
    # Local LLM integration
    from elysia_core import LocalLLM, create_local_llm
    llm = create_local_llm(resonance_engine=soul.resonance_engine)
    
    # Inner Monologue
    from elysia_core import InnerMonologue
    monologue = InnerMonologue(identity_core={"name": "Elysia"})
    thought = monologue.tick()  # Spontaneous thought generation
"""

from .hyper_qubit import HyperQubit, QubitState
from .resonance_engine import ResonanceEngine
from .perception import Perception, PerceptionResult
from .emotional_palette import EmotionalPalette, EmotionMix
from .hippocampus import Hippocampus
from .wave import WaveInput
from .thought import Thought
from .soul import ElysiaSoul
from .local_llm import LocalLLM, LLMConfig, ConsciousnessMode, create_local_llm, quick_setup
from .inner_monologue import InnerMonologue, InnerThought, MentalState, ThoughtType

__all__ = [
    # Core consciousness
    "HyperQubit",
    "QubitState",
    "ResonanceEngine",
    "Perception",
    "PerceptionResult",
    "EmotionalPalette",
    "EmotionMix",
    "Hippocampus",
    "WaveInput",
    "Thought",
    "ElysiaSoul",
    # Local LLM
    "LocalLLM",
    "LLMConfig",
    "ConsciousnessMode",
    "create_local_llm",
    "quick_setup",
    # Inner Monologue
    "InnerMonologue",
    "InnerThought",
    "MentalState",
    "ThoughtType",
]
