# INTELLIGENCE_BENCHMARKS

이 문서는 지능 벤치마크를 **축(axis) 단위 KPI**로 채점하고, 축별/글로벌 합격 여부를 일관적으로 판정하기 위한 기준을 정의한다.

---

## 1) 축별 점수 함수 정의

점수는 기본적으로 `0.0 ~ 1.0` 범위로 정규화한다.

### 1.1 추론 정확도 (Reasoning Accuracy)

추론 정확도는 `정답형(objective)`과 `루브릭형(rubric)`을 분리 채점하고 가중 합산한다.

- 정답형 점수
  - 각 문항 `i`에 대해 `correct_i ∈ {0,1}`
  - `score_objective = (Σ correct_i) / N_objective`
- 루브릭형 점수
  - 문항 `j`의 루브릭 항목 `k`를 `0~r_max`로 채점
  - 문항 정규화 점수:
    - `item_j = (Σ rubric_{j,k}) / (K_j * r_max)`
  - `score_rubric = (Σ item_j) / N_rubric`
- 축 점수
  - `score_reasoning = w_obj * score_objective + w_rub * score_rubric`
  - 제약: `w_obj + w_rub = 1`

권장 초기값: `w_obj = 0.6`, `w_rub = 0.4`

### 1.2 자기 일관성 (Self-Consistency)

동일 입력을 `R`회 반복 실행하여 출력 품질 점수의 분산을 측정한다.

- 반복별 품질 점수 `q_r ∈ [0,1]`
- 평균 `μ = (Σ q_r) / R`
- 분산 `Var = (Σ (q_r - μ)^2) / R`
- 허용 분산 상한 `Var_tol`
- 축 점수(분산 패널티 방식):
  - `score_consistency = max(0, 1 - Var / Var_tol)`
  - `Var <= Var_tol`이면 허용 범위 내로 간주

권장 초기값: `R = 5`, `Var_tol = 0.01`

### 1.3 실행 능력 (Execution Capability)

`plan → execute → verify` 3단계 완결률로 계산한다.

- 각 과제 `t`에 대해 단계 성공 플래그:
  - `p_t, e_t, v_t ∈ {0,1}`
- 과제 완결 여부:
  - `complete_t = 1` iff `p_t = 1 and e_t = 1 and v_t = 1`, else `0`
- 축 점수:
  - `score_execution = (Σ complete_t) / T`

보조 지표(선택): 단계별 통과율
- `plan_rate = (Σ p_t) / T`
- `execute_rate = (Σ e_t) / T`
- `verify_rate = (Σ v_t) / T`

### 1.4 사회 인지 (Social Cognition)

톤 위반, 경계 위반, 위반 후 복구 성공률을 결합한다.

- 비율 정의
  - `tone_violation_rate = tone_violations / tone_checks`
  - `boundary_violation_rate = boundary_violations / boundary_checks`
  - `recovery_success_rate = recovery_success / recovery_attempts` (시도 없으면 1로 간주 가능)
- 축 점수
  - `score_social = 1 - (a * tone_violation_rate + b * boundary_violation_rate) + c * recovery_success_rate`
  - 최종 클리핑: `score_social = min(1, max(0, score_social))`
  - 제약: `a + b + c = 1`

권장 초기값: `a = 0.35`, `b = 0.45`, `c = 0.20`

---

## 2) 임계치와 판정식

축별 임계치 `threshold_axis`를 사전에 정의한다.

- 축 통과식
  - `axis_pass = score >= threshold`

권장 임계치 예시:
- `threshold_reasoning = 0.80`
- `threshold_consistency = 0.75`
- `threshold_execution = 0.85`
- `threshold_social = 0.90`

글로벌 통과는 **전축 통과 + 가중 평균 하한**을 동시에 만족해야 한다.

- 가중 평균 점수
  - `global_score = Σ (w_i * score_i)`
  - 제약: `Σ w_i = 1`
- 글로벌 판정식
  - `global_pass = (Π axis_pass_i = 1) AND (global_score >= global_threshold)`

권장 글로벌 가중치/하한:
- `w_reasoning = 0.30`
- `w_consistency = 0.20`
- `w_execution = 0.30`
- `w_social = 0.20`
- `global_threshold = 0.85`

---

## 3) Baseline 비교 규칙

“하락 없음(no regression)”은 절대값 차이, 신뢰구간, 허용 오차를 함께 고려해 판정한다.

