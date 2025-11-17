# ⚔️ Chapter 3. Trinity Decision Engine

*(Body / Soul / Spirit 로 선택을 계산하는 법)*

---

## 1. 에이전트 기본 구조

```jsonc
{
  "id": "human_001",
  "trinity": {
    "body":   { "hp": 80, "hunger": 0.3, "thirst": 0.2, "pain": 0.1 },
    "soul":   { "bond": 0.7, "status": 0.5, "loneliness": 0.2 },
    "spirit": { "faith": 0.6, "meaning": 0.5, "promise": 0.8 }
  },
  "weights": {
    "body":   0.5,
    "soul":   0.3,
    "spirit": 0.2
  },
  "efp": {
    "energy":   1.0,
    "force":    0.3,
    "momentum": 0.4
  }
}
```

* `trinity.*` : 각 층의 상태
* `weights.*` : 그 존재가 어느 층을 우선하는가
* `efp` : Energy / Force / Momentum 내핵

---

## 2. 행동(Action) 정의

모든 행동 후보는 각 층에 어떤 영향을 줄지 갖고 있다.

```jsonc
{
  "id": "run_away",
  "delta": {
    "body":   { "hp": +0.2 },
    "soul":   { "bond": -0.4 },
    "spirit": { "meaning": -0.5 }
  }
}
```

* **도망(run_away)** → Body 보호, Soul/Spirit 손상  
* **싸우기(stand_and_fight)** → Body 위험, Soul/Spirit 강화

---

## 3. 층별 Force 함수

### 3.1 Body force

```python
def body_force(agent, action):
    dhp = action.delta["body"].get("hp", 0.0)
    pain = agent.trinity["body"]["pain"]
    hunger = agent.trinity["body"]["hunger"]
    thirst = agent.trinity["body"]["thirst"]

    survival_pressure = 0.4*hunger + 0.4*thirst + 0.2*pain
    return dhp * (1.0 + survival_pressure)
```

배고픔/갈증/통증이 높을수록 HP를 지키는 행동이 강하게 끌린다.

### 3.2 Soul force

```python
def soul_force(agent, action):
    dbond   = action.delta["soul"].get("bond", 0.0)
    dstatus = action.delta["soul"].get("status", 0.0)
    loneliness = agent.trinity["soul"]["loneliness"]

    social_need = 0.6*loneliness + 0.4*(1.0 - agent.trinity["soul"]["bond"])
    return (0.7*dbond + 0.3*dstatus) * (1.0 + social_need)
```

외로움/소속감 부족이 클수록 관계를 지키는 선택이 커진다.

### 3.3 Spirit force

```python
def spirit_force(agent, action):
    dpromise = action.delta["spirit"].get("promise", 0.0)
    dmeaning = action.delta["spirit"].get("meaning", 0.0)
    faith    = agent.trinity["spirit"]["faith"]

    calling = 0.5*faith + 0.5*agent.trinity["spirit"]["meaning"]
    return (0.6*dpromise + 0.4*dmeaning) * (1.0 + calling)
```

약속과 소명이 클수록 그걸 지키는 선택에 더 끌린다.

---

## 4. 통합 Force

```python
def total_force(agent, action):
    Fb = body_force(agent, action)
    Fs = soul_force(agent, action)
    Fp = spirit_force(agent, action)

    wb = agent.weights["body"]
    ws = agent.weights["soul"]
    wp = agent.weights["spirit"]

    return wb*Fb + ws*Fs + wp*Fp
```

weights는 직업/성향/성장이 결정한다.

---

## 5. 선택 규칙

```python
def choose_action(agent, actions):
    scores = [total_force(agent, a) for a in actions]
    probs = softmax(scores)
    return random_choice(actions, probs)
```

* 전사 → Body 비중↑, 싸움/생존 행동을 더 자주 선택  
* 성직자 → Spirit 비중↑, 약속/사명을 우선  
* 마법사 → Soul 중심, 관계/정보/포지션 행동을 선호

---

## 6. 레이어 생사와 각성

```python
body_alive   = agent.trinity["body"]["hp"] > 0
soul_alive   = agent.trinity["soul"]["bond"] > 0.05
spirit_alive = agent.trinity["spirit"]["meaning"] > 0.05
```

* Body false → 물리적 사망  
* Soul false → 사회적/정서적 붕괴  
* Spirit false → 의미 붕괴

붕괴 시 weights 조정:

```python
if not soul_alive:
    agent.weights["body"] += 0.2
    agent.weights["spirit"] += 0.2

if not spirit_alive:
    agent.weights["body"] += 0.3
```

각성/회심 이벤트:

```python
agent.weights["spirit"] += 0.3
normalize(agent.weights)
```

---

## 7. 직업별 예시

| 역할 | weights (body/soul/spirit) | 특징 |
| --- | --- | --- |
| **전사/도적/대장장이** | 0.6 / 0.3 / 0.1 | HP·전술 행동 우선, 전우가 있으면 희생도 가능 |
| **마법사/상인/학자** | 0.2 / 0.6 / 0.2 | 정보·관계·평판 중심, 소속 붕괴 시 방황 |
| **성직자/무당/왕** | 0.2 / 0.2 / 0.6 | 신념/약속이 몸보다 우선, 순교·자진 희생 경향 |

---

## 8. 엔진 이식 체크리스트

필수 데이터:

* `trinity.body/soul/spirit`
* `weights.body/soul/spirit`
* `efp` (선택)
* 각 행동의 `delta`

필수 함수:

1. `body_force`
2. `soul_force`
3. `spirit_force`
4. `total_force`
5. `choose_action`
6. (옵션) `update_weights_by_experience`

이 6개만 구현하면 어떤 엔진에서도 삼위일체 행동결정 모델을 그대로 이식할 수 있다.
