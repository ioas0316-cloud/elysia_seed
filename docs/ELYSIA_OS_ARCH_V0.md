# ELYSIA OS Architecture v0

## 구현자용 인터페이스

이 섹션은 Kernel-Service-App 경계에서 구현자가 따라야 할 **최소 계약(interfaces & contracts)** 을 정의한다.

### 1) 핵심 타입 정의 초안

#### `AxisState`
축 정렬 상태를 표현하는 런타임 구조체.

```ts
interface AxisState {
  axisId: string;                  // 축 식별자 (예: "intent", "memory", "tool")
  epoch: number;                   // 동일 lifecycle 내 재정렬 시 증가
  alignmentScore: number;          // 0.0 ~ 1.0, 정렬 신뢰도
  driftScore: number;              // 0.0 ~ 1.0, 기준점 대비 이탈도
  lastAlignedAt: string;           // ISO-8601 UTC timestamp
  sourceAnchors: SovereignAnchor[]; // 정렬에 사용된 기준점 집합
  status: "stable" | "degraded" | "realigning" | "failed";
}
```

#### `SovereignAnchor (@)`
시스템 전반에서 참조 가능한 주권 기준점(immutable semantic anchor).

```ts
interface SovereignAnchor {
  id: `@${string}`;                // 예: @mission, @safety, @user_policy
  version: string;                 // semver 또는 monotonic revision
  checksum: string;                // anchor payload 무결성 검증용
  scope: "kernel" | "service" | "app";
  invariants: string[];            // 반드시 유지되어야 할 규칙 목록
  createdAt: string;               // ISO-8601 UTC timestamp
  deprecatedAt?: string;           // 폐기 시점(선택)
}
```

#### `ProjectionContext`
입력 신호를 실행 가능한 상태로 투영할 때의 문맥.

```ts
interface ProjectionContext {
  lifecycleId: string;             // 실행 lifecycle 식별자
  requestId: string;               // 단일 요청 추적 ID
  caller: {
    appId: string;
    principalId: string;
    role: string;
  };
  axisSnapshot: AxisState[];       // 투영 시점의 축 상태 스냅샷
  activeAnchors: SovereignAnchor[];
  constraints: {
    latencyBudgetMs: number;
    tokenBudget?: number;
    consistencyLevel: "best_effort" | "strong";
  };
  trace: {
    spanId: string;
    parentSpanId?: string;
  };
}
```

#### `ScaleProfile`
배포/운영 스케일 특성에 따른 리소스 및 정책 프로필.

```ts
interface ScaleProfile {
  name: "dev" | "staging" | "prod" | string;
  maxConcurrentLifecycles: number;
  maxToolsPerRequest: number;
  memoryQuotaMb: number;
  channelQpsLimit: number;
  retryPolicy: {
    maxAttempts: number;
    backoffMs: number;
  };
  guardrails: {
    enforceAnchorValidation: boolean;
    driftThreshold: number;        // driftScore 임계치
    hardFailOnValidationError: boolean;
  };
}
```

---

### 2) 서비스 경계

#### Kernel이 보장할 것 (Lifecycle / Permission)

1. **Lifecycle orchestration**
   - `init -> active -> draining -> terminated` 상태 전이를 단일 상태기계로 보장.
   - 각 lifecycle에 대해 고유 `lifecycleId` 발급 및 종료 후 재사용 금지.
2. **Permission enforcement**
   - 앱/서비스 호출 전 capability 기반 권한 검사.
   - 권한은 `principalId + appId + scope` 조합으로 평가.
3. **Anchor consistency**
   - `SovereignAnchor` 버전 고정(pin) 또는 호환성 검사를 수행.
   - anchor checksum 불일치 시 실행 차단.
4. **Observability baseline**
   - 모든 요청에 `requestId`, `spanId`, `lifecycleId`를 강제 부여.
   - 서비스 이벤트를 공통 이벤트 버스로 수집.

#### Service(memory/tool/channel)가 제공할 API 계약

##### Memory Service
- 목적: 상태/문맥 저장 및 조회
- 계약:
  - `put(ctx: ProjectionContext, key: string, value: bytes, ttlSec?: number): PutResult`
  - `get(ctx: ProjectionContext, key: string): GetResult`
  - `query(ctx: ProjectionContext, filter: MemoryFilter): QueryResult`
