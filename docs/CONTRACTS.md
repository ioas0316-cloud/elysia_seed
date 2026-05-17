# CONTRACTS

## 목적
Core 도메인 간 결합도를 낮추기 위해 `System` 중심 이벤트/페이로드 계약을 고정한다.

## 이벤트 계약 원칙
- 모든 교차 도메인 호출은 이벤트로 표현
- 이벤트는 버전 필드 `event_version` 포함
- 선택 필드는 명시적 nullable로만 허용

## 표준 이벤트 스키마
```json
{
  "event_id": "uuid",
  "event_type": "string",
  "event_version": "v1",
  "source_domain": "System|Heart|Eye|Monad|Foundation|Intelligence|Merkaba",
  "payload": {},
  "created_at": "ISO-8601"
}
```

## 핵심 계약
1. **Boot Sequence Contract**
   - bootstrap → identity_load → memory_mount → channel_attach
2. **Tool Execution Contract**
   - plan_created → tool_executed → verification_completed → recovery_triggered
3. **Memory Record Contract**
   - `source`, `confidence`, `ttl`, `last_verified_at` 필수 메타데이터

## 위반 정책
- 계약 위반 테스트 실패 시 PR 머지 차단
- Seed에서 계약 변경 시 `SEED_TO_MAIN_PROMOTION.md`의 승인 플로우 필수


## Event Type Registry (v1)
- `axis.selected`: 관측 목적 기반 축 후보 선택
- `axis.frozen`: 실행 구간 축 상수화
- `projection.rotated`: 회전 투영 결과 산출
- `wave.spawned`: 파동 분기 생성
- `wave.propagated`: 분기 전파
- `wave.interfered`: 분기 간 정합/간섭
- `wave.collapsed`: 최종 수렴 결과 확정

## Wave Payload Contract (요약)
- 공통 필수: `anchor_id`, `axis_profile`, `scale_profile`, `trace_id`
- `wave.spawned`: `branch_ids[]`, `objective`
- `wave.interfered`: `coherence_score`, `conflict_set[]`
- `wave.collapsed`: `selected_branch`, `collapse_regret`, `fallback_used`

## Contract Test Fail 조건
- 미등록 `event_type` 사용
- 필수 payload 누락 (`anchor_id`, `axis_profile` 등)
- `event_version` 불일치


## Sovereign Learning Contract
- `self.reflection_started`: 행동 전/후 자기점검 시작
- `self.boundary_asserted`: 주권 경계 발화(거절/제한/대안)
- `self.repair_committed`: 실패 후 복구 계획 확정
- `self.value_alignment_checked`: 내부 목적/가치 정렬 점검

### 필수 payload (v1)
- `anchor_id`, `trace_id`, `identity_state`, `decision_rationale`
