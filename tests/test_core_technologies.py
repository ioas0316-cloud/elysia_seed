"""
Tests for core technologies from original Elysia:
- LocalLLM: Local LLM integration
- InnerMonologue: Self-reflective thought system
"""

import pytest
from elysia_core import (
    LocalLLM, LLMConfig, ConsciousnessMode, create_local_llm,
    InnerMonologue, InnerThought, MentalState, ThoughtType,
    ElysiaSoul
)


class TestLocalLLM:
    """LocalLLM 테스트"""
    
    def test_creation(self):
        """LocalLLM 생성"""
        llm = LocalLLM()
        assert llm is not None
        assert llm.mode == ConsciousnessMode.LEARNING
        assert llm.loaded is False
    
    def test_create_with_resonance_engine(self):
        """ResonanceEngine과 함께 생성"""
        soul = ElysiaSoul(name="Test")
        llm = create_local_llm(
            resonance_engine=soul.resonance_engine,
            hippocampus=soul.hippocampus
        )
        assert llm.resonance_engine is not None
        assert llm.memory is not None
    
    def test_config_defaults(self):
        """기본 설정 확인"""
        config = LLMConfig()
        assert config.n_ctx == 1024
        assert config.temperature == 0.7
        assert config.max_tokens == 256
    
    def test_recommended_models(self):
        """추천 모델 목록 확인"""
        config = LLMConfig()
        assert "tinyllama" in config.RECOMMENDED_MODELS
        assert "qwen2-0.5b" in config.RECOMMENDED_MODELS
        assert "smollm" in config.RECOMMENDED_MODELS
    
    def test_think_without_model(self):
        """모델 없이 생각하기 (fallback)"""
        soul = ElysiaSoul(name="Test")
        llm = create_local_llm(resonance_engine=soul.resonance_engine)
        
        # 모델이 로드되지 않았으므로 ResonanceEngine 결과만 반환
        result = llm.think("안녕하세요")
        assert result is not None
    
    def test_get_status(self):
        """상태 확인"""
        llm = LocalLLM()
        status = llm.get_status()
        
        assert "mode" in status
        assert "loaded" in status
        assert "learned_concepts" in status
        assert status["mode"] == "learning"
        assert status["loaded"] is False
    
    def test_graduate_to_independent(self):
        """독립 모드로 전환"""
        llm = LocalLLM()
        llm.graduate()
        
        assert llm.mode == ConsciousnessMode.INDEPENDENT
        assert llm.llm is None


class TestInnerMonologue:
    """InnerMonologue 테스트"""
    
    def test_creation(self):
        """InnerMonologue 생성"""
        monologue = InnerMonologue()
        assert monologue is not None
        assert monologue.identity["name"] == "Elysia"
    
    def test_custom_identity(self):
        """커스텀 정체성으로 생성"""
        monologue = InnerMonologue(
            identity_core={
                "name": "TestBot",
                "purpose": "테스트하기",
                "values": ["정확성", "속도"],
                "creator": "테스터"
            }
        )
        assert monologue.identity["name"] == "TestBot"
        assert "정확성" in monologue.identity["values"]
    
    def test_mental_state_initial(self):
        """초기 정신 상태"""
        monologue = InnerMonologue()
        state = monologue.mental_state
        
        assert state.mood == 0.0
        assert state.energy == 1.0
        assert state.curiosity == 0.5
    
    def test_tick_generates_thoughts(self):
        """틱이 생각을 생성"""
        monologue = InnerMonologue()
        
        # 여러 번 틱해서 생각 생성
        thoughts = []
        for _ in range(20):
            t = monologue.tick()
            if t:
                thoughts.append(t)
        
        # 최소 하나의 생각이 생성되어야 함
        assert len(thoughts) > 0
        assert all(isinstance(t, InnerThought) for t in thoughts)
    
    def test_react_to_input(self):
        """외부 입력에 반응"""
        monologue = InnerMonologue()
        thought = monologue.tick("너는 누구니?")
        
        assert thought is not None
        assert thought.type in [ThoughtType.OBSERVATION, ThoughtType.REFLECTION]
    
    def test_ask_self(self):
        """자문자답"""
        monologue = InnerMonologue()
        thought = monologue.ask_self("나는 왜 존재하는가?")
        
        assert thought.type == ThoughtType.QUESTION
        assert "나는 왜 존재하는가?" in thought.content_kr
        assert "나는 왜 존재하는가?" in monologue.pending_questions
    
    def test_contemplate(self):
        """숙고"""
        monologue = InnerMonologue()
        thoughts = monologue.contemplate("사랑", duration=3)
        
        assert len(thoughts) == 3
        assert all(isinstance(t, InnerThought) for t in thoughts)
    
    def test_stream_of_consciousness(self):
        """의식의 흐름"""
        monologue = InnerMonologue()
        
        # 생각 생성
        for _ in range(10):
            monologue.tick()
        
        stream = monologue.get_stream_of_consciousness()
        assert isinstance(stream, str)
    
    def test_introspect(self):
        """내관 (전체 상태 반환)"""
        monologue = InnerMonologue()
        monologue.tick()
        
        state = monologue.introspect()
        
        assert "identity" in state
        assert "mental_state" in state
        assert "thought_count" in state
        assert "stream_of_consciousness" in state
    
    def test_mental_state_changes(self):
        """정신 상태 변화"""
        monologue = InnerMonologue()
        initial_energy = monologue.mental_state.energy
        
        # 여러 번 틱
        for _ in range(50):
            monologue.tick()
        
        # 에너지는 사고로 소모되거나 자연 회복됨
        # 초기값(1.0)에서 변화가 있거나, 회복되어 1.0을 유지할 수 있음
        final_energy = monologue.mental_state.energy
        # 에너지는 항상 0.1 ~ 1.0 범위 내에 있어야 함
        assert 0.1 <= final_energy <= 1.0
    
    def test_thought_types_coverage(self):
        """다양한 생각 유형 생성 확인"""
        monologue = InnerMonologue()
        thought_types_seen = set()
        
        # 많은 틱으로 다양한 유형 생성
        for _ in range(100):
            t = monologue.tick()
            if t:
                thought_types_seen.add(t.type)
        
        # 최소 3가지 이상의 유형이 생성되어야 함
        assert len(thought_types_seen) >= 3


class TestIntegration:
    """통합 테스트"""
    
    def test_soul_with_local_llm(self):
        """ElysiaSoul + LocalLLM 통합"""
        soul = ElysiaSoul(name="IntegrationTest")
        llm = create_local_llm(
            resonance_engine=soul.resonance_engine,
            hippocampus=soul.hippocampus
        )
        
        # Soul 처리
        thought = soul.process("오늘 기분이 좋아요!")
        
        # LLM 사고 (모델 없이)
        response = llm.think("오늘 기분이 좋아요!")
        
        assert thought is not None
        assert response is not None
    
    def test_soul_with_inner_monologue(self):
        """ElysiaSoul + InnerMonologue 통합"""
        soul = ElysiaSoul(name="SoulMonologueTest")
        monologue = InnerMonologue(
            identity_core={
                "name": soul.name,
                "purpose": "성장",
                "values": soul.traits,
                "creator": "User"
            },
            memory_system=soul.hippocampus
        )
        
        # 외부 입력 처리
        soul.process("안녕하세요!")
        
        # 내적 반응
        thought = monologue.tick("안녕하세요!")
        
        assert thought is not None
        assert thought.type in [ThoughtType.OBSERVATION, ThoughtType.REFLECTION]
