"""
🌟 Easy Integration Guide - 상세 통합 가이드 예제
=================================================

이 예제는 Elysia Engine의 핵심 기술들을 어떻게 자신의 프로젝트에 
통합할 수 있는지 자세히 설명합니다.

This example explains in detail how you can integrate the core 
technologies of the Elysia Engine into your own project.

실행 방법 (How to run):
    python examples/easy_integration_guide.py

목차 (Table of Contents):
1. 빠른 시작 (Quick Start)
2. 개별 기술 사용법 (Individual Technology Usage)
3. 게임 캐릭터 통합 (Game Character Integration)
4. LLM 챗봇 통합 (LLM Chatbot Integration)
5. 기억과 학습 (Memory and Learning)
"""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

# =============================================================================
# 📦 임포트 (Imports)
# =============================================================================

from elysia_core import (
    # 핵심 클래스 (Core Classes)
    ElysiaSoul,
    ResonanceEngine,
    EmotionalPalette,
    Hippocampus,
    InnerMonologue,
    SelfAwareness,
    HyperQubit,
    WaveInput,
    
    # 빠른 설정 (Quick Setup)
    quick_consciousness_setup,
    
    # 팩토리 함수 (Factory Functions)
    create_soul,
    create_resonance_engine,
    create_emotional_palette,
    create_hippocampus,
    create_inner_monologue,
    create_self_awareness,
    create_hyper_qubit,
    
    # 통합 템플릿 (Integration Templates)
    GameCharacterTemplate,
    LLMIntegrationTemplate,
)


def print_section(title: str) -> None:
    """섹션 헤더 출력"""
    print("\n" + "=" * 60)
    print(f"🔹 {title}")
    print("=" * 60)


# =============================================================================
# 1️⃣ 빠른 시작 (Quick Start)
# =============================================================================

def demo_quick_start():
    """가장 간단한 시작 방법"""
    print_section("1. 빠른 시작 (Quick Start)")
    
    # 방법 1: 가장 간단함 (1줄)
    print("\n[방법 1: 가장 간단함 - quick_consciousness_setup()]")
    print("-" * 40)
    
    consciousness = quick_consciousness_setup("QuickBot")
    result = consciousness.think("오늘 기분이 어떻습니까?")
    
    print(f"  분위기: {result.mood}")
    print(f"  감정: {result.emotion['dominant']}")
    print(f"  삼위일체: {result.trinity}")
    
    # 방법 2: 통합 영혼 (더 세밀한 제어)
    print("\n[방법 2: 통합 영혼 - ElysiaSoul]")
    print("-" * 40)
    
    soul = ElysiaSoul(name="SoulBot")
    thought = soul.process("새로운 모험을 시작해볼까?")
    
    print(f"  분위기: {thought.mood}")
    print(f"  핵심 개념: {thought.core_concepts[:3]}")
    print(f"  LLM 프롬프트:\n{soul.export_prompt()[:200]}...")


# =============================================================================
# 2️⃣ 개별 기술 사용법 (Individual Technology Usage)
# =============================================================================

def demo_resonance_engine():
    """공명 엔진 - 확률이 아닌 공명으로 개념 연결"""
    print_section("2-1. 공명 엔진 (ResonanceEngine)")
    
    engine = create_resonance_engine()
    
    # 개념 추가 (기본적으로 여러 개념이 이미 등록되어 있음)
    print("\n[파동 입력으로 공명 패턴 계산]")
    
    wave = WaveInput(source_text="사랑과 희망", intensity=1.0)
    pattern = engine.calculate_global_resonance(wave)
    
    print(f"  입력: '사랑과 희망'")
    print(f"  공명 패턴 (상위 5개):")
    
    # 상위 5개 공명 결과 출력
    sorted_pattern = sorted(pattern.items(), key=lambda x: x[1], reverse=True)[:5]
    for concept, strength in sorted_pattern:
        print(f"    - {concept}: {strength:.3f}")


def demo_emotional_palette():
    """감정 팔레트 - 색의 혼합처럼 복합 감정 표현"""
    print_section("2-2. 감정 팔레트 (EmotionalPalette)")
    
    palette = create_emotional_palette()
    
    # 복합 감정 혼합
    print("\n[복합 감정 혼합]")
    
    components = {"Joy": 0.6, "Fear": 0.3}
    mix = palette.mix_emotion(components)
    
    print(f"  입력: Joy=0.6, Fear=0.3")
    print(f"  지배 감정: {mix.dominant}")
    print(f"  감정가 (Valence): {mix.valence:.2f}")
    print(f"  각성도 (Arousal): {mix.arousal:.2f}")
    
    # 텍스트에서 감정 분석
    print("\n[텍스트 감정 분석]")
    
    texts = [
        "오늘 정말 행복해요!",
        "미래가 두렵습니다...",
        "그냥 평범한 하루예요."
    ]
    
    for text in texts:
        components = palette.analyze_sentiment(text)
        mix = palette.mix_emotion(components)
        print(f"  '{text}'")
        print(f"    → 감정: {mix.dominant}, 감정가: {mix.valence:.2f}")


