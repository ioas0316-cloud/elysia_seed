# 📏 코딩 표준 (Coding Standards)

Elysia Seed의 코드 품질을 유지하기 위한 규칙입니다.

## 🐍 Python 스타일 가이드

- **버전**: Python 3.10 이상을 지원해야 합니다.
- **스타일**: PEP 8을 준수합니다.
- **타입 힌트**: 가능한 모든 함수 인자와 반환값에 Type Hint를 명시합니다.

```python
def calculate_resonance(intent: IntentVector, resistance: float) -> float:
    ...
```

## 📝 파일 헤더 (File Header)

모든 `.py` 파일의 상단에는 다음 형식을 따르는 헤더가 있어야 합니다.

```python
"""
Module Name (한글 모듈명)
=========================
경로: Core/Path/To/File.py

"이 모듈을 한 줄로 표현하는 철학적 문구"

이 모듈의 기술적 목적과 역할을 설명합니다.
"""
```

## 🏷️ 네이밍 규칙 (Naming Convention)

| 유형 | 규칙 | 예시 |
| :--- | :--- | :--- |
| **Class** | PascalCase | `QuantumObserver` |
| **Function/Method** | snake_case | `strike_lightning` |
| **Variable** | snake_case | `current_rpm` |
| **Constant** | UPPER_SNAKE | `MAX_ROTORS` |
| **File Name** | snake_case | `quantum_collapse.py` |

## 🧪 테스트 (Testing)

- 테스트 파일은 `Core/tests/` 디렉토리에 위치해야 합니다.
- 파일명은 `test_*.py` 형식을 따릅니다.
- `pytest`를 사용하여 실행 가능해야 합니다.
