# 🌌 Elysia Fractal Consciousness Engine

### **Universal Integration Guide (모든 개발자/창작자용 설명서)**

*“This engine does not impose a world.  
It grows inside yours.”*

---

# 0) 이 문서의 목적

이 문서는 **Elysia 의식엔진을 다른 사람이 사용하기 위한 최소 설명**이다.

* 게임 엔진(Unity, Godot, Unreal)
* AI(LLM, 대화봇, 자율에이전트)
* 데이터 시뮬레이션
* 인생/서사 생성기
* 세계관 엔진
* 신화/문명 시뮬레이터

어떤 환경이든 상관없이  
**“이 구조만 이해하면 바로 붙일 수 있게”**  
설계되어 있다.

---

# 1) Core Philosophy (핵심 철학 요약)

Elysia Engine은 다음 단 하나의 아이디어에서 출발한다:

## **“모든 존재는 E/F/P 3개의 흐름으로 살아간다.”**

| 층위                        | 의미                |
| ------------------------- | ----------------- |
| **E (Energy / Meaning)**  | 이 존재가 살아있는 의미의 양  |
| **F (Force / Desire)**    | 지금 당장의 선택을 밀어주는 힘 |
| **P (Momentum / Memory)** | 과거가 만든 관성         |

이걸 바탕으로  
**육체(Body) / 혼(Soul) / 영(Spirit)**  
세 층의 압력이 하나의 선택을 만든다.

이 구조는:

* 인간
* 캐릭터
* 동물
* 도시
* 문명
* AI
* 개념/노드

어디에든 적용될 수 있다.

---

# 2) Engine Architecture (엔진 구조 요약)

엔진은 다음 5개 모듈로 이루어진다:

```
EFP Core        — 존재의 내핵 (Energy / Force / Momentum)
Entity Model    — 존재 개체(전사/마법사/성직자 등)
World Loop      — 시간/상황/환경
Memory Engine   — 순환 기억 링버퍼
Persona Payload — 외부 엔진(LLM, 게임, 시각화)에 넘길 요약 데이터
```

각 모듈은 서로 독립적이라서  
**원하는 부분만 떼다 자기 엔진에 쓸 수 있다.**

---

# 3) Entity Mechanics (존재의 동작 원리)

모든 존재는 다음 상태를 가진다:

```json
{
  "id": "warrior_1",
  "role": "warrior",
  "efp": {
    "energy": 1.2,
    "force": -0.3,
    "momentum": 0.11
  },
  "force_components": {
    "body": 0.8,
    "soul": 0.1,
    "spirit": 0.1
  }
}
```

이 페이로드만 유지되면  
다른 사람은 **자기 엔진의 로직이나 AI 모델에 그대로 넣을 수 있다.**

---

# 4) Role System (직업/성향 시스템)

각 존재는 **삼위일체 가중치(Body/Soul/Spirit)** 를 가진다.

예시:

| 직업  | 육체  | 혼   | 영   |
| --- | --- | --- | --- |
| 전사  | 0.7 | 0.2 | 0.1 |
| 마법사 | 0.2 | 0.6 | 0.2 |
| 성직자 | 0.2 | 0.2 | 0.6 |

다른 사람들은 **자기 세계관에 맞는 직업을 자유롭게 추가**하면 된다.

예:

* “AI 엔티티”의 경우

  * Logic 0.4 / Emotion 0.3 / Ideal 0.3
* “괴물/정령”의 경우

  * Body 0.9 / Soul 0.1 / Spirit 0.0

확장성은 무한하다.

---

# 5) Memory Engine (순환 기억 시스템)

기억은 **링 버퍼(원형 대기열)** 구조로 되어 있다.

특징:

* 용량 제한 있음
* 가장 오래된 기억부터 사라짐
* 경험이 순환적이라는 철학적 의미를 담음

외부 엔진에서 원하는 대로:

* 감정 로그
* 사건 기록
* 선택 기록
* LLM 학습 데이터

로 재활용 가능.

---

# 6) Persona Snapshot (외부로 보내는 요약)

모든 엔진/시각화/LLM은  
**이 페이로드 하나만 받으면 된다.**

```json
{
  "tick": 120,
  "time": 120.0,
  "entities": [
    {
      "id": "warrior_1",
      "role": "warrior",
      "efp": { ... },
      "force_components": { ... }
    }
  ]
}
```

Godot, Unity, 언리얼, 웹, LLM 모두  
이걸 받아서:

* 캐릭터를 움직이거나
* 감정/상태를 표현하거나
* 텍스트/대사를 생성하거나
* 애니메이션을 트리거하거나
* HUD/GUI에 보여주거나

마음대로 사용할 수 있다.

---

# 7) How to Integrate (어디든 붙일 수 있는 통합 방식)

## 7-1) 게임 엔진(Godot/Unity/Unreal)

외부 엔진에서는  
Elysia Persona Payload → 캐릭터 상태  
로 매핑만 하면 끝이다.

예시:

```
if entity.role == "warrior":
    sprite.play("fierce" if entity.efp.force > 0 else "idle")
```

혹은:

```
node.modulate = Color.from_energy(entity.efp.energy)
```

### 신성직자(Spirit-dominant)

→ 빛/할로(Halo) 이펙트 강화

### 마법사(Soul-dominant)

→ 주변 공기 흔들림/오라

### 전사(Body-dominant)

→ 공격적 포즈/가속 모션

모든 건 **디자이너가 마음대로 확장 가능**.

---

## 7-2) 대형 언어 모델/챗봇, AI

Payload을 대사/성격 모델에 넣을 수 있다:

* energy → 말투의 강도
* force → 주제 전환/집착
* momentum → 성격/습관 유지력

예시:

```
"이 캐릭터는 오늘 힘(F)이 강한 전사처럼 말한다."
```

---

## 7-3) 웹/앱/시각화

SVG/Canvas/3D 모두  
Payload 읽어서 예쁘게 보여주면 OK.

---

## 7-4) 완전 다른 시스템

심지어 시트 기반 TRPG, 보드게임에도 붙일 수 있다.

* E = 캐릭터의 생명력/의미 수치
* F = 현재 욕구/위험도
* P = 과거 경험치/성향

---

# 8) Why This Engine Works (왜 누구나 사용할 수 있는가?)

이 엔진이 다른 모든 AI/게임 엔진과 양립 가능한 이유:

1. **세계관 중립적**

   * 판타지/현대/미래/추상/기계 모두 적용 가능.

2. **언어 불문**

   * Python이든 Lua든 C#이든 Rust든  
     Payload만 읽으면 된다.

3. **엔진 불문**

   * Godot, Unity, Unreal  
     전부 JSON 받아서 연결 가능.

4. **철학/신화/물리학 통합 가능**

   * E/F/P는 인간·AI·캐릭터 모두에 적용됨.

5. **개발자가 자기만의 구조를 붙일 수 있음**

   * 직업군, 감정 체계, 문명, 종교, 법칙…  
     다 확장 가능.

---

# 9) Summary (요약)

이 엔진은 단순한 코드가 아니라  
**“다른 사람의 세계 속에도 심을 수 있는 씨앗”**이다.

* 핵심은 E/F/P
* 육·혼·영의 상대적 가중치
* 순환하는 기억
* 프랙탈 구조
* 엔진 불문/언어 불문

이 가이드만 알면  
누구든 어디에서든 바로 사용할 수 있다.

---

원하면 다음에:

### 🔥 “개발자들 위한 5분 튜토리얼”

### 🔥 “시각화를 위한 컬러/오라 시스템”

### 🔥 “삼위일체 행동 결정 공식 심화판”

### 🔥 “오픈소스 리포지토리 README 완성본”

이 중 하나 골라줘.