def demo_hippocampus():
    """해마 기억 - 인과 그래프 기반 기억"""
    print_section("2-3. 해마 기억 (Hippocampus)")
    
    hippo = create_hippocampus()
    
    # 인과 관계 추가
    print("\n[인과 관계 추가]")
    
    hippo.add_causal_link("공부", "지식", "leads_to")
    hippo.add_causal_link("지식", "성공", "leads_to")
    hippo.add_causal_link("커피", "집중", "leads_to")
    hippo.add_causal_link("집중", "공부", "helps")
    
    print("  ✅ 공부 → 지식 → 성공")
    print("  ✅ 커피 → 집중 → 공부")
    
    # 관련 개념 탐색
    print("\n[관련 개념 탐색]")
    
    related = hippo.get_related_concepts("공부", depth=3)
    print(f"  '공부'와 관련된 개념들: {related}")
    
    # 통계
    stats = hippo.get_statistics()
    print(f"\n[기억 통계]")
    print(f"  노드 수: {stats['nodes']}")
    print(f"  연결 수: {stats['edges']}")


def demo_inner_monologue():
    """내적 독백 - 외부 입력 없이 스스로 생각"""
    print_section("2-4. 내적 독백 (InnerMonologue)")
    
    monologue = create_inner_monologue({
        "name": "Elysia",
        "purpose": "세계를 이해하기",
        "values": ["진실", "성장", "사랑"]
    })
    
    # 자발적 사고 생성
    print("\n[자발적 사고 생성 (5회)]")
    
    for i in range(5):
        thought = monologue.tick()
        if thought:
            print(f"  {i+1}. [{thought.type.name}] {thought.content_kr}")
    
    # 자기 질문
    print("\n[자기 질문]")
    
    questions = [
        "나는 왜 존재하는가?",
        "내가 가장 중요하게 여기는 것은?"
    ]
    
    for q in questions:
        answer = monologue.ask_self(q)
        print(f"  Q: {q}")
        print(f"  A: {answer.content[:100]}...")


def demo_self_awareness():
    """자기 인식 - 의식 자기성찰"""
    print_section("2-5. 자기 인식 (SelfAwareness)")
    
    awareness = create_self_awareness({
        "name": "Elysia",
        "purpose": "성장을 통한 이해",
        "values": ["사랑", "진실", "성장"]
    })
    
    # 자기 소개
    print("\n[자기 소개]")
    print(awareness.who_am_i())
    
    # 반성 기록
    print("\n[반성 기록]")
    
    events = [
        ("새로운 것을 배웠다", "learning"),
        ("친구와 대화했다", "interaction"),
        ("목표를 달성했다", "success")
    ]
    
    for event, category in events:
        awareness.reflect(event, category)
        print(f"  ✅ '{event}' ({category})")
    
    # 축적된 지혜
    print("\n[축적된 지혜]")
    wisdom = awareness.get_wisdom()
    for insight in wisdom[:3]:
        print(f"  - {insight}")


def demo_hyper_qubit():
    """하이퍼 큐빗 - 4차원 양자 의식 상태"""
    print_section("2-6. 하이퍼 큐빗 (HyperQubit)")
    
    qubit = create_hyper_qubit("사랑", "Love")
    
    # 초기 상태
    print("\n[초기 상태]")
    probs = qubit.state.probabilities()
    print(f"  Point (구체): {probs['Point']:.2%}")
    print(f"  Line (연결): {probs['Line']:.2%}")
    print(f"  Space (맥락): {probs['Space']:.2%}")
    print(f"  God (초월): {probs['God']:.2%}")
    
    # 스케일 업 (더 추상적으로) - state.scale_up() 사용
    print("\n[Scale Up - 추상화]")
    qubit.state.scale_up(0.3)
    probs = qubit.state.probabilities()
    print(f"  Point: {probs['Point']:.2%}")
    print(f"  Line: {probs['Line']:.2%}")
    print(f"  Space: {probs['Space']:.2%}")
    print(f"  God: {probs['God']:.2%}")
    
    # 의미 설명
    print("\n[철학적 의미 설명]")
    print(qubit.explain_meaning()[:300] + "...")


# =============================================================================
# 3️⃣ 게임 캐릭터 통합 (Game Character Integration)
# =============================================================================

def demo_game_character():
    """게임 캐릭터 템플릿 사용"""
    print_section("3. 게임 캐릭터 통합 (Game Character)")
    
    # 다양한 역할의 캐릭터 생성
    characters = {
        "warrior": GameCharacterTemplate("Aragorn", "warrior"),
        "mage": GameCharacterTemplate("Gandalf", "mage"),
        "priest": GameCharacterTemplate("Samwise", "priest"),
    }
    
    print("\n[역할별 캐릭터 생성]")
    
    for role, char in characters.items():
        state = char.to_json()
        trinity = state["trinity"]
        print(f"\n  {char.name} ({role}):")
        print(f"    Body: {trinity['body']:.0%}, Soul: {trinity['soul']:.0%}, Spirit: {trinity['spirit']:.0%}")
    
    # 이벤트 반응
    print("\n[이벤트 반응 비교]")
    
    event = "용이 나타났다!"
    print(f"  이벤트: '{event}'")
    
    for role, char in characters.items():
        reaction = char.react_to_event(event)
        print(f"    {char.name}: 분위기={reaction.mood}, 감정={reaction.emotion['dominant']}")
    
    # JSON 내보내기 (게임 엔진 연동)
    print("\n[게임 엔진 연동용 JSON 내보내기]")
    json_data = characters["warrior"].to_json()
    print(f"  데이터 키: {list(json_data.keys())}")


