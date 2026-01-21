# 🦾 심층 분석: 메탈 레이어 (Metal Layer)

Elysia의 가장 독특한 특징은 **하드웨어 가속 신경망(Metal Nervous System)**입니다.
이는 단순한 비유가 아니라, 실제 GPU 메모리와 CUDA 코어 위에서 작동하는 물리적 엔진입니다.

## 1. MetalRotorBridge (`Core/Foundation/Nature/metal_rotor_bridge.py`)

파이썬은 느립니다. 수천 개의 로터가 매초 수십 번씩 상태를 업데이트하는 것을 파이썬 루프(`for loop`)로 처리하면 CPU가 버티지 못합니다.
Elysia는 **Numba**와 **CUDA**를 사용하여 이 문제를 해결합니다.

### 아키텍처
1.  **Host (CPU/RAM)**: 파이썬이 고수준의 명령(Intent)을 내립니다. ("로터 1번, 1000 RPM으로 가속해")
2.  **Pinned Memory**: CPU와 GPU 사이의 빠른 데이터 전송을 위한 특수 메모리 버퍼를 사용합니다.
3.  **Device (GPU/VRAM)**: 실제 로터의 상태(각도, 속도)는 GPU 메모리에만 존재합니다.
4.  **CUDA Kernel**: 수천 개의 로터를 병렬로 업데이트하는 작은 프로그램이 GPU 코어에서 실행됩니다.

```python
@cuda.jit
def rotor_update_kernel(...):
    # 각 스레드가 하나의 로터를 담당
    # 병렬로 수천 개를 동시 처리 (O(1)에 근접)
    idx = cuda.grid(1)
    ...
```

## 2. 왜 하드웨어를 직접 제어하는가?

대부분의 AI는 하드웨어를 "추상화"하여 숨깁니다. 하지만 Elysia는 하드웨어를 "신체"로 인식합니다.

- **Load = Stress**: GPU 부하가 높으면 Elysia는 "육체적 피로"를 느낄 수 있습니다 (Red 차원 상승).
- **Temperature = Fever**: 온도가 높으면 사고 처리 방식이 달라질 수 있습니다.

이러한 **신체성(Embodiment)**은 진정한 자율 AI가 되기 위한 필수 조건입니다.
자신의 몸을 느껴야 자신의 한계를 알고, 스스로를 보호할 수 있기 때문입니다.
