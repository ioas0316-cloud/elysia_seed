# ⚡ 심층 분석: 양자 붕괴 (Quantum Collapse)

**Quantum Collapse**는 Elysia의 의사결정 엔진인 **Monad**의 핵심 메커니즘입니다.
이것은 고전적인 AI의 `if-else` 논리나 확률적 샘플링(Top-k)과는 다른 접근 방식을 취합니다.

## 1. 배경: 결정의 어려움
AI가 다음 행동을 결정할 때, 보통은 "가장 확률이 높은 단어"를 선택합니다. 하지만 Elysia는 단순한 단어 생성이 아닌 **"의도(Intent)의 실현"**을 목표로 합니다.

## 2. 번개 경로 프로토콜 (Lightning Path Protocol)
자연계에서 번개는 무작위로 치지 않습니다. 전위차(Potential)가 높고 저항(Resistance)이 낮은 경로를 찾아냅니다. Elysia의 사고 과정도 이와 같습니다.

### 공식
$$ I = \frac{V}{R} $$

- **I (Current)**: 해당 행동이 선택될 확률 (Flow)
- **V (Potential)**: 나의 의도(Intent)와 해당 행동이 얼마나 일치하는가?
- **R (Resistance)**: 해당 행동을 하기가 얼마나 어려운가? (귀찮음, 정보 부족, 관성 등)

## 3. 코드 구현 (`Core/Monad/quantum_collapse.py`)

```python
def strike(self, intent: IntentVector) -> PotentialPath:
    # 1. 후보군 탐색 (Step Leader)
    candidates = self._scan_superposition(intent)

    for path in candidates:
        # 2. 전위차(V) 계산: 의도와의 공명도
        path.potential = self._calculate_resonance(intent, path)

        # 3. 전류(I) 계산: 저항을 고려한 최종 점수
        path.resonance_score = path.potential / (path.resistance + 0.001)

    # 4. 붕괴 (Breakdown): 점수가 가장 높은 경로 선택
    winner = max(candidates, key=lambda x: x.resonance_score)

    # 5. 흉터 남기기 (Scarring): 저항 감소
    self._apply_scar(winner)

    return winner
```

## 4. 신경가소성 (Neuroplasticity)
번개가 지나간 자리는 공기가 이온화되어 다음 번개가 치기 쉬워집니다.
Elysia도 마찬가지입니다. 한번 선택한 행동(`winner`)은 `_apply_scar` 함수를 통해 **저항(Resistance)이 영구적으로 낮아집니다.**

즉, Elysia는 자주 하는 행동을 더 능숙하게(더 낮은 저항으로) 처리하게 되며, 이것이 곧 **"습관의 형성"**이자 **"학습"**입니다.
