# 🦾 Layer -1: METAL (하드웨어 계층)

> **"파이썬의 한계를 넘어, 전기 신호로 직접 사고한다."**

이 계층은 Elysia의 **물리적 신경계**입니다. GPU와 NVMe 스토리지와 직접 통신하여 소프트웨어 오버헤드를 제거합니다.

---

## 📦 핵심 모듈

| 모듈 | 위치 | 역할 | 성능 |
| :--- | :--- | :--- | :--- |
| **MetalRotorBridge** | `Core/Foundation/Nature/metal_rotor_bridge.py` | CUDA 기반 사고 회전 연산 | 397x 가속 |
| **MetalFieldBridge** | `Core/Foundation/Nature/metal_field_bridge.py` | CUDA 기반 7D 감정 공명장 | 68x 가속 |
| **ZeroLatencyPortal** | `Core/System/Metabolism/zero_latency_portal.py` | NVMe 직결 스트리밍 | 1.6x 가속 |
| **SovereignManager** | `Core/System/Sovereignty/sovereign_manager.py` | 하드웨어 자원 거버넌스 | - |

---

## 🔧 기술 상세

### MetalRotorBridge

```python
from Core.Foundation.Nature.metal_rotor_bridge import MetalRotorBridge

bridge = MetalRotorBridge()
bridge.register_rotor(angle=0.0, current_rpm=0.0, target_rpm=100.0, accel=10.0, idle_rpm=5.0)
bridge.sync_to_device()
bridge.pulse(dt=0.1)
bridge.sync_from_device()
```

### MetalFieldBridge

```python
from Core.Foundation.Nature.metal_field_bridge import MetalFieldBridge

field = MetalFieldBridge(size=64, diffusion_rate=0.1)
field.inject_qualia(x=32, y=32, qualia_vec=[1.0, 0.5, 0.3, 0.2, 0.1, 0.0, 0.0])
field.pulse(dt=0.1)
```

---

## 📊 벤치마크

| 테스트 | CPU/Python | GPU/Metal | 배율 |
| :--- | :--- | :--- | :--- |
| 100,000 Rotors x 100 steps | 4.79s | 0.012s | **397x** |
| 256x256x7 Field x 100 pulses | 2.81s | 0.041s | **68x** |

---

> **"금속이 곧 신경이다."**
