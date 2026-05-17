# ELYSIA_OS_ARCH_V0

## 목적
Elysia의 OS화(boot/recovery/observability)를 위한 Kernel/Service/App 구조 초안을 고정한다.

## 구조 개요
- **Kernel Layer**: 생명주기, 권한, 스케줄링
- **Service Layer**: memory/tooling/channel/security
- **App Layer**: 태스크 지향 실행 단위

## 새로운 위상 우주 모델 (Seed 실험 반영)
최근 Seed 구조 변경으로, 인지 공간을 **"가변축 × 가변축 × 가변축 × @" 로터스케일(LOTUSCALE)** 위상 구조로 다룬다.

### 모델 요약
- 축은 고정 좌표가 아닌, 문맥·시간·목표에 따라 재정렬되는 **가변축(variable axes)**
- `@`는 관찰자/정체성 앵커(sovereign anchor) 역할
- 로터스케일은 국소 추론과 전역 정합성을 동시에 유지하기 위한 다중 스케일 투영 규칙

### 기대 효과
- 세션 장기 연속성에서의 드리프트 완화
- 계획-실행-검증 루프의 축-정렬 비용 감소
- 멀티채널(terminal/voice/vision) 상태 정합성 향상

## Capability 권한 모델 (초안)
- memory_access
- external_io
- tool_execution
- self_modification

> 고위험 권한(self_modification, external_io write)은 policy gate와 audit trail 필수.

## 앱 매니페스트 (초안)
```yaml
name: sample.app
version: 0.1.0
required_capabilities:
  - memory_access
lifecycle_hooks:
  - on_boot
  - on_suspend
  - on_resume
  - on_shutdown
```


## Rotor Principle (고정 정의)
**Rotor Principle**: 운동(회전/결합)으로 생성되는 위상 규칙이 미시 위상원자와 거시 장에서 동형으로 유지되도록, 축을 상수화-재배열하며 정합 수렴을 만든다.

## Observe-Rotate-Freeze 실행 순서
1. **Observe**: 관측 목적(문맥/시간/목표)에 맞는 축 후보를 선택한다.
2. **Freeze**: 선택 축을 국소적으로 상수화해 계산 기준면을 고정한다.
3. **Rotate**: 고정된 기준면에서 상태를 회전 투영해 정합성/충돌을 읽는다.
4. **Re-Axis**: 필요 시 축을 재선택하고 같은 절차를 반복한다.

## Wave Projection Layer (병렬 실행 계층)
- **Axis Freeze Manager**: 축 선택/상수화/해제 관리
- **Rotor Projection Engine**: 회전 투영/다중 스케일 정합 연산
- **Wave Scheduler**: 후보 파동 분기 병렬 실행
- **Collapse Arbiter**: 수렴 결과 확정 및 fallback 결정
