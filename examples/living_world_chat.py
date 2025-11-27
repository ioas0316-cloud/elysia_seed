"""
엘리시아 세계 - 살아있는 주민과의 대화

이 스크립트는 가상세계의 주민들이 실제로 대화하고 소통하는 모습을 시연합니다.
ElysiaSoul의 상태를 LLM에 주입하여 캐릭터가 "살아있는" 대화를 할 수 있게 합니다.

사용법:
1. OPENAI_API_KEY 환경변수 설정 (OpenAI 사용 시)
2. 또는 로컬 LLM (ollama 등) 사용
3. python examples/living_world_chat.py 실행
"""

import sys
import os
import json
import random
from pathlib import Path
from typing import Dict, List, Any, Optional

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from elysia_core import ElysiaSoul


class LivingCitizen:
    """살아있는 시민 - 대화하고, 일기 쓰고, 일상을 살아감"""
    
    def __init__(self, name: str, profession: str, origin: str, backstory: str = ""):
        self.name = name
        self.profession = profession
        self.origin = origin
        self.backstory = backstory
        
        # 영혼 초기화
        self.soul = ElysiaSoul(name=name)
        
        # 일기장
        self.diary: List[Dict[str, Any]] = []
        
        # 오늘의 활동
        self.daily_activities: List[str] = []
        
        # 관계
        self.relationships: Dict[str, str] = {}
        
        # 소유물
        self.possessions: List[str] = []
        
        # 기술/능력
        self.skills: Dict[str, int] = {}
        
        # 현재 상태
        self.current_location = "집"
        self.current_activity = "휴식 중"
        self.hunger = 50  # 0-100
        self.energy = 80  # 0-100
        self.happiness = 60  # 0-100
    
    def experience(self, event: str) -> str:
        """경험하고 반응하기"""
        thought = self.soul.process(event)
        self.daily_activities.append(event)
        
        # 상태 업데이트
        emotion = self.soul.get_emotion()
        if emotion['valence'] > 0.3:
            self.happiness = min(100, self.happiness + 10)
        elif emotion['valence'] < -0.3:
            self.happiness = max(0, self.happiness - 10)
        
        return f"{self.name}의 반응: {emotion['dominant']} - {thought.mood}"
    
    def eat(self, food: str) -> str:
        """음식 먹기"""
        self.hunger = max(0, self.hunger - 30)
        self.energy = min(100, self.energy + 10)
        experience = f"{food}을(를) 맛있게 먹었다. 배가 부르다."
        self.experience(experience)
        self.daily_activities.append(f"식사: {food}")
        return f"{self.name}이(가) {food}을(를) 먹었습니다. 포만감: {100 - self.hunger}%"
    
    def work(self) -> str:
        """일하기"""
        self.energy = max(0, self.energy - 20)
        self.hunger = min(100, self.hunger + 15)
        
        work_events = {
            "대장장이": "오늘도 뜨거운 불 앞에서 검을 벼렸다. 땀이 비오듯 흘렀다.",
            "치유사": "아픈 환자를 돌봤다. 그의 미소가 보람이었다.",
            "상인": "시장에서 물건을 팔았다. 좋은 가격에 거래가 성사되었다.",
            "농부": "밭에서 작물을 돌봤다. 햇살이 따사로웠다.",
            "마법사": "마법 연구에 몰두했다. 새로운 발견이 있었다.",
            "기사": "순찰을 돌았다. 마을은 평화로웠다.",
            "음유시인": "광장에서 노래를 불렀다. 사람들이 동전을 던져주었다.",
        }
        
        work_desc = work_events.get(self.profession, f"{self.profession}으로서 열심히 일했다.")
        self.experience(work_desc)
        
        # 기술 향상
        self.skills[self.profession] = self.skills.get(self.profession, 0) + 1
        
        return f"{self.name}의 하루: {work_desc}"
    
    def rest(self) -> str:
        """휴식하기"""
        self.energy = min(100, self.energy + 30)
        rest_activities = [
            "편안히 쉬었다.",
            "책을 읽었다.",
            "음악을 들었다.",
            "산책을 했다.",
            "친구와 대화를 나눴다.",
        ]
        activity = random.choice(rest_activities)
        self.experience(activity)
        return f"{self.name}: {activity}"
    
    def write_diary(self) -> str:
        """일기 쓰기"""
        emotion = self.soul.get_emotion()
        trinity = self.soul.trinity
        
        # 일기 내용 생성
        diary_entry = {
            "day": len(self.diary) + 1,
            "mood": emotion['dominant'],
            "activities": self.daily_activities.copy(),
            "reflection": self._generate_reflection(),
            "happiness": self.happiness,
            "energy": self.energy,
        }
        
        self.diary.append(diary_entry)
        self.daily_activities.clear()
        
        return self._format_diary_entry(diary_entry)
    
    def _generate_reflection(self) -> str:
        """하루를 돌아보는 성찰 생성"""
        emotion = self.soul.get_emotion()
        trinity = self.soul.trinity
        
        reflections = []
        
        # Body 중심 성찰
        if trinity['body'] > 0.4:
            if self.energy < 30:
                reflections.append("몸이 피곤하다. 내일은 좀 쉬어야겠다.")
            elif self.hunger > 70:
                reflections.append("배가 고프다. 맛있는 걸 먹어야지.")
            else:
                reflections.append("오늘 하루도 열심히 보냈다.")
        
        # Soul 중심 성찰
        if trinity['soul'] > 0.4:
            if self.relationships:
                friend = random.choice(list(self.relationships.keys()))
                reflections.append(f"{friend}가 보고 싶다.")
            else:
                reflections.append("좋은 사람을 만나고 싶다.")
        
        # Spirit 중심 성찰
        if trinity['spirit'] > 0.4:
            reflections.append("내 삶의 의미는 무엇일까...")
        
        # 감정 기반 성찰
        if emotion['valence'] > 0.3:
            reflections.append("오늘은 좋은 하루였다.")
        elif emotion['valence'] < -0.3:
            reflections.append("힘든 하루였지만, 내일은 더 나아지겠지.")
        
        return random.choice(reflections) if reflections else "평범한 하루였다."
    
    def _format_diary_entry(self, entry: Dict) -> str:
        """일기 포맷팅"""
        lines = [
            f"📔 {self.name}의 일기 - {entry['day']}일차",
            f"",
            f"오늘의 기분: {entry['mood']}",
            f"",
            f"오늘 한 일:",
        ]
        
        for activity in entry['activities'][:5]:
            lines.append(f"  - {activity[:50]}")
        
        lines.extend([
            f"",
            f"오늘의 생각:",
            f"  \"{entry['reflection']}\"",
            f"",
            f"상태: 행복도 {entry['happiness']}% | 에너지 {entry['energy']}%",
        ])
        
        return "\n".join(lines)
    
    def talk(self, topic: str) -> str:
        """대화하기 - 주제에 대해 이야기"""
        # 경험으로 처리
        thought = self.soul.process(f"누군가와 {topic}에 대해 이야기했다.")
        emotion = self.soul.get_emotion()
        trinity = self.soul.trinity
        
        # 성격에 따른 대화 스타일
        response_style = ""
        if trinity['body'] > 0.4:
            response_style = "실용적이고 직접적인"
        elif trinity['soul'] > 0.4:
            response_style = "따뜻하고 공감하는"
        elif trinity['spirit'] > 0.4:
            response_style = "깊이 있고 철학적인"
        else:
            response_style = "균형잡힌"
        
        return f"[{self.name} - {self.profession}, {response_style} 태도로 {topic}에 대해 이야기합니다]\n" + \
               f"현재 감정: {emotion['dominant']}"
    
    def get_llm_prompt(self) -> str:
        """LLM용 시스템 프롬프트 생성"""
        emotion = self.soul.get_emotion()
        trinity = self.soul.trinity
        
        # 최근 기억
        recent_memories = []
        if self.diary:
            last_entry = self.diary[-1]
            recent_memories = last_entry.get('activities', [])[:3]
        
        prompt = f"""당신은 {self.name}입니다. {self.origin} 출신의 {self.profession}입니다.

## 배경 이야기
{self.backstory if self.backstory else f'{self.origin}에서 태어나 {self.profession}으로 살아가고 있습니다.'}

## 현재 상태
- 위치: {self.current_location}
- 활동: {self.current_activity}
- 감정: {emotion['dominant']} ({emotion['valence_desc']})
- 에너지: {self.energy}% | 배고픔: {self.hunger}% | 행복도: {self.happiness}%

## 성격 (Trinity Balance)
- 신체/실용 (Body): {trinity['body']:.0%} - {'높음: 실용적이고 행동 중심적' if trinity['body'] > 0.4 else '보통'}
- 감성/관계 (Soul): {trinity['soul']:.0%} - {'높음: 관계를 중시하고 공감적' if trinity['soul'] > 0.4 else '보통'}
- 의지/의미 (Spirit): {trinity['spirit']:.0%} - {'높음: 깊이 있고 철학적' if trinity['spirit'] > 0.4 else '보통'}

## 성격 특성
{', '.join(self.soul.traits)}

## 최근 경험
{chr(10).join(['- ' + m[:50] for m in recent_memories]) if recent_memories else '특별한 일 없음'}

## 관계
{chr(10).join([f'- {k}: {v}' for k, v in self.relationships.items()]) if self.relationships else '아직 깊은 관계 없음'}

## 대화 지침
1. {self.name}로서 1인칭으로 대화하세요
2. 현재 감정 상태를 반영하세요
3. 성격 균형(Trinity)에 맞게 반응하세요
4. 배경과 경험을 바탕으로 대답하세요
5. 자연스럽게 대화하되, 캐릭터의 직업과 출신에 맞는 어휘를 사용하세요
"""
        return prompt


