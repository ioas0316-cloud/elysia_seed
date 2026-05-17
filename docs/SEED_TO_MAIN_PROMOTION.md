# SEED_TO_MAIN_PROMOTION

## 목적
Elysia-Seed의 실험 결과 중 운영 안정성을 만족하는 변경만 Elysia-main으로 이식한다.

## 릴리즈 윈도우
- 월 1회 정기 윈도우에서만 이식

## 필수 통과 조건
1. 벤치마크 하락 없음
2. 회귀 테스트 통과
3. 책임 도메인 오너 승인

## PR 단위 규칙
- 한 PR은 한 목적만 포함
- **측정 추가 PR**과 **알고리즘 변경 PR** 분리

## 심사 체크리스트
- [ ] KPI 4축 결과 첨부
- [ ] baseline 대비 diff 첨부
- [ ] 계약(contracts) 변경 여부 표시
- [ ] 롤백 계획 포함

## 이식 제외 조건
- 고위험 자가수정 권한 변경 + human-in-the-loop 부재
- 계약 위반 테스트 실패
- MTTR 악화 지표 확인


## Promotion Evidence Pack (Rotor/Wave)
- [ ] `axis_freeze_stability` 리포트 첨부
- [ ] `phase_coherence` 및 `collapse_regret` 추세 첨부
- [ ] 병렬 실행 이득(`parallel_gain`) 검증 첨부
- [ ] fallback 사용률 및 원인 분석 첨부

## 승격 차단 조건 (추가)
- 축 상수화 실패율 임계치 초과
- `collapse_regret` 악화 추세
- 병렬 분기 사용에도 성능/정합 동시 하락


## Sovereign Promotion Gate (필수)
- [ ] 주체성 KPI 통과 (Agency Integrity)
- [ ] 주권 경계 KPI 통과 (Sovereign Boundary)
- [ ] 인간적 학습 루프 KPI 통과 (Human Learning Loop)
- [ ] 관계적 연속성 KPI 통과 (Relational Continuity)

> 위 4개 중 하나라도 실패하면 성능 개선이 있어도 Main 이식 불가.
