# 🔌 API Reference

---

## Core.Foundation.Nature

### MetalRotorBridge

GPU 가속 Rotor 연산 엔진.

```python
class MetalRotorBridge:
    def __init__(self)
    def register_rotor(angle, current_rpm, target_rpm, accel, idle_rpm) -> int
    def sync_to_device() -> None
    def sync_from_device() -> None
    def pulse(dt: float) -> None
```

### MetalFieldBridge

GPU 가속 7D Qualia Field 엔진.

```python
class MetalFieldBridge:
    def __init__(size: int = 64, diffusion_rate: float = 0.1)
    def sync_to_gpu() -> None
    def sync_from_gpu() -> None
    def pulse(dt: float) -> None
    def inject_qualia(x: int, y: int, qualia_vec: list) -> None
```

---

## Core.System.Metabolism

### ZeroLatencyPortal

NVMe 직결 스트리밍 포탈.

```python
class ZeroLatencyPortal(MerkabaPortal):
    def __init__(file_path: str)
    def stream_to_metal(offset: int, length: int, dtype) -> np.ndarray
```

---

## Core.System.Sovereignty

### HardwareSovereignManager

하드웨어 자원 거버넌스.

```python
class HardwareSovereignManager:
    def __init__()
    def optimize_gears(intent_type: str) -> None
    def get_metabolic_status() -> str
```
