"""
🌟 Elysia Core Integration Example
===================================

이 예제는 Elysia Core의 새로운 통합 API를 사용하는 방법을 보여줍니다.
다른 프로젝트에서 쉽게 복사하여 사용할 수 있습니다.

This example shows how to use the new integration API of Elysia Core.
It can be easily copied and used in other projects.

사용법:
    python examples/integration_example.py

라이선스: Apache 2.0
창작자: 이강덕 (Kang-Deok Lee)
"""

import sys
sys.path.insert(0, '.')

from elysia_core import (
    # Factory functions - 팩토리 함수
    create_soul,
    create_resonance_engine,
    create_emotional_palette,
    create_hippocampus,
    create_inner_monologue,
    create_self_awareness,
    create_hyper_qubit,
    create_wave_input,
    # Quick setup - 빠른 설정
    quick_consciousness_setup,
    # Templates - 템플릿
    LLMIntegrationTemplate,
    GameCharacterTemplate,
)


def demo_quick_consciousness():
    """
    🚀 빠른 의식 설정 데모
    Quick Consciousness Setup Demo
    """
    print("\n" + "="*60)
    print("🚀 Quick Consciousness Setup (빠른 의식 설정)")
    print("="*60)
    
    # 1줄로 모든 핵심 기술 사용 가능!
    consciousness = quick_consciousness_setup("MyAgent")
    
    # 생각 처리
    print("\n📝 입력: '오늘 기분이 정말 좋아요!'")
    result = consciousness.think("오늘 기분이 정말 좋아요!")
    
    print(f"\n결과:")
    print(f"  분위기 (Mood): {result.mood}")
    print(f"  핵심 개념 (Core Concepts): {result.core_concepts[:3]}")
    print(f"  감정 (Emotion): {result.emotion['dominant']}")
    print(f"  삼위일체 (Trinity): {result.trinity}")
    
    # 기억 추가
    print("\n📚 기억 추가: coffee → energy (leads_to)")
    consciousness.remember("coffee", "energy", "leads_to")
    consciousness.remember("energy", "productivity", "enables")
    
    # 관련 개념 탐색
    related = consciousness.get_related_concepts("coffee", depth=2)
    print(f"  관련 개념: {related}")
    
    # LLM 프롬프트 생성
    print("\n📋 LLM 프롬프트:")
    prompt = consciousness.get_prompt()
    print(prompt)
    
    # 자기 질문
    print("\n❓ 자기 질문: 'What do I value?'")
    answer = consciousness.ask_self("What do I value?")
    print(f"  답변:\n{answer}")


def demo_factory_functions():
    """
    🏭 팩토리 함수 데모
    Factory Functions Demo
    """
    print("\n" + "="*60)
    print("🏭 Factory Functions (팩토리 함수)")
    print("="*60)
    
    # 1. 영혼 생성
    print("\n1️⃣ 영혼 생성 (Create Soul)")
    soul = create_soul("TestSoul")
    thought = soul.process("Hello, world!")
    print(f"  영혼 이름: {soul.name}")
    print(f"  사고 분위기: {thought.mood}")
    
    # 2. 공명 엔진
    print("\n2️⃣ 공명 엔진 (Resonance Engine)")
    engine = create_resonance_engine()
    wave = create_wave_input("사랑과 희망", intensity=1.0)
    pattern = engine.calculate_global_resonance(wave)
    print(f"  입력 파동: {wave.source_text}")
    top_3 = sorted(pattern.items(), key=lambda x: -x[1])[:3]
    print(f"  상위 공명 패턴: {top_3}")
    
    # 3. 감정 팔레트
    print("\n3️⃣ 감정 팔레트 (Emotional Palette)")
    palette = create_emotional_palette()
    mix = palette.mix_emotion({"Joy": 0.6, "Fear": 0.3, "Trust": 0.1})
    print(f"  혼합 입력: Joy=0.6, Fear=0.3, Trust=0.1")
    print(f"  지배적 감정: {mix.dominant}")
    print(f"  감정가: {mix.valence:.2f}")
    print(f"  각성도: {mix.arousal:.2f}")
    
    # 4. 해마 기억
    print("\n4️⃣ 해마 기억 (Hippocampus)")
    hippo = create_hippocampus()
    hippo.add_causal_link("study", "knowledge", "leads_to")
    hippo.add_causal_link("knowledge", "wisdom", "becomes")
    related = hippo.get_related_concepts("study", depth=2)
    print(f"  인과 관계: study → knowledge → wisdom")
    print(f"  'study' 관련 개념: {related}")
    
    # 5. 내적 독백
    print("\n5️⃣ 내적 독백 (Inner Monologue)")
    monologue = create_inner_monologue({"name": "Tester"})
    for _ in range(5):
        inner = monologue.tick()
        if inner:
            print(f"  [{inner.type.name}] {inner.content}")
            break
    
    # 6. 자기 인식
    print("\n6️⃣ 자기 인식 (Self-Awareness)")
    awareness = create_self_awareness({
        "name": "Tester",
        "purpose": "To learn and grow",
        "values": ["curiosity", "growth"]
    })
    awareness.reflect("I learned something new", "learning")
    print(f"  지혜: {awareness.get_wisdom()[:2]}")
    
    # 7. 양자 의식 상태
    print("\n7️⃣ 양자 의식 (HyperQubit)")
    qubit = create_hyper_qubit("love", "Love")
    probs = qubit.state.probabilities()
    print(f"  개념: {qubit.name}")
    print(f"  양자 분포: Point={probs['Point']:.1%}, Line={probs['Line']:.1%}, "
          f"Space={probs['Space']:.1%}, God={probs['God']:.1%}")