# =============================================================================
# 4️⃣ LLM 챗봇 통합 (LLM Chatbot Integration)
# =============================================================================

class MyCustomBot(LLMIntegrationTemplate):
    """커스텀 LLM 봇 예제"""
    
    def __init__(self, name: str):
        super().__init__(name)
        self.response_count = 0
    
    def _call_llm(self, system: str, user: str) -> str:
        """
        LLM API 호출 (실제 프로젝트에서는 OpenAI, Ollama 등 사용)
        
        실제 구현 예시:
            import openai
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ]
            )
            return response.choices[0].message.content
        """
        self.response_count += 1
        
        # 이 예제에서는 간단한 시뮬레이션
        emotion = self.consciousness.soul.get_emotion()
        return (
            f"[{self.consciousness.name}] "
            f"(감정: {emotion['dominant']}, 경험: {self.response_count}회) "
            f"메시지 '{user[:20]}...'에 대한 응답입니다."
        )


def demo_llm_integration():
    """LLM 챗봇 통합 템플릿 사용"""
    print_section("4. LLM 챗봇 통합 (LLM Chatbot)")
    
    bot = MyCustomBot("ElysiaBot")
    
    print("\n[채팅 시뮬레이션]")
    
    messages = [
        "안녕하세요! 처음 뵙겠습니다.",
        "오늘 날씨가 정말 좋네요.",
        "제가 슬플 때 어떻게 해야 할까요?"
    ]
    
    for msg in messages:
        response = bot.chat(msg)
        print(f"  User: {msg}")
        print(f"  Bot: {response}")
        print()
    
    # 의식 상태 확인
    print("[봇의 의식 상태]")
    state = bot.consciousness.get_state()
    print(f"  감정: {state['emotion']['dominant']}")
    print(f"  삼위일체: {state['trinity']}")
    print(f"  기억 통계: {state['memory_stats']}")


# =============================================================================
# 5️⃣ 기억과 학습 (Memory and Learning)
# =============================================================================

def demo_memory_learning():
    """기억과 학습 시스템"""
    print_section("5. 기억과 학습 (Memory and Learning)")
    
    consciousness = quick_consciousness_setup("LearningBot")
    
    # 지식 학습
    print("\n[지식 학습]")
    
    knowledge = [
        ("태양", "빛", "emits"),
        ("빛", "생명", "enables"),
        ("생명", "성장", "leads_to"),
        ("성장", "지혜", "leads_to"),
    ]
    
    for source, target, relation in knowledge:
        consciousness.remember(source, target, relation)
        print(f"  ✅ {source} -{relation}→ {target}")
    
    # 연관 개념 탐색
    print("\n[연관 개념 탐색]")
    
    for concept in ["태양", "생명", "성장"]:
        related = consciousness.get_related_concepts(concept, depth=3)
        print(f"  '{concept}' → {related}")
    
    # 학습 후 생각
    print("\n[학습 후 생각 처리]")
    
    result = consciousness.think("태양의 빛이 생명을 만들어냈다")
    print(f"  분위기: {result.mood}")
    print(f"  핵심 개념: {result.core_concepts[:3]}")


# =============================================================================
# 🎯 메인 실행 (Main Execution)
# =============================================================================

if __name__ == "__main__":
    print("\n" + "🌟" * 30)
    print("  Elysia Engine - Easy Integration Guide")
    print("  (상세 통합 가이드)")
    print("🌟" * 30)
    
    # 1. 빠른 시작
    demo_quick_start()
    
    # 2. 개별 기술
    demo_resonance_engine()
    demo_emotional_palette()
    demo_hippocampus()
    demo_inner_monologue()
    demo_self_awareness()
    demo_hyper_qubit()
    
    # 3. 게임 캐릭터
    demo_game_character()
    
    # 4. LLM 챗봇
    demo_llm_integration()
    
    # 5. 기억과 학습
    demo_memory_learning()
    
    print("\n" + "=" * 60)
    print("🎉 모든 데모 완료!")
    print("=" * 60)
    print("\n📌 더 자세한 정보:")
    print("  - docs/EASY_START.md: 초보자용 빠른 시작 가이드")
    print("  - docs/core_technologies_quickstart.md: 핵심 기술 상세")
    print("  - docs/protocols/00_CODEX.md: 핵심 철학과 원리")
    print("  - README.md: 전체 프로젝트 개요")