- 보장:
  - key 단위 read-after-write 일관성(최소 same lifecycle).
  - 만료(TTL) 및 삭제 이벤트 발행.

##### Tool Service
- 목적: 외부 도구 실행/중개
- 계약:
  - `invoke(ctx: ProjectionContext, toolId: string, input: Json): ToolResult`
  - `describe(toolId: string): ToolSpec`
- 보장:
  - tool 실행 전 권한/정책 검사.
  - 실행 결과에 `exitCode`, `durationMs`, `policyDecision` 포함.

##### Channel Service
- 목적: 사용자/시스템 입출력 채널 관리
- 계약:
  - `publish(ctx: ProjectionContext, channel: string, payload: Json): Ack`
  - `subscribe(ctx: ProjectionContext, channel: string, cursor?: string): Stream<Event>`
- 보장:
  - 채널별 전송량 제한(QPS) 적용.
  - 이벤트 순서 보장 범위를 명시(채널 파티션 단위).

---

### 3) 최소 실행 시나리오 2개

동일한 lifecycle 내에서 두 앱이 동작하며, 같은 `lifecycleId`를 공유한다.

#### 시나리오 A: 메모리 보강형 Q&A 앱

- **입력**
  - 사용자 질의 텍스트
  - 세션 컨텍스트 키(`session:{id}`)
- **출력**
  - 최종 답변 텍스트
  - 근거 메모리 레코드 ID 목록
- **필요 권한**
  - `memory.read`, `memory.write`, `channel.publish:user`
- **실행 흐름(요약)**
  1. `Channel`로 질의 수신
  2. `Memory.query`로 관련 컨텍스트 조회
  3. 응답 생성 후 `Memory.put`으로 대화 요약 저장
  4. `Channel.publish`로 사용자 응답 반환

#### 시나리오 B: 툴 호출형 운영 자동화 앱

- **입력**
  - 운영 명령(예: "최근 drift 급증 원인 분석")
  - 대상 범위(서비스/시간창)
- **출력**
  - 구조화된 점검 리포트(JSON)
  - 실행한 tool invocation 로그
- **필요 권한**
  - `tool.invoke:observability/*`, `memory.read`, `channel.publish:ops`
- **실행 흐름(요약)**
  1. `Channel`로 운영 요청 수신
  2. `Tool.invoke`로 메트릭 조회/분석 도구 실행
  3. 결과를 `Memory`에 저장(선택)
  4. `Channel.publish`로 ops 채널에 리포트 송신

---

### 4) 관측 포인트(운영 지표 이벤트 정의)

아래 지표는 **이벤트 기반**으로 노출하며, 공통 스키마 `EventEnvelope`를 따른다.

```ts
interface EventEnvelope<T = unknown> {
  eventId: string;
  eventType: string;
  occurredAt: string;              // ISO-8601 UTC timestamp
  lifecycleId: string;
  requestId?: string;
  appId?: string;
  payload: T;
}
```

#### 이벤트 타입

1. `axis.drift.detected`
   - payload: `{ axisId, driftScore, threshold, anchorId, epoch }`
   - 용도: drift 분포, 급증 구간 탐지

2. `axis.realign.performed`
   - payload: `{ axisId, fromEpoch, toEpoch, reason, durationMs }`
   - 용도: 축 재정렬 횟수/소요시간 집계

3. `anchor.validation.failed`
   - payload: `{ anchorId, expectedChecksum, actualChecksum, scope }`
   - 용도: 검증 실패율 및 영향 범위 추적

4. `projection.rejected`
   - payload: `{ reasonCode, consistencyLevel, policyDecision }`
   - 용도: 투영 거부율(정책/정합성 원인 분리)

5. `service.contract.violation`
   - payload: `{ serviceType, apiName, violationType, details }`
   - 용도: 서비스 계약 위반 감지 및 회귀 추적

#### 집계 지표 예시

- `drift_rate = count(axis.drift.detected) / total_requests`
- `realign_per_1k_req = count(axis.realign.performed) / total_requests * 1000`
- `anchor_validation_failure_rate = count(anchor.validation.failed) / count(anchor_validation_attempts)`
- `projection_rejection_rate = count(projection.rejected) / total_projections`

운영 대시보드는 최소 `lifecycleId`, `appId`, `axisId` 차원을 기준으로 필터링 가능해야 한다.
