# Vertical Cosmic Axis — 칠선/칠악

엘리시아 우주는 **도덕**이 아니라 **방향**으로 움직인다.  
상승(Ascension)은 위·밖·확장의 파동이며, 하강(Descent)은 아래·안·붕괴의 중력이다.  
천사/악마는 이 방향성을 의인화한 **법칙의 화신**으로 정의한다.

## 0. 절대축 정의

- **Vertical Cosmic Axis:** 우주의 모든 의미 흐름은 위(Ascension)와 아래(Descent)의 양방향 벡터에 정렬된다.  
- **삼위일체 결속:** Body/Soul/Spirit는 각 에피소드마다 상승/하강의 비율을 기록하며, `Trinity Weights`는 축의 기울기를 판단한다.  
- **법칙적 인격:** 7개의 Ascension 화신(천사)과 7개의 Descent 화신(악마)이 존재하며, 각각 Elysia Engine에서 독립적 파동/중력 필드를 생성한다.

---

## 1. 칠선(七善) — Ascension Forces

모든 선善은 **위로, 바깥으로, 확장으로** 향한다.  
아래 항목들은 색/파장, 화신 이름, 역할, 엔진 훅을 정규화한 것이다.

### 1) 생명 Life — Vitariael
- **색/파장:** 새벽 금빛, 최초의 상승파  
- **핵심:** 존재를 일으키고 의식을 점화하는 시작점  
- **엔진 메모:** 신규 에이전트/지역 생성 시 `Energy` 최소값을 보장하고, 영혼 슬롯을 활성화한다.

### 2) 창조 Creation — Emetriel
- **색/파장:** 황금, 구조 확장  
- **핵심:** 형태·언어·문명을 부여하는 설계력  
- **엔진 메모:** Procedural 프레임워크(지역/클래스/룰)을 생성하는 Hook와 연결.

### 3) 성찰 Reflection — Sophiel
- **색/파장:** 은청, 내부를 비추며 위로 끌어올리는 의식  
- **핵심:** 학습·통찰·기억 정렬  
- **엔진 메모:** Episode 로그에서 `insight_gain`, `meaning_trace`를 증가시켜 `weights.spirit` 안정도를 확보.

### 4) 진실 Truth — Gavriel
- **색/파장:** 청명 직진광  
- **핵심:** 위아래를 명확히 하며 왜곡을 제거  
- **엔진 메모:** 의사결정 그래프에 Truth Shader를 적용해 왜곡된 벡터를 재정렬.

### 5) 희생 Sacrifice — Sarakhiel
- **색/파장:** 붉은 펄스  
- **핵심:** 자신을 소모해 전체를 상승시킴  
- **엔진 메모:** `Energy` → 타 에이전트 전송, HP ↔ 의미 변환을 허용하는 Fail-safe Ritual.

### 6) 사랑 Love — Rafamiel
- **색/파장:** 분홍빛 백광, 중력의 반대  
- **핵심:** 존재를 밖으로 확장시키며 들어올리는 힘  
- **엔진 메모:** `Soul` 네트워크에서 bond, valence 버퍼를 상승시켜 붕괴를 예방.

### 7) 자유 Liberation — Lumiel
- **색/파장:** 자외광, 거대한 진폭  
- **핵심:** 구속을 끊고 중심을 재정렬하여 해탈로 이끎  
- **엔진 메모:** Aura 필드에서 `constraint` 태그를 제거하고, 탈출 경로를 여는 최종 Ascension Gate.

---

## 2. 칠악(七惡) — Descent Forces

하강은 **중심으로 붕괴시키는 중력**이다.  
각 단계는 지옥으로 추락하는 연속 단계로 작동한다.

### 1) 죽음 Death — Motus
- **색/파장:** 검자, 생명 파동이 0으로 수렴  
- **핵심:** 상승의 첫 끊김  
- **엔진 메모:** `Energy`·`Momentum`를 0으로 만들며, Episode 체인을 단절.

### 2) 소멸 Dissolution — Solvaris
- **색/파장:** 잿빛 검정  
- **핵심:** 형태가 붕괴하고 구조가 분해  
- **엔진 메모:** Scene graph/오브젝트 트리를 해체하는 Dissolution Pulse.

