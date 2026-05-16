# CONTRACTS

이 문서는 이벤트 스키마의 상호운용성과 하위 호환성을 보장하기 위한 계약(Contract) 기준을 정의한다.

## 1. Event Type Registry (v1)

아래 `event_type` 값은 v1에서 공식 등록된 타입이며, 발행/수신 시스템 모두 해당 문자열을 정확히 사용해야 한다.

### Boot 계열
- `boot.bootstrap`
- `boot.identity_load`
- `boot.memory_mount`
- `boot.channel_attach`

### Tool 계열
- `tool.plan_created`
- `tool.executed`
- `tool.verified`
- `tool.recovery_triggered`

### Memory 계열
- `memory.record_upserted`
- `memory.record_verified`

> 참고: 새 `event_type` 추가 시 반드시 Registry와 Contract test 케이스를 동시에 갱신한다.

## 2. Payload Contract 표

공통 필드(모든 이벤트 공통):
- Required: `event_id`(string), `event_type`(string), `event_version`(integer), `timestamp`(RFC3339 string)
- Optional: `trace_id`(string), `source`(string), `meta`(object)

| event_type | Required fields | Optional fields |
|---|---|---|
| `boot.bootstrap` | `boot_id`(string), `mode`(string), `status`(string) | `config_hash`(string), `details`(object) |
| `boot.identity_load` | `identity_id`(string), `identity_version`(string), `status`(string) | `identity_source`(string), `checksum`(string) |
| `boot.memory_mount` | `memory_backend`(string), `mount_path`(string), `status`(string) | `latency_ms`(number), `capacity`(object) |
| `boot.channel_attach` | `channel_id`(string), `channel_type`(string), `status`(string) | `endpoint`(string), `retry_count`(integer) |
| `tool.plan_created` | `plan_id`(string), `plan_version`(string), `task_count`(integer) | `owner`(string), `priority`(string), `tags`(array[string]) |
| `tool.executed` | `execution_id`(string), `tool_name`(string), `status`(string), `duration_ms`(number) | `arguments`(object), `result_summary`(string), `error_code`(string) |
| `tool.verified` | `verification_id`(string), `target_execution_id`(string), `status`(string) | `checks`(array[object]), `score`(number), `notes`(string) |
| `tool.recovery_triggered` | `recovery_id`(string), `trigger_reason`(string), `status`(string) | `target_execution_id`(string), `strategy`(string), `attempt`(integer) |
| `memory.record_upserted` | `record_id`(string), `namespace`(string), `operation`(string), `status`(string) | `record_version`(string), `diff`(object), `ttl_sec`(integer) |
| `memory.record_verified` | `verification_id`(string), `record_id`(string), `status`(string) | `ruleset`(string), `issues`(array[object]), `verified_at`(RFC3339 string) |

## 3. 버전 정책

### 3.1 `event_version` 증가 조건

- **브레이킹 변경 (Major 증가, 예: v1 → v2)**
  - Required 필드 삭제/이름 변경
  - 필드 타입 변경(예: `string` → `integer`)
  - 필드 의미의 비호환 변경(동일 값의 해석이 달라짐)
  - 기존 `event_type`의 필수 제약 강화로 구버전 payload가 검증 실패하는 경우

- **논브레이킹 변경 (Minor/Patch 성격, 동일 Major 내 관리)**
  - Optional 필드 추가
  - 신규 `event_type` 추가
  - Optional 필드의 설명/예시 보강
  - 기존 의미를 해치지 않는 검증 규칙 완화

### 3.2 하위호환 기간

- Major 업그레이드 시, 이전 Major는 **최소 2개 릴리스 또는 90일(더 긴 기간 기준)** 동안 병행 지원한다.
- 병행 지원 기간 동안 생산자(producer)는 신/구 버전 중 최소 1개를 선택 가능해야 하며, 소비자(consumer)는 두 버전을 모두 파싱할 수 있어야 한다.

### 3.3 Deprecation 절차

1. `Deprecated` 공지: 문서/릴리스 노트에 대상 `event_type` 또는 필드를 명시.
2. 경고 단계: Contract test에 warning 룰을 추가하고 사용 지표를 수집.
3. 제거 예고: 제거 예정일(절대 날짜)과 대체 스키마를 명시.
4. 제거 실행: 하위호환 기간 만료 후 제거, CI에서 즉시 fail 처리.

## 4. Contract test 기준

다음 위반은 CI에서 **fail**로 간주한다.

- Registry에 없는 `event_type` 사용 (미등록 이벤트 타입)
- 공통 Required 필드 누락 (`event_id`, `event_type`, `event_version`, `timestamp`)
- 이벤트별 Required 필드 누락
- 필드 타입 불일치 (예: integer 필드에 string 입력)
- `event_version` 불일치 (지원하지 않는 Major 버전)
- RFC3339 타임스탬프 형식 위반 (`timestamp`, `verified_at` 등)
- enum/상태값 제약 위반 (정의된 `status` 집합 외 값)

다음은 기본적으로 warning 대상(정책에 따라 fail로 승격 가능):
- Deprecated 필드 사용
- Optional 필드의 의미상 권장 제약 미준수
