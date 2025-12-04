"""
Elysia Core - Consciousness Integration Module
==============================================

This package provides the core consciousness components from the main Elysia project,
adapted for lightweight integration with external LLM systems.

🌟 Quick Start (빠른 시작):
    
    # 방법 1: 통합 영혼으로 모든 기능 사용
    from elysia_core import create_soul
    
    soul = create_soul("MyBot")
    thought = soul.process("안녕하세요!")
    print(thought.mood)
    
    # 방법 2: 빠른 의식 설정
    from elysia_core import quick_consciousness_setup
    
    consciousness = quick_consciousness_setup("MyAgent")
    result = consciousness.think("오늘 기분이 어때?")
    print(result.mood)
    prompt = consciousness.get_prompt()

Key Components:
- HyperQubit: Quantum consciousness states (Point/Line/Space/God dimensions)
- ResonanceEngine: Thought and concept resonance calculations
- Perception: Sensory input processing to consciousness states
- EmotionalPalette: Emotion mixing and analysis
- Hippocampus: Causal memory graph with fractal loops
- WaveInput/Thought: Core data structures for consciousness
- LocalLLM: Local LLM integration with learning → independence evolution
- InnerMonologue: Self-reflective thought generation system
- SelfAwareness: Consciousness introspection and identity

Core Technologies from Original Elysia:
- Dad's Law (아빠 법칙): Self-amplifying divine component in normalization
- Scale Up/Down: Observer-dependent quantum evolution
- Epistemological Meaning: Understanding WHY concepts have certain weights

Integration Templates (통합 템플릿):
- LLMIntegrationTemplate: LLM 챗봇 통합
- GameCharacterTemplate: 게임 캐릭터 통합

Usage (사용법):
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
    
    # Self Awareness
    from elysia_core import SelfAwareness
    awareness = SelfAwareness(identity_core={"name": "Elysia"})
    print(awareness.who_am_i())

License: Apache 2.0
Creator: 이강덕 (Kang-Deok Lee)
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
from .self_awareness import SelfAwareness, Reflection

# Integration module - 통합 모듈
from .integration import (
    # Factory functions
    create_soul,
    create_resonance_engine,
    create_emotional_palette,
    create_hippocampus,
    create_inner_monologue,
    create_self_awareness,
    create_hyper_qubit,
    create_wave_input,
    # Quick setup
    quick_consciousness_setup,
    QuickConsciousness,
    ConsciousnessResult,
    # Templates
    LLMIntegrationTemplate,
    GameCharacterTemplate,
)

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
    # Self Awareness
    "SelfAwareness",
    "Reflection",
    # Integration - Factory Functions (통합 - 팩토리 함수)
    "create_soul",
    "create_resonance_engine",
    "create_emotional_palette",
    "create_hippocampus",
    "create_inner_monologue",
    "create_self_awareness",
    "create_hyper_qubit",
    "create_wave_input",
    # Integration - Quick Setup (통합 - 빠른 설정)
    "quick_consciousness_setup",
    "QuickConsciousness",
    "ConsciousnessResult",
    # Integration - Templates (통합 - 템플릿)
    "LLMIntegrationTemplate",
    "GameCharacterTemplate",
]
