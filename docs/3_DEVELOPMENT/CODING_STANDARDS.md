# 📏 Coding Standards

---

## 🐍 Python

| 항목 | 규칙 |
| :--- | :--- |
| **버전** | 3.10+ |
| **스타일** | PEP 8 |
| **타입 힌트** | 권장 |
| **Docstring** | Google 스타일 |

---

## 📝 파일 헤더

모든 `.py` 파일 상단에 목적 기술:

```python
"""
Module Name (한글명)
====================
경로: Core/...

"철학적 한 줄"

이 모듈의 목적과 역할을 설명합니다.
"""
```

---

## 🏷️ 네이밍

| 유형 | 규칙 | 예시 |
| :--- | :--- | :--- |
| 클래스 | PascalCase | `MetalRotorBridge` |
| 함수 | snake_case | `sync_to_device` |
| 상수 | UPPER_SNAKE | `MAX_CAPACITY` |
| 파일 | snake_case | `metal_rotor_bridge.py` |

---

## 🧪 테스트

- 위치: `Core/tests/`
- 네이밍: `test_*.py` 또는 `*_test.py`
- 실행: `pytest Core/tests/`
