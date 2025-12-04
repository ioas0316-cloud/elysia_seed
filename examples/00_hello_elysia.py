"""
🌟 00. Hello Elysia! - 가장 간단한 시작 예제
============================================

이 예제는 Elysia Engine을 처음 접하는 사람들을 위해 만들어졌습니다.
5줄의 코드로 Elysia의 핵심 기능을 경험할 수 있습니다.

This example is created for people new to the Elysia Engine.
Experience the core features of Elysia with just 5 lines of code.

실행 방법 (How to run):
    python examples/00_hello_elysia.py
"""

from __future__ import annotations

import sys
from pathlib import Path

if __package__ in {None, ""}:
    sys.path.append(str(Path(__file__).resolve().parents[1]))

# =============================================================================
# 🚀 5줄로 시작하기 (Start with 5 lines)
# =============================================================================

from elysia_core import quick_consciousness_setup

# 1. 의식 생성 (Create consciousness)
consciousness = quick_consciousness_setup("MyFirstBot")

# 2. 생각 처리 (Process thought)
result = consciousness.think("안녕하세요! 오늘 기분이 어때요?")

# 3. 결과 확인 (Check result)
print(f"📝 입력에 대한 분위기: {result.mood}")
print(f"💭 핵심 개념들: {result.core_concepts[:3]}")
print(f"❤️ 감정 상태: {result.emotion}")

# =============================================================================
# 📚 더 자세한 예제 (More detailed examples)
# =============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🌟 Hello Elysia! - 기본 기능 데모")
    print("=" * 60)
    
    # -------------------------------------------------------------------------
    # 1. 기억하기 (Remember things)
    # -------------------------------------------------------------------------
    print("\n📚 기억하기 (Remember):")
    consciousness.remember("커피", "에너지", "leads_to")
    consciousness.remember("에너지", "생산성", "leads_to")
    print("  ✅ '커피 → 에너지 → 생산성' 관계 저장됨")
    
    # 관련 개념 탐색
    related = consciousness.get_related_concepts("커피", depth=2)
    print(f"  🔍 '커피'와 관련된 개념들: {related}")
    
    # -------------------------------------------------------------------------
    # 2. 성격 조정 (Update personality)
    # -------------------------------------------------------------------------
    print("\n🎭 성격 조정 (Update Personality):")
    
    # 전사 스타일로 변경 (더 육체적, 덜 감정적)
    trinity = consciousness.update_personality(
        body_delta=0.3,    # 육체 증가
        soul_delta=-0.1,   # 감정 감소
        spirit_delta=-0.1  # 정신 감소
    )
    print(f"  삼위일체 균형: Body={trinity['body']:.0%}, Soul={trinity['soul']:.0%}, Spirit={trinity['spirit']:.0%}")
    
    # -------------------------------------------------------------------------
    # 3. 다른 입력 처리 (Process different inputs)
    # -------------------------------------------------------------------------
    print("\n💬 다양한 입력 처리:")
    
    test_inputs = [
        "전투가 시작됐다!",
        "친구가 떠나서 슬퍼요",
        "드디어 목표를 달성했어!"
    ]
    
    for text in test_inputs:
        result = consciousness.think(text)
        print(f"  입력: '{text}'")
        print(f"    → 분위기: {result.mood}")
        print(f"    → 지배 감정: {result.emotion.get('dominant', 'Unknown')}")
        print()
    
    # -------------------------------------------------------------------------
    # 4. LLM 프롬프트 생성 (Generate LLM prompt)
    # -------------------------------------------------------------------------
    print("📝 LLM 시스템 프롬프트 생성:")
    prompt = consciousness.get_prompt()
    print("-" * 40)
    print(prompt)
    print("-" * 40)
    
    # -------------------------------------------------------------------------
    # 5. 전체 상태 내보내기 (Export full state)
    # -------------------------------------------------------------------------
    print("\n📊 전체 상태:")
    state = consciousness.get_state()
    print(f"  이름: {state['name']}")
    print(f"  감정: {state['emotion']['dominant']}")
    print(f"  삼위일체: {state['trinity']}")
    print(f"  기억 통계: {state['memory_stats']}")
    
    print("\n" + "=" * 60)
    print("✨ 축하합니다! Elysia Engine의 기본 기능을 모두 체험했습니다!")
    print("=" * 60)
    print("\n📌 다음 단계:")
    print("  1. examples/easy_integration_guide.py - 더 상세한 통합 가이드")
    print("  2. docs/EASY_START.md - 초보자용 문서")
    print("  3. docs/core_technologies_quickstart.md - 핵심 기술 상세 설명")