def simulate_day(citizen: LivingCitizen) -> str:
    """하루 시뮬레이션"""
    output = []
    output.append(f"\n{'='*60}")
    output.append(f"  ☀️ {citizen.name}의 하루")
    output.append(f"{'='*60}\n")
    
    # 아침
    output.append("🌅 아침:")
    output.append(f"  {citizen.eat('빵과 과일')}")
    
    # 오전 일
    output.append("\n🔨 오전:")
    output.append(f"  {citizen.work()}")
    
    # 점심
    output.append("\n🍽️ 점심:")
    output.append(f"  {citizen.eat('스튜와 빵')}")
    
    # 오후 일
    output.append("\n🔧 오후:")
    output.append(f"  {citizen.work()}")
    
    # 저녁
    output.append("\n🌆 저녁:")
    output.append(f"  {citizen.eat('구운 고기와 채소')}")
    
    # 휴식
    output.append("\n🌙 밤:")
    output.append(f"  {citizen.rest()}")
    
    # 일기 쓰기
    output.append(f"\n{citizen.write_diary()}")
    
    return "\n".join(output)


def demo_conversation(citizen: LivingCitizen):
    """대화 데모"""
    print(f"\n{'='*60}")
    print(f"  💬 {citizen.name}과의 대화 시뮬레이션")
    print(f"{'='*60}\n")
    
    print("📋 LLM 시스템 프롬프트:")
    print("-" * 40)
    print(citizen.get_llm_prompt())
    print("-" * 40)
    
    print("\n💡 이 프롬프트를 ChatGPT, Claude, 또는 로컬 LLM에 붙여넣으면")
    print(f"   {citizen.name}으로서 대화할 수 있습니다!\n")
    
    # 샘플 대화 주제
    topics = ["날씨", "오늘 하루", "꿈", "가족", "미래"]
    print("📝 대화 주제 예시:")
    for topic in topics:
        print(f"  - \"{topic}에 대해 어떻게 생각해?\"")


