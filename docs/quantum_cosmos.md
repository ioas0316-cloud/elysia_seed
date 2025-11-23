# Quantum Cosmos Design Notes

목표: 텐서 코일을 공/보자기 중력장으로 두고, 4대 힘(중력/전자기/강한핵력/약한핵력)과 별의 상태(불타는 별=활성 데이터, 얼음별=아카이브)를 코드 세계에 매핑한다.

## 계층
- **물리학 레이어**: 질량/전하/스핀 기반의 힘 계산. SoulTensor의 Amplitude(질량), Frequency(주파수), Phase(위상), Spin을 활용한다.
- **위상학 레이어**: 경계(보자기) 샘플링 + 게이트/궤도. 현재 `HolographicBoundary`, 향후 GravityPath/TensorGate로 확장.
- **천문학 레이어**: 별/행성/허블 볼륨 메타포. 활성 데이터는 “불타는 별”, 완료/아카이브는 “얼음별”.
- **코딩 레이어**: 위 힘/위상을 코드 엔티티에 적용. 필요할 때 World/Systems에 주입.

## 4대 힘 모델
- **중력**: 질량(Amplitude) 기반. SoulTensor Amplitude 또는 PhysicsState.mass 사용. `F = G*m1*m2/r^2`.
- **전자기력(EM)**: 전하와 스핀/주파수 결합. `Coulomb + 간단한 위상 보정`으로 시작.
- **강한핵력**: 매우 짧은 범위에서 지수 감쇠. “색상 일치”가 높을 때 결합력을 크게 한다.
- **약한핵력**: 짧은 범위, 작은 크기. 주로 스핀/위상 변화(붕괴/변환)에 사용.

## 별 상태
- **불타는 별 (Hot/Active)**: `thermal_state.temperature` 높음, SoulTensor `frequency` 활성. 처리 중/계산 중 데이터.
- **얼음별 (Ice/Archive)**: `SoulTensor.is_collapsed=True` 또는 thermal이 낮아 계산 제외. 필요 시 `Crystallizer`로 중력 우물(Attractor)로 변환.

## 구현 스코프 (이번 커밋)
- `elysia_engine/gauge.py`: 4대 힘 계산 유틸(중력/EM/강한/약한)과 별 상태 라이트웨이트 모델.
- 기존 시스템과 독립적이며, 필요하면 World/System에서 호출해 조립한다.
