# SEED to MAIN Promotion

## Promotion Evidence Pack

프로모션 승인 요청 시 아래 **필수 첨부물**을 PR 본문에 포함해야 합니다.

### 1) 필수 첨부물 경로 규격

- **KPI 리포트**: `data/benchmarks/...`
- **회귀 결과**: `Core/tests` 실행 결과 요약
- **계약 영향 분석**: `docs/CONTRACTS.md` 변경 diff 링크

### 2) PR 템플릿 체크리스트 강화

- **PR 분류 필드 추가**: 측정 PR / 알고리즘 PR
- **롤백 절차 명시**:
  - 실행 명령
  - 롤백 대상 브랜치
  - 복구 시간 목표(RTO)

### 3) 승인자 매트릭스

도메인별 required approver를 아래 표로 명시합니다.

| 도메인 | Required Approver |
|---|---|
| System | System 소유자 |
| Heart | Heart 소유자 |
| Memory | Memory 소유자 |
