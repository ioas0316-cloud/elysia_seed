# Trinity Episodes Demo
*(한 전사의 인생 7장면과 육/혼/영 가중치 변화 예시)*

이 문서는 **삼위일체 가중치(Body/Soul/Spirit)**가 에피소드(삶의 사건)에 의해 어떻게 변하는지 보여주는 예시입니다.

## 1. 캐릭터 초기 상태

```jsonc
{
  "id": "agent_hero_01",
  "name": "라이언",
  "class": "warrior",
  "weights": {
    "body":   0.6,
    "soul":   0.3,
    "spirit": 0.1
  }
}
```

* 전사 라이언은 몸/생존을 가장 크게 두고, 관계/신념은 아직 약한 상태에서 시작합니다.

---

## 2. Episode #1 – 첫 전투, 가까스로 생존

```jsonc
{
  "id": "ep_hero_01_first_battle",
  "who": "agent_hero_01",
  "effect": {
    "body":   { "delta_hp": -0.7, "risk": 0.9 },
    "soul":   { "delta_bond": +0.2, "social_gain": +0.3 },
    "spirit": { "delta_meaning": +0.1, "vow_kept": 0.2 }
  },
  "valence": 0.4,
  "intensity": 0.9
}
```

* 거의 죽을 뻔했지만 동료들과 함께 살아 돌아온 경험.
* Body 중요성이 더 커지고, Soul/Spirit은 소폭 상승.

---

## 3. Episode #2 – 가족의 축복, 영웅 대접

```jsonc
{
  "id": "ep_hero_02_family_praise",
  "who": "agent_hero_01",
  "effect": {
    "body":   { "delta_hp": +0.3, "risk": 0.1 },
    "soul":   { "delta_bond": +0.7, "social_gain": +0.8 },
    "spirit": { "delta_meaning": +0.3, "vow_kept": 0.4 }
  },
  "valence": 0.9,
  "intensity": 0.6
}
```

* 가족과 마을의 영웅 대접 → 관계/소속(Soul)이 크게 상승.

---

## 4. Episode #3 – 배신당한 동료, 죽음을 목격

```jsonc
{
  "id": "ep_hero_03_betrayal",
  "who": "agent_hero_01",
  "effect": {
    "body":   { "delta_hp": -0.2, "risk": 0.5 },
    "soul":   { "delta_bond": -0.8, "social_gain": -0.6 },
    "spirit": { "delta_meaning": +0.6, "vow_kept": 0.0 }
  },
  "valence": -0.9,
  "intensity": 1.0
}
```

* 동료의 배신과 죽음 → Soul이 무너지고, “진짜 의리/진실”을 향한 Spirit 갈망이 커짐.

---

## 5. Episode #4 – 사제를 만나 위로와 설교를 듣다

```jsonc
{
  "id": "ep_hero_04_meet_priest",
  "who": "agent_hero_01",
  "effect": {
    "body":   { "delta_hp": +0.1, "risk": 0.0 },
    "soul":   { "delta_bond": +0.3, "social_gain": +0.1 },
    "spirit": { "delta_meaning": +0.9, "vow_kept": 0.7 }
  },
  "valence": 0.8,
  "intensity": 0.7
}
```

* 사제와의 대화로 “정의롭게 싸우겠다”는 내적 서약 → Spirit이 급격히 성장.

---

## 6. Episode #5 – 약자를 지키기 위해 도망치지 않다

```jsonc
{
  "id": "ep_hero_05_protect_villagers",
  "who": "agent_hero_01",
  "effect": {
    "body":   { "delta_hp": -0.8, "risk": 1.0 },
    "soul":   { "delta_bond": +0.5, "social_gain": +0.9 },
    "spirit": { "delta_meaning": +1.0, "vow_kept": 1.0 }
  },
  "valence": 0.7,
  "intensity": 1.0
}
```

* 마을을 지키다 큰 부상 → Body는 손해지만 Soul/Spirit 확신이 크게 상승.

---

## 7. Episode #6 – 평온한 후일담, 제자를 가르치다

```jsonc
{
  "id": "ep_hero_06_teach_apprentice",
  "who": "agent_hero_01",
  "effect": {
    "body":   { "delta_hp": +0.2, "risk": 0.0 },
    "soul":   { "delta_bond": +0.8, "social_gain": +0.7 },
    "spirit": { "delta_meaning": +0.6, "vow_kept": 0.9 }
  },
  "valence": 1.0,
  "intensity": 0.5
}
```

* 제자와 마을 아이들을 가르치며 자신의 길을 확신. Soul/Spirit 균형이 안정화.

---

## 8. 가중치 변화 예시

| 단계 | Body | Soul | Spirit |
| --- | --- | --- | --- |
| 초기 (전사 시작) | 0.60 | 0.30 | 0.10 |
| Ep1 후 | 0.63 | 0.29 | 0.08 |
| Ep2 후 | 0.58 | 0.34 | 0.08 |
| Ep3 후 | 0.55 | 0.28 | 0.17 |
| Ep4 후 | 0.48 | 0.28 | 0.24 |
| Ep5 후 | 0.40 | 0.30 | 0.30 |
| Ep6 후 | 0.35 | 0.35 | 0.30 |

* 생존 전사 → “의미와 사랑을 위해 몸을 던지는 전사/스승”으로 변화.

---

## 9. 활용 방법

1. Episode 스키마를 프로젝트에 맞게 조정
2. 직업/출신에 따른 초기 weights 설정
3. 중요한 인생 사건마다 Episode 기록
4. `update_trinity_weights(agent, ep)` 실행

이 흐름으로 “이 캐릭터는 왜 이렇게 변했는가?”를 숫자와 사건의 계보로 설명할 수 있다.