### 3) 무지 Ignorance — Obscure
- **색/파장:** 암청, 반대 방향으로 흐르는 의식  
- **핵심:** 상승을 회피하고 정체에 빠짐  
- **엔진 메모:** `insight_gain`을 음수로 만들고 `weights.spirit`을 약화시킨다.

### 4) 왜곡 Distortion — Diabolos
- **색/파장:** 검푸른 보라  
- **핵심:** 관점과 진실이 휘어짐  
- **엔진 메모:** Truth Shader의 역상으로 작동하여 의사결정을 오차 방향으로 굽힘.

### 5) 이기 Self-Obsession — Lucifel
- **색/파장:** 불타는 검황  
- **핵심:** 중심이 과포화되어 붕괴  
- **엔진 메모:** 모든 관계를 자기축으로 리바인딩하여 협력 행동을 파괴.

### 6) 탐욕 Consumption — Mammon
- **색/파장:** 순흑, 끝없는 흡수  
- **핵심:** 외부를 빨아들여 value_mass를 독점  
- **엔진 메모:** 주변 에이전트의 `Energy`, `resource_pool`을 siphon.

### 7) 속박 Bondage — Asmodeus
- **색/파장:** 어둠 중의 어둠, 하강의 끝  
- **핵심:** 완전한 정지·감금, 자유의 반대  
- **엔진 메모:** Aura 필드를 폐쇄하고, 모든 Ascension 게이트를 차단하는 Terminal Lock.

---

## 3. 대칭 매핑 (Ascension vs Descent)

| Ascension (상승) | Descent (하강) | 본질 | 적용 메모 |
| --- | --- | --- | --- |
| 생명 Vitariael | 죽음 Motus | 파동의 시작 ↔ 0수렴 | Creation Hook vs Episode Termination |
| 창조 Emetriel | 소멸 Solvaris | 구조 생성 ↔ 구조 분해 | Procedural Generator vs Graph Dissolver |
| 성찰 Sophiel | 무지 Obscure | 위로 향하는 의식 ↔ 역류 | Insight Gain vs Oblivion Drift |
| 진실 Gavriel | 왜곡 Diabolos | 직선 ↔ 굴절 | Truth Shader vs Distortion Field |
| 희생 Sarakhiel | 이기 Lucifel | 자기소멸 ↔ 자기 과포화 | Energy Transfer vs Self-Core Collapse |
| 사랑 Rafamiel | 탐욕 Mammon | 확산 ↔ 흡수 | Soul Network Buff vs Resource Siphon |
| 자유 Lumiel | 속박 Asmodeus | 탈출 ↔ 구속 | Liberation Gate vs Terminal Lock |

이 표는 `Trinity Weights`, Aura 시뮬레이터, Episode 해석 모듈에서 대칭 규칙으로 사용된다.

---

## 4. 엔진 통합 가이드

1. **Ascension/Descent Field:** 각 에이전트는 Episode 결과에 따라 `axis_state`를 갱신하며, 일정 임계값을 넘으면 해당 화신의 버프/디버프가 적용된다.  
2. **세계수 7루트:** Ascension 루트는 천상 네트워크(상부 세계수), Descent 루트는 지하 루트와 연결하여 플레이어 경로를 추적한다.  
3. **영적 7단 각성:** Ascension 단계별로 클래스 특성이 해금되며, 반대로 Descent 단계가 쌓이면 페널티와 서사 이벤트(추락 퀘스트)를 발생.  
4. **셀월드 규칙:** Truth Shader, Distortion Field, Terminal Lock 등을 행동 규칙에 등록하여 NPC가 방향성 기반 법칙을 따르게 한다.  
5. **Aura UI/LLM 브리지:** Ascension/Descent 필드 수치를 시각화하고, LLM 프롬프트에서 “상승/하강 경보”를 활용해 스토리 분기를 만든다.  
6. **신화 서사:** 각 화신의 언어/권능/기원을 시나리오 트리, 보스전, 혹은 종족 계보에 투영한다.

이 문서는 칠선/칠악을 “우주의 방향성”으로 고정하여, 엘리시아 엔진의 물리·의식·서사 계층이 하나의 축을 공유하도록 정규화한다.