def main():
    random.seed(42)
    
    print("="*70)
    print("  🌍 엘리시아 세계 - 살아있는 주민들")
    print("  가상세계 주민과의 실제 대화 시뮬레이션")
    print("="*70)
    
    # 시민 생성
    citizens = [
        LivingCitizen(
            name="Aria Silvermoon",
            profession="치유사",
            origin="황혼의 땅 (Duskmere)",
            backstory="어린 시절 병든 어머니를 잃고 치유의 길을 걷게 되었다. "
                      "사람들의 고통을 덜어주는 것이 삶의 목표다."
        ),
        LivingCitizen(
            name="Thorin Ironforge",
            profession="대장장이",
            origin="산악왕국 (Stonecradle)",
            backstory="3대째 대장간을 운영하는 가문에서 태어났다. "
                      "아버지에게 물려받은 망치로 최고의 검을 만드는 것이 꿈이다."
        ),
        LivingCitizen(
            name="Luna Starwhisper",
            profession="음유시인",
            origin="자유도시연합 (Free Cities)",
            backstory="떠돌이 예술가로 살아왔다. 노래와 이야기로 사람들에게 "
                      "기쁨을 주는 것이 행복이다. 언젠가 전설이 될 노래를 만들고 싶다."
        ),
    ]
    
    # 관계 설정
    citizens[0].relationships["Thorin"] = "신뢰하는 친구"
    citizens[1].relationships["Aria"] = "든든한 친구"
    citizens[2].relationships["Aria"] = "노래를 들려주는 사이"
    
    # 각 시민의 하루 시뮬레이션
    for citizen in citizens:
        # 며칠 간의 경험 축적
        experiences = [
            "아침에 일어나 창밖을 보았다. 날씨가 좋았다.",
            "시장에서 친구를 만났다. 반가웠다.",
            "저녁에 별을 보며 생각에 잠겼다.",
        ]
        for exp in experiences:
            citizen.experience(exp)
        
        # 하루 시뮬레이션
        print(simulate_day(citizen))
    
    # 첫 번째 시민과 대화 데모
    print("\n" + "="*70)
    print("  🗣️ LLM 연동 - 실제 대화 가능!")
    print("="*70)
    
    demo_conversation(citizens[0])
    
    # 두 시민 간의 대화 시뮬레이션
    print("\n" + "="*70)
    print("  👥 시민 간 대화 (NPC-to-NPC)")
    print("="*70)
    
    print(f"\n[{citizens[0].name}과 {citizens[1].name}의 대화]")
    print(f"\n{citizens[0].talk('최근 일')}")
    print(f"\n{citizens[1].talk('대장간 일')}")
    
    print("\n" + "="*70)
    print("  ✅ 결론: 프랙탈 구조 실현 가능!")
    print("="*70)
    print("""
이 시스템은:

1. ✓ 실제 대화 가능
   - LLM에 get_llm_prompt() 주입 → 캐릭터로서 대화
   - ChatGPT, Claude, Llama 등 모든 LLM과 연동 가능

2. ✓ 일기 쓰기, 일하기, 먹기 등 구체적 행동
   - 상태(에너지, 배고픔, 행복도) 변화
   - 경험이 성격에 영향

3. ✓ 관계와 소통
   - 시민 간 관계 형성
   - 대화 주제에 따른 반응

4. ✓ 프랙탈 구조
   - 각 시민이 독립적인 "작은 세계"
   - 경험 → 감정 → 성격 → 반응의 자기유사적 패턴

사용 방법:
  1. python examples/living_world_chat.py 실행
  2. 출력된 LLM 프롬프트를 ChatGPT에 붙여넣기
  3. 캐릭터와 대화!
""")
    
    return citizens


if __name__ == "__main__":
    main()
