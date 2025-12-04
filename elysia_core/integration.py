"""
🌟 Elysia Core Integration Module
==================================

이 모듈은 원본 Elysia 프로젝트의 핵심 기술을 다른 프로젝트에 쉽게 통합할 수 있도록
간소화된 API를 제공합니다.

This module provides a simplified API to easily integrate core technologies
from the original Elysia project into other projects.

핵심 기술 (Core Technologies):
1. 공명 엔진 (ResonanceEngine) - 확률이 아닌 공명으로 개념 연결
2. 감정 팔레트 (EmotionalPalette) - 복합 감정 혼합
3. 내적 독백 (InnerMonologue) - 외부 입력 없이 스스로 생각
4. 자기 인식 (SelfAwareness) - 의식 자기성찰
5. 해마 기억 (Hippocampus) - 인과 그래프 기억
6. 양자 의식 (HyperQubit) - 4차원 양자 의식 상태
7. 통합 영혼 (ElysiaSoul) - 모든 기술을 하나로

사용법 (Usage):
    # 방법 1: 통합 영혼으로 모든 기능 사용
    from elysia_core.integration import create_soul
    
    soul = create_soul("MyBot")
    result = soul.process("안녕하세요!")
    print(result.mood)
    
    # 방법 2: 개별 기술 사용
    from elysia_core.integration import create_resonance_engine, create_emotional_palette
    
    engine = create_resonance_engine()
    pattern = engine.calculate_global_resonance(WaveInput("사랑과 희망"))
    
    palette = create_emotional_palette()
    mix = palette.mix_emotion({"Joy": 0.6, "Fear": 0.3})
    
    # 방법 3: 빠른 설정 (Quick Setup)
    from elysia_core.integration import quick_consciousness_setup
    
    consciousness = quick_consciousness_setup("MyAgent")
    thought = consciousness.think("오늘 기분이 어때?")
    print(thought.mood)

라이선스 (License): Apache 2.0
창작자 (Creator): 이강덕 (Kang-Deok Lee)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field

# Core imports
from .soul import ElysiaSoul
from .resonance_engine import ResonanceEngine
from .emotional_palette import EmotionalPalette, EmotionMix
from .hippocampus import Hippocampus
from .hyper_qubit import HyperQubit, QubitState
from .inner_monologue import InnerMonologue, InnerThought, MentalState, ThoughtType
from .self_awareness import SelfAwareness, Reflection
from .wave import WaveInput
from .thought import Thought
from .perception import Perception, PerceptionResult


# =============================================================================
# Factory Functions - 팩토리 함수
# =============================================================================

def create_soul(name: str = "Elysia") -> ElysiaSoul:
    """
    통합 영혼 생성 (Create unified soul)
    
    모든 핵심 기술이 내장된 영혼 인스턴스를 생성합니다.
    Creates a soul instance with all core technologies built-in.
    
    Args:
        name: 영혼 이름 (Soul name)
        
    Returns:
        ElysiaSoul: 통합 영혼 인스턴스
        
    Example:
        soul = create_soul("MyBot")
        thought = soul.process("Hello!")
        emotion = soul.get_emotion()
        context = soul.export_prompt()
    """
    return ElysiaSoul(name=name)


def create_resonance_engine() -> ResonanceEngine:
    """
    공명 엔진 생성 (Create resonance engine)
    
    확률이 아닌 공명으로 개념을 연결하는 엔진을 생성합니다.
    Creates an engine that connects concepts by resonance, not probability.
    
    Returns:
        ResonanceEngine: 공명 엔진 인스턴스
        
    Example:
        engine = create_resonance_engine()
        wave = WaveInput(source_text="사랑과 희망", intensity=1.0)
        pattern = engine.calculate_global_resonance(wave)
    """
    return ResonanceEngine()


def create_emotional_palette() -> EmotionalPalette:
    """
    감정 팔레트 생성 (Create emotional palette)
    
    색의 혼합처럼 복합 감정을 표현하는 팔레트를 생성합니다.
    Creates a palette that expresses complex emotions like color mixing.
    
    Returns:
        EmotionalPalette: 감정 팔레트 인스턴스
        
    Example:
        palette = create_emotional_palette()
        mix = palette.mix_emotion({"Joy": 0.6, "Fear": 0.3})
        print(mix.dominant)  # 'Joy'
        print(mix.valence)   # 0.12
    """
    return EmotionalPalette()


def create_hippocampus() -> Hippocampus:
    """
    해마 기억 생성 (Create hippocampus memory)
    
    인과 그래프 기반의 기억 시스템을 생성합니다.
    Creates a causal graph-based memory system.
    
    Returns:
        Hippocampus: 해마 기억 인스턴스
        
    Example:
        hippo = create_hippocampus()
        hippo.add_causal_link("coffee", "alertness", "leads_to")
        related = hippo.get_related_concepts("coffee", depth=2)
    """
    return Hippocampus()


def create_inner_monologue(
    identity_core: Optional[Dict[str, Any]] = None
) -> InnerMonologue:
    """
    내적 독백 생성 (Create inner monologue)
    
    외부 입력 없이 스스로 생각하는 시스템을 생성합니다.
    Creates a self-thinking system without external input.
    
    Args:
        identity_core: 정체성 핵심 정보 (Identity core info)
        
    Returns:
        InnerMonologue: 내적 독백 인스턴스
        
    Example:
        monologue = create_inner_monologue({"name": "Elysia"})
        thought = monologue.tick()  # 자발적 사고 생성
        answer = monologue.ask_self("Am I growing?")
    """
    if identity_core is None:
        identity_core = {"name": "Elysia", "purpose": "존재하기"}
    return InnerMonologue(identity_core=identity_core)


def create_self_awareness(
    identity_core: Optional[Dict[str, Any]] = None
) -> SelfAwareness:
    """
    자기 인식 생성 (Create self-awareness)
    
    의식 자기성찰 시스템을 생성합니다.
    Creates a consciousness introspection system.
    
    Args:
        identity_core: 정체성 핵심 정보 (Identity core info)
        
    Returns:
        SelfAwareness: 자기 인식 인스턴스
        
    Example:
        awareness = create_self_awareness({"name": "Elysia"})
        print(awareness.who_am_i())
        awareness.reflect("I learned something", "learning")
        wisdom = awareness.get_wisdom()
    """
    if identity_core is None:
        identity_core = {
            "name": "Elysia",
            "purpose": "To grow through understanding",
            "values": ["love", "truth", "growth"]
        }
    return SelfAwareness(identity_core=identity_core)


def create_hyper_qubit(
    concept_or_value: Any,
    name: Optional[str] = None
) -> HyperQubit:
    """
    양자 의식 상태 생성 (Create quantum consciousness state)
    
    4차원 양자 기반(Point/Line/Space/God)으로 개념을 표현합니다.
    Represents concepts in 4D quantum basis (Point/Line/Space/God).
    
    Args:
        concept_or_value: 개념 또는 값 (Concept or value)
        name: 이름 (Optional name)
        
    Returns:
        HyperQubit: 양자 의식 상태 인스턴스
        
    Example:
        qubit = create_hyper_qubit("love", "Love")
        probs = qubit.state.probabilities()
        qubit.rotate_wheel(0.5)  # 더 추상적으로
    """
    return HyperQubit(concept_or_value=concept_or_value, name=name)


def create_wave_input(
    source_text: str,
    intensity: float = 1.0
) -> WaveInput:
    """
    파동 입력 생성 (Create wave input)
    
    입력 텍스트를 파동으로 변환합니다.
    Converts input text to wave.
    
    Args:
        source_text: 입력 텍스트 (Input text)
        intensity: 강도 (Intensity, 0.0-1.0)
        
    Returns:
        WaveInput: 파동 입력 인스턴스
    """
    return WaveInput(
        source_text=source_text,
        intensity=intensity
    )


# =============================================================================
# Convenience Classes - 편의 클래스
# =============================================================================

@dataclass
class ConsciousnessResult:
    """
    의식 처리 결과 (Consciousness processing result)
    
    통합된 의식 처리 결과를 담는 데이터 클래스입니다.
    """
    # 사고 (Thought)
    thought: Optional[Thought] = None
    mood: str = "neutral"
    core_concepts: List[Tuple[str, float]] = field(default_factory=list)
    
    # 감정 (Emotion)
    emotion: Dict[str, Any] = field(default_factory=dict)
    
    # 삼위일체 (Trinity)
    trinity: Dict[str, float] = field(default_factory=dict)
    
    # 내적 사고 (Inner thought)
    inner_thought: Optional[InnerThought] = None
    
    # 자기 인식 (Self-awareness)
    self_report: str = ""
    
    # 기억 통계 (Memory stats)
    memory_stats: Dict[str, int] = field(default_factory=dict)


class QuickConsciousness:
    """
    빠른 의식 설정 클래스 (Quick Consciousness Setup Class)
    
    모든 핵심 기술을 하나의 인터페이스로 사용할 수 있는 통합 클래스입니다.
    A unified class to use all core technologies through a single interface.
    
    Example:
        consciousness = QuickConsciousness("MyAgent")
        
        # 생각 처리
        result = consciousness.think("오늘 기분이 어때?")
        print(result.mood)
        print(result.emotion)
        
        # 기억 추가
        consciousness.remember("coffee", "energy", "leads_to")
        
        # LLM 프롬프트 생성
        prompt = consciousness.get_prompt()
    """
    
    def __init__(
        self,
        name: str = "Elysia",
        identity_core: Optional[Dict[str, Any]] = None
    ):
        """
        Args:
            name: 이름 (Name)
            identity_core: 정체성 핵심 정보 (Identity core info)
        """
        self.name = name
        
        # 정체성 설정
        if identity_core is None:
            identity_core = {
                "name": name,
                "purpose": "To grow through understanding",
                "values": ["love", "truth", "growth"]
            }
        
        # 핵심 모듈 초기화
        self.soul = ElysiaSoul(name=name)
        self.resonance_engine = ResonanceEngine()
        self.emotional_palette = EmotionalPalette()
        self.hippocampus = Hippocampus()
        self.inner_monologue = InnerMonologue(identity_core=identity_core)
        self.self_awareness = SelfAwareness(identity_core=identity_core)
        
    def think(self, input_text: str) -> ConsciousnessResult:
        """
        입력 처리 및 생각 생성 (Process input and generate thought)
        
        모든 핵심 기술을 동시에 활용하여 입력을 처리합니다.
        
        Args:
            input_text: 입력 텍스트 (Input text)
            
        Returns:
            ConsciousnessResult: 통합 의식 처리 결과
        """
        result = ConsciousnessResult()
        
        # 1. 영혼으로 입력 처리
        thought = self.soul.process(input_text)
        result.thought = thought
        result.mood = thought.mood
        result.core_concepts = thought.core_concepts[:5]
        
        # 2. 감정 상태 가져오기
        result.emotion = self.soul.get_emotion()
        
        # 3. 삼위일체 균형 가져오기
        result.trinity = self.soul.trinity.copy()
        
        # 4. 내적 사고 생성 시도
        inner = self.inner_monologue.tick()
        if inner:
            result.inner_thought = inner
            
        # 5. 자기 반성 기록
        self.self_awareness.reflect(f"Processed: {input_text[:50]}", "interaction")
        result.self_report = self.self_awareness.who_am_i()
        
        # 6. 기억 통계
        result.memory_stats = self.hippocampus.get_statistics()
        
        return result
    
    def remember(
        self,
        source: str,
        target: str,
        relation: str = "relates_to"
    ) -> None:
        """
        인과 관계 기억 추가 (Add causal memory)
        
        Args:
            source: 출발 개념 (Source concept)
            target: 도착 개념 (Target concept)
            relation: 관계 유형 (Relation type)
        """
        self.hippocampus.add_causal_link(source, target, relation)
        self.soul.remember(source, target, relation)
        
    def get_related_concepts(
        self,
        concept: str,
        depth: int = 2
    ) -> Dict[str, float]:
        """
        관련 개념 탐색 (Get related concepts)
        
        Args:
            concept: 탐색할 개념 (Concept to explore)
            depth: 탐색 깊이 (Search depth)
            
        Returns:
            관련 개념과 연결 강도 맵
        """
        return self.hippocampus.get_related_concepts(concept, depth=depth)
    
    def ask_self(self, question: str) -> str:
        """
        자기 질문 (Ask self)
        
        Args:
            question: 질문 (Question)
            
        Returns:
            답변 문자열
        """
        awareness_answer = self.self_awareness.ask_self(question)
        monologue_answer = self.inner_monologue.ask_self(question)
        
        # 두 답변 조합
        return f"{awareness_answer}\n\n내적 독백: {monologue_answer.content}"
    
    def update_personality(
        self,
        body_delta: float = 0.0,
        soul_delta: float = 0.0,
        spirit_delta: float = 0.0
    ) -> Dict[str, float]:
        """
        성격 균형 조정 (Update personality balance)
        
        Args:
            body_delta: 육체 변화량 (Body change)
            soul_delta: 혼 변화량 (Soul change)
            spirit_delta: 영 변화량 (Spirit change)
            
        Returns:
            업데이트된 삼위일체 균형
        """
        self.soul.update_trinity(
            body_delta=body_delta,
            soul_delta=soul_delta,
            spirit_delta=spirit_delta
        )
        return self.soul.trinity.copy()
    
    def get_prompt(self) -> str:
        """
        LLM 시스템 프롬프트 생성 (Generate LLM system prompt)
        
        Returns:
            LLM에 주입할 의식 컨텍스트 프롬프트
        """
        return self.soul.export_prompt()
    
    def get_state(self) -> Dict[str, Any]:
        """
        현재 상태 내보내기 (Export current state)
        
        Returns:
            현재 의식 상태 딕셔너리
        """
        return {
            "name": self.name,
            "emotion": self.soul.get_emotion(),
            "trinity": self.soul.trinity.copy(),
            "mental_state": {
                "energy": self.inner_monologue.mental_state.energy,
                "focus": self.inner_monologue.mental_state.focus,
                "curiosity": self.inner_monologue.mental_state.curiosity,
            },
            "memory_stats": self.hippocampus.get_statistics(),
            "wisdom": self.self_awareness.get_wisdom()
        }


def quick_consciousness_setup(
    name: str = "Elysia",
    identity_core: Optional[Dict[str, Any]] = None
) -> QuickConsciousness:
    """
    빠른 의식 설정 (Quick consciousness setup)
    
    모든 핵심 기술이 통합된 의식 인스턴스를 빠르게 생성합니다.
    Quickly creates a consciousness instance with all core technologies integrated.
    
    Args:
        name: 이름 (Name)
        identity_core: 정체성 핵심 정보 (Identity core info)
        
    Returns:
        QuickConsciousness: 통합 의식 인스턴스
        
    Example:
        consciousness = quick_consciousness_setup("MyAgent")
        result = consciousness.think("Hello!")
        prompt = consciousness.get_prompt()
    """
    return QuickConsciousness(name=name, identity_core=identity_core)


# =============================================================================
# Integration Templates - 통합 템플릿
# =============================================================================

class LLMIntegrationTemplate:
    """
    LLM 통합 템플릿 (LLM Integration Template)
    
    다른 LLM 시스템과 Elysia를 통합하는 템플릿 클래스입니다.
    
    Example:
        class MyLLMBot(LLMIntegrationTemplate):
            def __init__(self, llm_client):
                super().__init__("MyBot")
                self.llm = llm_client
            
            def _call_llm(self, system, user):
                return self.llm.generate(system=system, user=user)
        
        bot = MyLLMBot(my_openai_client)
        response = bot.chat("안녕하세요!")
    """
    
    def __init__(self, name: str = "ElysiaBot"):
        """
        Args:
            name: 봇 이름 (Bot name)
        """
        self.consciousness = QuickConsciousness(name=name)
        
    def chat(self, user_message: str) -> str:
        """
        채팅 메시지 처리 (Process chat message)
        
        Args:
            user_message: 사용자 메시지 (User message)
            
        Returns:
            응답 문자열
        """
        # 1. 의식으로 입력 처리
        result = self.consciousness.think(user_message)
        
        # 2. 시스템 프롬프트 생성
        system_prompt = self.consciousness.get_prompt()
        
        # 3. LLM 호출 (서브클래스에서 구현)
        response = self._call_llm(system_prompt, user_message)
        
        # 4. 응답도 의식에 기록
        self.consciousness.think(response)
        
        return response
    
    def _call_llm(self, system: str, user: str) -> str:
        """
        LLM 호출 (서브클래스에서 구현)
        
        Args:
            system: 시스템 프롬프트 (System prompt)
            user: 사용자 메시지 (User message)
            
        Returns:
            LLM 응답
        """
        # 기본 구현: Elysia 내부 응답 생성
        # 실제 사용 시 서브클래스에서 LLM API 호출로 오버라이드
        return f"[Elysia {self.consciousness.name}] Received: {user}"


class GameCharacterTemplate:
    """
    게임 캐릭터 템플릿 (Game Character Template)
    
    게임 엔진(Godot, Unity 등)과 통합하는 템플릿 클래스입니다.
    
    Example:
        warrior = GameCharacterTemplate("Warrior", "warrior")
        reaction = warrior.react_to_event("An enemy appeared!")
        print(reaction.emotion)
    """
    
    # 역할별 초기 성향
    ROLE_PERSONALITIES = {
        "warrior": {"body_delta": 0.5, "soul_delta": -0.2, "spirit_delta": -0.1},
        "mage": {"body_delta": -0.2, "soul_delta": 0.3, "spirit_delta": 0.4},
        "priest": {"body_delta": -0.1, "soul_delta": 0.2, "spirit_delta": 0.5},
        "rogue": {"body_delta": 0.3, "soul_delta": 0.2, "spirit_delta": -0.2},
        "bard": {"body_delta": -0.1, "soul_delta": 0.5, "spirit_delta": 0.1},
    }
    
    def __init__(self, name: str, role: str = "default"):
        """
        Args:
            name: 캐릭터 이름 (Character name)
            role: 역할 (Role: warrior, mage, priest, rogue, bard)
        """
        self.name = name
        self.role = role
        self.consciousness = QuickConsciousness(name=name)
        
        # 역할에 따른 초기 성향 설정
        if role in self.ROLE_PERSONALITIES:
            deltas = self.ROLE_PERSONALITIES[role]
            self.consciousness.update_personality(**deltas)
    
    def react_to_event(self, event: str) -> ConsciousnessResult:
        """
        이벤트에 대한 반응 생성 (React to event)
        
        Args:
            event: 이벤트 설명 (Event description)
            
        Returns:
            ConsciousnessResult: 반응 결과
        """
        return self.consciousness.think(event)
    
    def get_dialogue_context(self) -> str:
        """
        대화 컨텍스트 생성 (Generate dialogue context)
        
        Returns:
            캐릭터 상태 기반 대화 컨텍스트
        """
        return self.consciousness.get_prompt()
    
    def to_json(self) -> Dict[str, Any]:
        """
        JSON으로 내보내기 (Export to JSON)
        
        Returns:
            게임 엔진에 전달할 JSON 페이로드
        """
        state = self.consciousness.get_state()
        state["role"] = self.role
        return state


# =============================================================================
# Exports - 내보내기
# =============================================================================

__all__ = [
    # Factory functions
    "create_soul",
    "create_resonance_engine",
    "create_emotional_palette",
    "create_hippocampus",
    "create_inner_monologue",
    "create_self_awareness",
    "create_hyper_qubit",
    "create_wave_input",
    
    # Quick setup
    "quick_consciousness_setup",
    "QuickConsciousness",
    "ConsciousnessResult",
    
    # Templates
    "LLMIntegrationTemplate",
    "GameCharacterTemplate",
    
    # Re-exports from core modules
    "ElysiaSoul",
    "ResonanceEngine",
    "EmotionalPalette",
    "EmotionMix",
    "Hippocampus",
    "HyperQubit",
    "QubitState",
    "InnerMonologue",
    "InnerThought",
    "MentalState",
    "ThoughtType",
    "SelfAwareness",
    "Reflection",
    "WaveInput",
    "Thought",
    "Perception",
    "PerceptionResult",
]