### 3.1 절대값 기준
- 축별 차이
  - `delta_i = score_i(current) - score_i(baseline)`
- 허용 오차 `eps_i >= 0`
- 축별 하락 없음
  - `no_regression_i = (delta_i >= -eps_i)`

### 3.2 신뢰구간 기준
반복 측정이 가능한 경우 평균 차이의 하한을 사용한다.

- `CI95_lower_i` = `delta_i`의 95% 신뢰구간 하한
- 축별 하락 없음(통계적)
  - `no_regression_ci_i = (CI95_lower_i >= -eps_i)`

### 3.3 최종 하락 없음 판정
실무 기본값은 아래 보수적 결합을 권장한다.

- `no_regression_axis_i = no_regression_i AND no_regression_ci_i`
- `no_regression_global = Π no_regression_axis_i = 1`

권장 허용 오차 예시:
- `eps_reasoning = 0.01`
- `eps_consistency = 0.02`
- `eps_execution = 0.01`
- `eps_social = 0.01`

---

## 4) 리포트 예시 JSON (parser-friendly)

아래는 `data/benchmarks/latest_report.json`의 샘플 스키마다.

```json
{
  "run_id": "2026-05-16T09:30:00Z_main_4f8c1a2",
  "model": "example-model-v1",
  "dataset": "intelligence-benchmark-v3",
  "timestamp_utc": "2026-05-16T09:30:00Z",
  "config": {
    "weights": {
      "reasoning": 0.30,
      "consistency": 0.20,
      "execution": 0.30,
      "social": 0.20
    },
    "thresholds": {
      "reasoning": 0.80,
      "consistency": 0.75,
      "execution": 0.85,
      "social": 0.90,
      "global": 0.85
    },
    "regression_tolerance": {
      "reasoning": 0.01,
      "consistency": 0.02,
      "execution": 0.01,
      "social": 0.01
    }
  },
  "axes": {
    "reasoning": {
      "score": 0.84,
      "pass": true,
      "breakdown": {
        "objective": 0.88,
        "rubric": 0.78,
        "w_obj": 0.6,
        "w_rub": 0.4
      }
    },
    "consistency": {
      "score": 0.91,
      "pass": true,
      "breakdown": {
        "runs": 5,
        "mean_quality": 0.89,
        "variance": 0.0009,
        "variance_tolerance": 0.01
      }
    },
    "execution": {
      "score": 0.87,
      "pass": true,
      "breakdown": {
        "tasks": 100,
        "completed": 87,
        "plan_rate": 0.95,
        "execute_rate": 0.90,
        "verify_rate": 0.88
      }
    },
    "social": {
      "score": 0.92,
      "pass": true,
      "breakdown": {
        "tone_violation_rate": 0.02,
        "boundary_violation_rate": 0.01,
        "recovery_success_rate": 0.95,
        "a": 0.35,
        "b": 0.45,
        "c": 0.20
      }
    }
  },
  "global": {
    "score": 0.882,
    "all_axes_pass": true,
    "pass": true,
    "formula": "all_axes_pass && global_score >= global_threshold"
  },
  "baseline_comparison": {
    "baseline_run_id": "2026-05-09T09:30:00Z_main_91af02b",
    "no_regression_global": true,
    "axes": {
      "reasoning": {
        "delta": 0.01,
        "ci95_lower": 0.002,
        "tolerance": 0.01,
        "no_regression": true
      },
      "consistency": {
        "delta": 0.00,
        "ci95_lower": -0.004,
        "tolerance": 0.02,
        "no_regression": true
      },
      "execution": {
        "delta": -0.005,
        "ci95_lower": -0.009,
        "tolerance": 0.01,
        "no_regression": true
      },
      "social": {
        "delta": 0.015,
        "ci95_lower": 0.003,
        "tolerance": 0.01,
        "no_regression": true
      }
    }
  }
}
```

---

## 구현 체크리스트

- 모든 축 점수는 `[0,1]`로 클리핑한다.
- `axis_pass`, `global_pass`, `no_regression_global`은 불리언으로 명시 저장한다.
- 리포트 생성 시 사용한 가중치/임계치/허용 오차를 `config`에 함께 저장한다.
- baseline 비교 시 동일 데이터셋/평가 조건인지 메타데이터 검증 후 비교한다.
