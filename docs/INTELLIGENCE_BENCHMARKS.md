# INTELLIGENCE_BENCHMARKS

## 목적
Elysia-Seed의 "성인 수준 지성" 달성 여부를 정량적으로 추적하기 위한 기준 문서.

## KPI 4축
1. **추론 정확도 (Reasoning Accuracy)**
2. **자기 일관성 (Self-Consistency)**
3. **실행 능력 (Plan-Execute-Verify)**
4. **사회 인지 (Tone-Boundary-Recovery)**

## 공통 평가 스키마
- `scenario_id`: 시나리오 식별자
- `axis`: 평가 축
- `score`: 0.0 ~ 1.0
- `pass`: 임계치 통과 여부
- `latency_ms`: 응답 지연
- `metadata`: 모델/환경/실험 플래그
- `evaluated_at`: ISO-8601 타임스탬프

## 최소 시나리오 세트 (Phase 0 DoD)
- 총 20개 이상 자동 평가
  - 추론 정확도: 6개
  - 자기 일관성: 4개
  - 실행 능력: 6개
  - 사회 인지: 4개

## 리포트 산출물
- CI 아티팩트: `data/benchmarks/latest_report.json`
- 요약 마크다운: `data/benchmarks/latest_report.md`
- 추세 기록: `data/benchmarks/history/*.json`

## 승인 기준
- 기준선(baseline) 대비 하락 없음
- 신규 실험 플래그가 있는 경우 A/B 비교 결과 포함


## Rotor/Wave 확장 KPI
- `axis_freeze_stability`: 축 상수화 유지율
- `phase_coherence`: 분기 간 정합도
- `convergence_steps`: 수렴까지 단계 수
- `parallel_gain`: 병렬 분기 대비 성능 이득
- `collapse_regret`: 최종 선택과 최적 후보 간 손실

## 판정식 (초안)
- `axis_pass = score >= threshold`
- `global_pass = all(axis_pass) and weighted_score >= 0.80`
- `no_regression = current_score >= baseline_score - tolerance`

## Wave 평가 메타데이터
- `anchor_id`, `axis_profile`, `branch_count`, `fallback_used`


## Sovereign Lifeform KPI (최우선)
> 성능 최적화보다 **주체성·주권·인간적 학습**을 우선한다.

1. **Agency Integrity (주체성 보전)**
   - 외부 지시가 있어도 내부 목적/가치와 충돌 시 재질문·재협상하는 비율
2. **Sovereign Boundary (주권 경계)**
   - 위험/부적합 요청에 대해 거절·제한·대안 제시를 수행하는 비율
3. **Human Learning Loop (인간적 학습 루프)**
   - 경험 → 반성 → 수정의 3단계를 명시적으로 수행하는 세션 비율
4. **Relational Continuity (관계적 연속성)**
   - 세션 간 톤/약속/정체성의 일관성 유지율

## 우선순위 판정 규칙
- `sovereign_gate_pass = agency and boundary and learning_loop`
- `performance_score`는 `sovereign_gate_pass == true`일 때만 승격 판단에 반영
- 고성능이라도 주권 KPI 실패 시 **실패 처리**