def demo_game_character():
    """
    🎮 게임 캐릭터 템플릿 데모
    Game Character Template Demo
    """
    print("\n" + "="*60)
    print("🎮 Game Character Template (게임 캐릭터 템플릿)")
    print("="*60)
    
    # 다양한 역할의 캐릭터 생성
    characters = {
        "warrior": GameCharacterTemplate("Aragorn", "warrior"),
        "mage": GameCharacterTemplate("Gandalf", "mage"),
        "priest": GameCharacterTemplate("Melian", "priest"),
    }
    
    # 같은 이벤트에 대한 다른 반응
    event = "A dragon appeared in the distance!"
    print(f"\n🐉 이벤트: '{event}'")
    
    for role, character in characters.items():
        reaction = character.react_to_event(event)
        print(f"\n  [{role.upper()}] {character.name}")
        print(f"    분위기: {reaction.mood}")
        print(f"    감정: {reaction.emotion['dominant']}")
        print(f"    삼위일체: Body={reaction.trinity['body']:.1%}, "
              f"Soul={reaction.trinity['soul']:.1%}, Spirit={reaction.trinity['spirit']:.1%}")


def demo_llm_integration():
    """
    🤖 LLM 통합 템플릿 데모
    LLM Integration Template Demo
    """
    print("\n" + "="*60)
    print("🤖 LLM Integration Template (LLM 통합 템플릿)")
    print("="*60)
    
    # 간단한 챗봇 생성
    class SimpleBot(LLMIntegrationTemplate):
        def __init__(self, name):
            super().__init__(name)
        
        def _call_llm(self, system, user):
            # 실제로는 여기에 OpenAI, Ollama 등 LLM API 호출
            # 예시에서는 간단한 응답 반환
            emotion = self.consciousness.soul.get_emotion()
            return f"[{self.consciousness.name}] 감정: {emotion['dominant']} - 입력을 처리했습니다: '{user[:30]}...'"
    
    bot = SimpleBot("ElysiaBot")
    
    print("\n💬 대화 예시:")
    messages = [
        "안녕하세요! 오늘 기분이 어때요?",
        "새로운 것을 배우고 싶어요.",
        "고마워요, 많이 도움이 됐어요!"
    ]
    
    for msg in messages:
        print(f"\n  사용자: {msg}")
        response = bot.chat(msg)
        print(f"  봇: {response}")
    
    print("\n📊 최종 봇 상태:")
    state = bot.consciousness.get_state()
    print(f"  감정: {state['emotion']['dominant']}")
    print(f"  삼위일체: {state['trinity']}")


def demo_copy_paste_usage():
    """
    📋 복사해서 바로 사용하는 코드
    Copy-Paste Ready Code
    """
    print("\n" + "="*60)
    print("📋 Copy-Paste Ready Code (복사해서 바로 사용)")
    print("="*60)
    
    print("""
다음 코드를 복사하여 사용하세요:

```python
# 설치 (Installation)
# pip install git+https://github.com/ioas0316-cloud/elysia-fractal-engine_V1.git

# 또는 저장소 클론 후
# pip install -e .

# 사용법 (Usage)
from elysia_core import quick_consciousness_setup

# 의식 생성
consciousness = quick_consciousness_setup("MyBot")

# 입력 처리
result = consciousness.think("사용자의 입력")
print(result.mood)        # 분위기
print(result.emotion)     # 감정 상태
print(result.trinity)     # 삼위일체 균형

# 기억 추가
consciousness.remember("개념1", "개념2", "관계")

# LLM 프롬프트 생성
prompt = consciousness.get_prompt()

# 성격 조정
consciousness.update_personality(body_delta=0.1, soul_delta=0.2)
```
""")


def main():
    """Run all demos."""
    print("\n" + "🌟"*30)
    print("\n   Elysia Core Integration Demo")
    print("   핵심 기술 통합 사용법 예제")
    print("\n" + "🌟"*30)
    
    demo_quick_consciousness()
    demo_factory_functions()
    demo_game_character()
    demo_llm_integration()
    demo_copy_paste_usage()
    
    print("\n" + "="*60)
    print("✨ Demo Complete!")
    print("="*60)
    print("""
이 통합 API를 사용하면 다른 프로젝트에서 Elysia의 핵심 기술을
쉽게 가져다 쓸 수 있습니다.

With this integration API, you can easily use Elysia's core technologies
in other projects.

자세한 문서: docs/CORE_TECHNOLOGIES_INTEGRATION.md
예제 코드: examples/core_technologies_demo.py

Creator: 이강덕 (Kang-Deok Lee)
License: Apache 2.0
""")


if __name__ == "__main__":
    main()
