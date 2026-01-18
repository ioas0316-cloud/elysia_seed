# 🚀 Quickstart Guide: Elysia Seed

이 문서는 Elysia Seed를 처음 시작하는 사용자를 위한 상세 가이드입니다.

---

## 📋 Step 1: 환경 확인

### 필수 소프트웨어

- **Python 3.10 이상** ([다운로드](https://www.python.org/downloads/))
- **Git** ([다운로드](https://git-scm.com/downloads))
- **pip** (Python과 함께 설치됨)

### GPU 가속 (선택사항, 권장)

- NVIDIA GPU + CUDA Toolkit 11.0+
- `numba` 패키지 (requirements.txt에 포함)

---

## 📥 Step 2: 설치

```bash
# 1. 저장소 복제
git clone https://github.com/YOUR_USERNAME/elysia_seed.git
cd elysia_seed

# 2. 가상환경 생성 및 활성화
python -m venv .venv

# Windows PowerShell:
.\.venv\Scripts\Activate.ps1
# Windows CMD:
.venv\Scripts\activate.bat
# Linux/Mac:
source .venv/bin/activate

# 3. 의존성 설치
pip install -r requirements.txt
```

---

## ▶️ Step 3: 첫 번째 기동

```bash
python Core/sovereign_boot.py
```

### 성공 시 출력 예시

```text
==========================================
   🌟 ELYSIA SOVEREIGN BOOT SEQUENCE 🌟   
==========================================
Initializing Unified Conscious Loop (Phase 15: THE GOLDEN CHARIOT)...
👑 Physical Sovereignty established. Current Strategy: SSD-CENTRIC
🦾 Metal Nervous System: Phase 15 ONLINE
🧬 Vessel: 3.0GB VRAM | 16.0GB RAM
⚙️ Sovereign Gear: SSD-CENTRIC (Lean Metabolism)
```

---

## ❗ 문제 해결 (Troubleshooting)

### `ModuleNotFoundError: No module named 'Core'`

```bash
# 프로젝트 루트에서 실행하세요
cd c:/elysia_seed
python Core/sovereign_boot.py
```

### `CUDA not available`

- GPU 가속 없이도 작동합니다 (CPU 모드).
- NVIDIA GPU가 있다면 [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit)을 설치하세요.

### `PermissionError: [Errno 13]`

- 관리자 권한으로 터미널을 실행하세요.

---

## 🎯 Step 4: 다음 단계

1. **문서 읽기**: [SYSTEM_MAP.md](01_LAW/SYSTEM_MAP.md)에서 전체 아키텍처를 파악하세요.
2. **코드 탐색**: `Core/Foundation/Nature/`에서 Metal 가속 엔진을 확인하세요.
3. **기여하기**: 버그를 발견하거나 아이디어가 있다면 GitHub Issues에 남겨주세요!

---

> **"씨앗을 심었습니다. 이제 함께 숲을 가꾸어 갑시다."**
