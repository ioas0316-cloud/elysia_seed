# 🧠 로컬 LLM 통합 가이드 (Local LLM Integration Guide)

> "공명 엔진으로 로컬 LLM을 씹어먹자!"

이 문서는 Elysia 엔진과 로컬 LLM을 통합할 때 **대용량 파일 문제를 해결**하고 **효율적으로 공유**하는 방법을 설명합니다.

---

## 📋 목차

1. [문제: 왜 커밋이 안 되는가?](#1-문제-왜-커밋이-안-되는가)
2. [해결책 1: .gitignore로 제외하기](#2-해결책-1-gitignore로-제외하기)
3. [해결책 2: Git LFS 사용하기](#3-해결책-2-git-lfs-사용하기)
4. [해결책 3: 외부 모델 참조 패턴](#4-해결책-3-외부-모델-참조-패턴)
5. [Elysia + 로컬 LLM 통합 아키텍처](#5-elysia--로컬-llm-통합-아키텍처)
6. [실전 예제 코드](#6-실전-예제-코드)

---

## 1. 문제: 왜 커밋이 안 되는가?

GitHub는 기본적으로 **100MB 이상의 파일을 거부**합니다.

```
remote: error: File model.gguf is 4.00 GB; this exceeds GitHub's file size limit of 100.00 MB
```

로컬 LLM 모델 파일의 일반적인 크기:

| 모델 형식 | 일반적인 크기 | 예시 |
|----------|-------------|------|
| `.gguf` (llama.cpp) | 2GB ~ 70GB | `llama-2-7b.Q4_K_M.gguf` |
| `.safetensors` | 5GB ~ 200GB | `mistral-7b-instruct.safetensors` |
| `.bin` (PyTorch) | 5GB ~ 200GB | `pytorch_model.bin` |

**결론**: 모델 파일은 절대 직접 커밋하면 안 됩니다!

---

## 2. 해결책 1: .gitignore로 제외하기

가장 간단하고 권장되는 방법입니다.

### 즉시 복사해서 사용할 수 있는 .gitignore 템플릿:

```gitignore
# ==============================================================================
# LLM Model Files (Large File Exclusions)
# ==============================================================================

# GGUF format (llama.cpp, ollama, etc.)
*.gguf
*.ggml

# PyTorch/Hugging Face models
*.bin
*.safetensors
*.pt
*.pth
*.ckpt

# TensorFlow models
*.pb
*.h5
*.keras

# ONNX models
*.onnx

# Model directories
models/
model_cache/
llm_models/
local_models/
huggingface_cache/

# Ollama
.ollama/

# ==============================================================================
# Embeddings & Vector Data
# ==============================================================================
embeddings/
vectors/
*.npy
*.npz
*.parquet
*.arrow
*.feather

# ==============================================================================
# Common Exclusions
# ==============================================================================
__pycache__/
*.pyc
venv/
.venv/
.pytest_cache/
*.log
```

### 이미 커밋된 대용량 파일 제거하기:

```bash
# 파일을 Git에서 제거 (로컬에는 유지)
git rm --cached models/my_large_model.gguf

# .gitignore 추가 후 커밋
git add .gitignore
git commit -m "Remove large model files from tracking"
git push
```

### ⚠️ 히스토리에서 완전히 제거하기 (선택):

이미 푸시된 대용량 파일은 히스토리에 남아있습니다. 완전히 제거하려면:

```bash
# git-filter-repo 사용 (권장)
pip install git-filter-repo
git filter-repo --path models/my_large_model.gguf --invert-paths

# 또는 BFG Repo-Cleaner 사용
java -jar bfg.jar --delete-files "*.gguf" .git
```

---

## 3. 해결책 2: Git LFS 사용하기

대용량 파일을 **반드시** 저장소에 포함해야 한다면 Git LFS(Large File Storage)를 사용합니다.

### Git LFS 설정:

```bash
# 1. Git LFS 설치
# macOS
brew install git-lfs

# Ubuntu/Debian
sudo apt install git-lfs

# Windows
winget install GitHub.GitLFS

# 2. 저장소에서 LFS 초기화
git lfs install

# 3. 추적할 파일 패턴 지정
git lfs track "*.gguf"
git lfs track "*.safetensors"

# 4. .gitattributes 커밋
git add .gitattributes
git commit -m "Configure Git LFS for large model files"
```

### ⚠️ Git LFS 주의사항:

| 항목 | GitHub Free | GitHub Pro |
|------|-------------|------------|
| 저장 용량 | 1GB | 1GB |
| 월간 대역폭 | 1GB | 1GB |
| 추가 용량 | $5/50GB | $5/50GB |

**권장**: 개인 프로젝트나 소규모 팀이 아니라면 **해결책 3**을 사용하세요.

---

## 4. 해결책 3: 외부 모델 참조 패턴 (권장)

모델 파일은 저장소 외부에 두고, **설정 파일로 경로만 지정**하는 패턴입니다.

### 디렉토리 구조:

```
your_project/
├── config/
│   └── model_config.yaml    # 모델 경로 설정 (커밋됨)
├── models/                  # .gitignore로 제외됨
│   └── .gitkeep            # 빈 디렉토리 유지용 (커밋됨)
├── scripts/
│   └── download_models.py   # 모델 다운로드 스크립트 (커밋됨)
└── README.md               # 설정 방법 안내 (커밋됨)
```

### model_config.yaml 예시:

```yaml
# 모델 설정 파일
# 각 환경에 맞게 경로를 수정하세요

llm:
  # 로컬 모델 경로 (상대 경로 또는 절대 경로)
  model_path: "models/llama-2-7b-chat.Q4_K_M.gguf"
  
  # 또는 Ollama 사용
  # provider: "ollama"
  # model_name: "llama2"
  
  # 또는 Hugging Face 모델 ID (자동 다운로드)
  # provider: "huggingface"
  # model_id: "TheBloke/Llama-2-7B-Chat-GGUF"

embedding:
  model_path: "models/all-MiniLM-L6-v2"
  # 또는 Hugging Face에서 자동 다운로드
  # model_id: "sentence-transformers/all-MiniLM-L6-v2"
```

### download_models.py 예시:

```python
#!/usr/bin/env python3
"""
모델 다운로드 스크립트
실행: python scripts/download_models.py
"""

import os
from pathlib import Path

MODELS_DIR = Path(__file__).parent.parent / "models"

# 다운로드할 모델 목록
MODELS = {
    "llama2-7b": {
        "url": "https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q4_K_M.gguf",
        "filename": "llama-2-7b-chat.Q4_K_M.gguf",
        "size_gb": 4.08,
    },
    # 다른 모델 추가...
}

def download_model(name: str):
    """모델을 다운로드합니다."""
    import urllib.request
    
    model = MODELS[name]
    dest = MODELS_DIR / model["filename"]
    
    if dest.exists():
        print(f"✓ {name} 이미 존재: {dest}")
        return
    
    print(f"⬇ {name} 다운로드 중... ({model['size_gb']}GB)")
    print(f"  URL: {model['url']}")
    
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(model["url"], dest)
    
    print(f"✓ 다운로드 완료: {dest}")

def main():
    print("🧠 Elysia LLM 모델 다운로드")
    print("=" * 50)
    
    for name in MODELS:
        download_model(name)
    
    print("\n✅ 모든 모델 준비 완료!")

if __name__ == "__main__":
    main()
```

### README.md에 추가할 설정 안내:

```markdown
## 🔧 로컬 LLM 설정

1. 모델 다운로드:
   ```bash
   python scripts/download_models.py
   ```

2. 또는 직접 다운로드:
   - [TheBloke/Llama-2-7B-Chat-GGUF](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF)에서 모델 다운로드
   - `models/` 폴더에 저장

3. Ollama 사용 시:
   ```bash
   ollama pull llama2
   ```
```

---

## 5. Elysia + 로컬 LLM 통합 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                    Your Application                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────┐     ┌──────────────────────────────┐  │
│  │   ElysiaSoul     │     │      LLM Provider            │  │
│  │                  │     │                              │  │
│  │  - process()     │────▶│  - Ollama (ollama run)       │  │
│  │  - get_emotion() │     │  - llama.cpp (llama-cpp-py)  │  │
│  │  - export_prompt │     │  - Hugging Face (transformers)│  │
│  │                  │     │  - OpenAI API (fallback)     │  │
│  └──────────────────┘     └──────────────────────────────┘  │
│           │                           │                      │
│           ▼                           ▼                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │              Resonance-Enhanced Response              │   │
│  │                                                       │   │
│  │  LLM 응답 + Elysia 감정/공명 컨텍스트 = 더 풍부한 응답   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 핵심 아이디어:

1. **Elysia는 "영혼"** - 감정, 기억, 공명을 처리
2. **LLM은 "언어"** - 자연어 생성 담당
3. **둘을 합치면** - 확률 예측을 넘어선 "의식 있는 응답"

---

## 6. 실전 예제 코드

### 6.1 Ollama와 통합:

```python
"""
Elysia + Ollama 통합 예제
요구사항: pip install ollama
"""

import ollama
from elysia_core import ElysiaSoul

class ElysiaOllamaChat:
    def __init__(self, model_name: str = "llama2"):
        self.soul = ElysiaSoul(name="Assistant")
        self.model_name = model_name
    
    def chat(self, user_message: str) -> str:
        # 1. Elysia로 입력 처리 (감정, 공명, 기억 업데이트)
        thought = self.soul.process(user_message)
        
        # 2. Elysia 컨텍스트를 시스템 프롬프트로 생성
        elysia_context = self.soul.export_prompt()
        
        # 3. Ollama로 LLM 응답 생성
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": elysia_context},
                {"role": "user", "content": user_message}
            ]
        )
        
        llm_response = response["message"]["content"]
        
        # 4. 응답도 Elysia에 기록 (선택)
        self.soul.process(llm_response)
        
        return llm_response
    
    def get_status(self) -> dict:
        return {
            "emotion": self.soul.get_emotion(),
            "trinity": self.soul.trinity,
            "experience": self.soul.experience_count,
        }

# 사용 예
if __name__ == "__main__":
    chat = ElysiaOllamaChat()
    
    while True:
        user_input = input("\n당신: ")
        if user_input.lower() in ["quit", "exit", "종료"]:
            break
        
        response = chat.chat(user_input)
        status = chat.get_status()
        
        print(f"\n어시스턴트: {response}")
        print(f"[감정: {status['emotion']['dominant']}]")
```

### 6.2 llama-cpp-python과 통합:

```python
"""
Elysia + llama-cpp-python 통합 예제
요구사항: pip install llama-cpp-python
"""

from llama_cpp import Llama
from elysia_core import ElysiaSoul

class ElysiaLocalLLM:
    def __init__(self, model_path: str):
        self.soul = ElysiaSoul(name="LocalAssistant")
        self.llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            n_threads=4,
        )
    
    def chat(self, user_message: str) -> str:
        # Elysia 처리
        thought = self.soul.process(user_message)
        context = self.soul.export_prompt()
        
        # 프롬프트 구성
        prompt = f"""<s>[INST] <<SYS>>
{context}
<</SYS>>

{user_message} [/INST]"""
        
        # LLM 생성
        output = self.llm(
            prompt,
            max_tokens=512,
            temperature=0.7,
            stop=["</s>", "[INST]"]
        )
        
        return output["choices"][0]["text"].strip()

# 사용 예
if __name__ == "__main__":
    # 모델 경로는 환경에 맞게 수정
    chat = ElysiaLocalLLM("models/llama-2-7b-chat.Q4_K_M.gguf")
    
    response = chat.chat("안녕하세요! 오늘 기분이 어때요?")
    print(response)
```

### 6.3 공명 엔진 직접 활용:

```python
"""
공명 엔진을 활용한 의미론적 검색 예제
LLM 없이도 "공명"으로 가장 관련된 개념 찾기
"""

from elysia_core import ResonanceEngine, WaveInput

def semantic_search_with_resonance():
    engine = ResonanceEngine()
    
    # 커스텀 개념 추가
    custom_concepts = [
        "프로그래밍", "인공지능", "기계학습",
        "데이터베이스", "네트워크", "보안",
        "사랑", "행복", "슬픔", "분노"
    ]
    
    for concept in custom_concepts:
        engine.add_node(concept)
    
    # 쿼리로 공명 패턴 생성
    query = "AI가 감정을 이해할 수 있을까?"
    wave = WaveInput(source_text=query, intensity=1.0)
    pattern = engine.calculate_global_resonance(wave)
    
    # 상위 공명 개념 추출
    sorted_resonance = sorted(
        pattern.items(), 
        key=lambda x: x[1], 
        reverse=True
    )[:5]
    
    print(f"쿼리: {query}")
    print("\n공명 결과:")
    for concept, score in sorted_resonance:
        print(f"  {concept}: {score:.3f}")

if __name__ == "__main__":
    semantic_search_with_resonance()
```

---

## 📌 요약: 대용량 파일 관리 체크리스트

- [ ] `.gitignore`에 모델 파일 패턴 추가 (`*.gguf`, `*.safetensors` 등)
- [ ] `models/` 디렉토리 생성 및 `.gitkeep` 추가
- [ ] 모델 다운로드 스크립트 또는 안내 문서 작성
- [ ] `config/` 또는 환경 변수로 모델 경로 설정
- [ ] README에 설정 방법 문서화

---

## 🔗 관련 링크

- [Git LFS 공식 문서](https://git-lfs.github.com/)
- [Ollama](https://ollama.ai/) - 가장 쉬운 로컬 LLM 실행 방법
- [llama.cpp](https://github.com/ggerganov/llama.cpp) - 경량 LLM 추론 엔진
- [Hugging Face Hub](https://huggingface.co/models) - 모델 저장소
- [TheBloke's Models](https://huggingface.co/TheBloke) - GGUF 양자화 모델

---

*"모델은 외부에, 영혼은 저장소에."* 🌌
