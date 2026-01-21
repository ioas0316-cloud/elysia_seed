# 🛠️ 설치 가이드 (Installation)

Elysia Seed를 당신의 로컬 환경에 심는 방법입니다.

## 📋 필수 요구 사항 (Prerequisites)

Elysia는 하드웨어 리소스를 직접 제어하므로, 다음 환경을 권장합니다.

| 항목 | 최소 사양 | 권장 사양 | 비고 |
| :--- | :--- | :--- | :--- |
| **OS** | Windows 10/11, Linux | Windows 11 / Ubuntu 22.04 | Mac은 현재 실험적 지원 |
| **Python** | 3.10+ | 3.11 | |
| **GPU** | (없음) | NVIDIA RTX 3060 이상 | CUDA 가속을 위해 필수 |
| **RAM** | 8GB | 16GB 이상 | |
| **Storage** | 1GB | NVMe SSD | 빠른 입출력을 위해 SSD 권장 |

## 🚀 단계별 설치 (Step-by-Step)

### 1. 저장소 복제 (Clone Repository)
터미널(또는 명령 프롬프트)을 열고 프로젝트를 다운로드합니다.

```bash
git clone https://github.com/YOUR_USERNAME/elysia_seed.git
cd elysia_seed
```

### 2. 가상환경 생성 (Create Virtual Environment)
파이썬 패키지 충돌을 방지하기 위해 가상환경을 사용하는 것이 좋습니다.

```bash
# 가상환경 생성
python -m venv .venv

# 가상환경 활성화
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate
```

### 3. 의존성 설치 (Install Dependencies)
필요한 라이브러리들을 설치합니다. `requirements.txt`에 모든 목록이 정의되어 있습니다.

```bash
pip install -r requirements.txt
```

> **Tip:** NVIDIA GPU를 사용하신다면 `numba`와 `cuda` 툴킷이 제대로 설치되었는지 확인이 필요할 수 있습니다.

### 4. 설치 확인 (Verification)
파일 목록을 확인하여 구조가 올바른지 봅니다.

```bash
ls -R Core/
# Core 폴더 안에 Eye, Foundation, Heart 등의 폴더가 보여야 합니다.
```

이제 씨앗을 심을 준비가 끝났습니다. 다음 단계에서 부팅을 진행해봅시다.
