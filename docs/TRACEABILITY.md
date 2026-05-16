# TRACEABILITY

## 1) Seed 개념 ↔ Main 구현 위치 매핑

| Seed 개념 | Main 구현 위치(모듈 경로) | 비고 |
|---|---|---|
| Boot sequence | `Core/sovereign_boot.py` | Main 부팅 엔트리 |
| Tool protocol | `Core/Merkaba/portal.py` | 실행 오케스트레이션 |
| Memory metadata | `Core/Foundation/Nature/metal_field_bridge.py` | 저장 계층 메타데이터/브리지 |

## 2) 확인 주기

- 월 1회, **승격 윈도우 이전**에 상기 매핑 링크(모듈 경로) 유효성을 검증한다.

## 3) 변경 알림 규칙

- Main에서 인터페이스(시그니처, 입출력 스키마, 호출 규약) 변경이 발생하면, Seed 문서(`docs/CONTRACTS.md` 또는 `docs/TRACEABILITY.md`)를 **의무적으로 동기 업데이트**한다.
