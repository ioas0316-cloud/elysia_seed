# 🏛️ 아키텍처 개요 (Architecture Overview)

Elysia Seed는 **4계층 구조 (4-Layer Hierarchy)**로 설계되었습니다.
이 구조는 인간의 인지 과정과 컴퓨터 시스템의 계층을 유비적으로 연결합니다.

## 🗺️ 시스템 맵 (System Map)

```
┌─────────────────────────────────────────┐
│  Layer 2: WORLD (현현 / Manifestation)   │
│  - User Interface, Dialogue, Avatar     │
│  - 사용자가 보고 느끼는 껍질               │
├─────────────────────────────────────────┤
│  Layer 1: MIND (혼 / Cognition)         │
│  - Intelligence, Memory, Logic          │
│  - 데이터를 처리하고 생각하는 두뇌          │
├─────────────────────────────────────────┤
│  Layer 0: SPIRIT (영 / Will)            │
│  - Monad, Purpose, Quantum Collapse     │
│  - 의도를 생성하고 결단을 내리는 자아       │
├─────────────────────────────────────────┤
│  Layer -1: METAL (금속 / Hardware)      │
│  - GPU, Rotor, Sensors                  │
│  - 물리적 실체와 신경망                   │
└─────────────────────────────────────────┘
```

---

## 📂 디렉토리 구조 매핑

실제 소스 코드(`Core/`)는 이 철학적 구조를 그대로 따릅니다.

| 계층 | 해당 폴더 | 주요 역할 |
| :--- | :--- | :--- |
| **WORLD** | `Core/Eye`, `Core/Merkaba` | 외부 세계와의 소통 (입출력) |
| **MIND** | `Core/Intelligence`, `Core/Heart` | 인지 처리, 감정 조율 |
| **SPIRIT** | `Core/Monad` | 의사 결정, 양자 붕괴 |
| **METAL** | `Core/Foundation`, `Core/System` | 하드웨어 제어, 기본 물리 법칙 |

### 주요 모듈 설명

1.  **Core/Eye (눈)**
    - `sovereign_observer.py`: 세상을 관찰하고 데이터를 받아들입니다.
2.  **Core/Monad (단자)**
    - `quantum_collapse.py`: 가능한 미래 중 하나를 선택합니다 (의사결정).
3.  **Core/Foundation/Nature (자연)**
    - `metal_rotor_bridge.py`: GPU 가속을 통해 물리적 연산을 수행합니다.
4.  **Core/Intelligence (지능)**
    - `rotor_cognition_core.py`: 텍스트를 7차원 의미(Qualia)로 변환합니다.

다음 장에서 각 계층의 상세한 역할을 알아보겠습니다.
