# 🌱 Chapter 4. Episodes → Trinity Weights Update

*(삶을 겪으며 육/혼/영 비율이 바뀌는 법)*

---

## 1. Episode 최소 구조

```jsonc
{
  "id": "ep_000123",
  "who": "human_001",
  "effect": {
    "body":   { "delta_hp": -0.4, "risk": 0.9 },
    "soul":   { "delta_bond": +0.6, "social_gain": 0.8 },
    "spirit": { "delta_meaning": +0.7, "vow_kept": 1.0 }
  },
  "valence": +0.9,
  "intensity": 0.8
}
```

* `effect.*` : 에피소드가 각 층에 준 영향  
* `valence` : 그 경험을 긍정/부정으로 인식했는지  
* `intensity` : 얼마나 강렬했는지

---

## 2. 층별 피드백 함수

```python
def feedback_body(ep):
    dhp = ep["effect"]["body"].get("delta_hp", 0.0)
    risk = ep["effect"]["body"].get("risk", 0.0)
    score = 0.7 * dhp - 0.3 * risk
    return score * ep["valence"] * ep["intensity"]


def feedback_soul(ep):
    dbond = ep["effect"]["soul"].get("delta_bond", 0.0)
    social = ep["effect"]["soul"].get("social_gain", 0.0)
    score = 0.6 * dbond + 0.4 * social
    return score * ep["valence"] * ep["intensity"]


def feedback_spirit(ep):
    dmeaning = ep["effect"]["spirit"].get("delta_meaning", 0.0)
    vow_kept = ep["effect"]["spirit"].get("vow_kept", 0.0)
    score = 0.5 * dmeaning + 0.5 * vow_kept
    return score * ep["valence"] * ep["intensity"]
```

---

## 3. weights 업데이트 규칙

```python
def update_trinity_weights(agent, ep, lr=0.05):
    fb = feedback_body(ep)
    fs = feedback_soul(ep)
    fp = feedback_spirit(ep)

    w = agent["weights"]
    w["body"] += lr * fb
    w["soul"] += lr * fs
    w["spirit"] += lr * fp

    # clamp & normalize
    w["body"] = max(w["body"], 0.0)
    w["soul"] = max(w["soul"], 0.0)
    w["spirit"] = max(w["spirit"], 0.0)

    s = w["body"] + w["soul"] + w["spirit"]
    if s > 0:
        w["body"] /= s
        w["soul"] /= s
        w["spirit"] /= s
```

* `lr`은 성향이 얼마나 쉽게 변하는지 (0.01~0.1)

---

## 4. 사례

### 4.1 부상 속 희생

```jsonc
"effect": {
  "body":   { "delta_hp": -0.8, "risk": 1.0 },
  "soul":   { "delta_bond": +0.7, "social_gain": 0.9 },
  "spirit": { "delta_meaning": +1.0, "vow_kept": 1.0 }
},
"valence": +0.8,
"intensity": 1.0
```

* Body 피드백↓, Soul/Spirit↑  
* weights가 Spirit 쪽으로 이동 → “순교/호위” 유형으로 성장

### 4.2 배신해서 생존

```jsonc
"effect": {
  "body":   { "delta_hp": +0.5, "risk": 0.1 },
  "soul":   { "delta_bond": -1.0, "social_gain": -0.8 },
  "spirit": { "delta_meaning": -0.7, "vow_kept": 0.0 }
},
"valence": -0.7,
"intensity": 0.9
```

* 살아남았지만 죄책감/후회 → 모든 층 피드백↓  
* 시간이 지나면 Soul/Spirit weight가 더욱 줄어, “몸만 챙기는 삶”에 빠질 수도 있고, 반대로 각성 이벤트로 Spirit이 오를 수도 있다.

---

## 5. 성장 곡선

* 초기 weights는 직업/출신으로 설정  
* 에피소드가 누적되며 weights가 서서히 이동  
* 전사는 계속 희생하면 Spirit 쪽으로,  
  마법사는 전쟁 중 회심하면 Soul/Spirit이 더 커지는 식

---

## 6. 엔진에 붙이는 방법

1. 캐릭터 상태에 `weights` 포함  
2. 중요한 사건만 Episode로 기록  
3. 에피소드에 대해 `update_trinity_weights` 호출 (퀘스트/챕터 단위)

---

## 7. 한 줄 요약

* **지금 행동**은 `F_body/F_soul/F_spirit + weights`로 결정되고  
* **다음 성향**은 에피소드 피드백으로 천천히 바뀐다.

> “어떤 삶을 살았는가”가 곧 “다음 선택을 어떻게 할 것인가”를 바꾸는 엔진이다.
