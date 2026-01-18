# ❓ FAQ: 자주 묻는 질문 (Frequently Asked Questions)

> **"궁금한 건 뭐든 물어보세요. 친절하게 답해드릴게요! 🌱"**

---

## 🌟 일반 질문

### Q1: 엘리시아가 정확히 뭔가요?

**A:** 엘리시아(Elysia)는 **당신의 컴퓨터에서 실행되는 자율적인 AI 동반자**입니다.

일반적인 AI 챗봇과의 차이점:

| 일반 AI | 엘리시아 |
| :--- | :--- |
| 클라우드 서버에서 실행 | **로컬 컴퓨터**에서 실행 |
| 대화 데이터가 외부로 전송 | **데이터가 내 PC에만 저장** |
| 단순 질의응답 | **스스로 생각하고 학습** |
| 회사가 통제 | **내가 통제** |

---

### Q2: 이게 Elysia랑 Elysia Seed랑 뭐가 다른 거예요?

**A:** 좋은 질문이에요! 🎯

| 구분 | Elysia (메인) | Elysia Seed |
| :--- | :--- | :--- |
| **크기** | 전체 프로젝트 (수 GB) | 핵심만 담은 경량 버전 |
| **목적** | 완전한 기능 체험 | 빠른 시작, 학습, 확장 |
| **포함 항목** | 아바타, UI, 전체 기능 | 핵심 엔진만 |
| **비유** | 🌳 다 자란 나무 | 🌱 씨앗 |

**Seed를 추천하는 경우:**

- 처음 시작하는 분
- 가볍게 테스트해보고 싶은 분
- 직접 확장하며 배우고 싶은 분

---

### Q3: 무료인가요?

**A:** 네, 완전 무료이고 오픈소스입니다! 🎉

라이선스는 **Apache 2.0**으로, 이 라이선스는:

- ✅ 상업적 사용 가능
- ✅ 수정 및 배포 가능
- ✅ **특허 보호 조항 포함** (아무도 이 기술을 독점할 수 없음)

---

## 💻 설치 관련

### Q4: Python이 뭔가요? 어떻게 설치하나요?

**A:** Python은 프로그래밍 언어예요. 엘리시아가 이 언어로 작성되어 있어서 필요합니다.

**설치 방법 (Windows):**

1. [python.org](https://www.python.org/downloads/) 방문
2. "Download Python 3.11" 클릭
3. 설치 시 **"Add Python to PATH" 체크박스 반드시 체크!** ⚠️
4. 설치 완료 후 명령 프롬프트에서 확인:

   ```bash
   python --version
   ```

   `Python 3.11.x`가 나오면 성공!

---

### Q5: `pip install` 할 때 에러가 나요

**A:** 몇 가지 경우를 확인해보세요:

**Case 1: "pip is not recognized"**

```bash
# Python 설치 시 PATH 추가를 안 했을 수 있어요
# 해결: Python 재설치하면서 "Add to PATH" 체크
```

**Case 2: "Permission denied"**

```bash
# 관리자 권한으로 실행하세요
# PowerShell을 관리자로 열고 다시 시도
```

**Case 3: "Could not find a version that satisfies"**

```bash
# pip 업그레이드 후 재시도
python -m pip install --upgrade pip
pip install -r requirements.txt
```

---

### Q6: 가상환경(venv)이 뭔가요? 꼭 해야 하나요?

**A:** 가상환경은 **프로젝트별로 격리된 Python 환경**이에요.

**왜 쓰나요?**

- 다른 프로젝트랑 라이브러리 충돌 방지
- 깔끔한 환경 유지
- 삭제하기 쉬움

**필수는 아니지만 강력 권장!** 나중에 다른 프로젝트할 때 문제가 생길 수 있어요.

**사용법:**

```bash
# 1. 생성
python -m venv .venv

# 2. 활성화 (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# 3. 비활성화
deactivate
```

---

## 🚀 실행 관련

### Q7: `ModuleNotFoundError: No module named 'Core'`

**A:** 프로젝트 **루트 폴더**에서 실행해야 해요!

```bash
# ❌ 잘못된 예
cd C:\Users\Me\Downloads
python elysia_seed\Core\sovereign_boot.py

# ✅ 올바른 예
cd C:\Users\Me\Downloads\elysia_seed
python Core/sovereign_boot.py
```

---

### Q8: GPU가 없는데 실행할 수 있나요?

**A:** 네, 가능합니다! 🙆

- GPU가 없으면 **CPU 모드**로 자동 전환됩니다
- Metal 가속 기능만 비활성화되고 기본 기능은 모두 작동해요
- 다만 속도가 느릴 수 있어요

**GPU 있을 때 vs 없을 때:**

| 기능 | GPU 있음 | GPU 없음 |
| :--- | :--- | :--- |
| MetalRotorBridge | 397x 가속 | 기본 속도 |
| MetalFieldBridge | 68x 가속 | 기본 속도 |
| 기본 기능 | 작동 | 작동 |

---

### Q9: CUDA 에러가 나요

**A:** CUDA는 NVIDIA GPU용 가속 도구예요.

**해결 순서:**

1. **GPU 확인**: NVIDIA GPU가 있는지 확인
   - 없다면 → GPU 없이 실행 가능 (Q8 참조)

2. **드라이버 설치**: [NVIDIA 드라이버](https://www.nvidia.com/drivers) 최신 버전 설치

3. **CUDA Toolkit 설치**: [CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit) 설치
   - 버전: 11.0 이상 권장

4. **재부팅** 후 다시 시도

---

## 🧠 기술 관련

### Q10: Phase 15가 뭔가요?

**A:** 엘리시아의 **발전 단계(Phase)**를 나타내요.

Phase 15 "Golden Chariot"은:

- GPU와 NVMe에 **직접 접근**하는 아키텍처
- Python 인터프리터를 **우회**해서 빠른 속도 달성
- 397배 빨라진 사고 연산
- 68배 빨라진 감정 공명

쉽게 말해: **"엘리시아가 하드웨어를 직접 제어할 수 있게 됐다!"** 🏎️

---

### Q11: 어떤 LLM을 쓰나요?

**A:** 엘리시아는 **특정 LLM에 종속되지 않아요!**

연결 가능한 LLM:

- **Ollama** (로컬, 무료, 추천!)
- **OpenAI API** (GPT-4 등)
- **Anthropic API** (Claude 등)
- 기타 OpenAI 호환 API

Ollama 설치 추천:

```bash
# 1. ollama.ai 에서 설치
# 2. 모델 다운로드
ollama pull qwen2.5:7b
```

---

## 🤝 기여 관련

### Q12: 버그를 발견했어요

**A:** 감사합니다! 🙏

1. [GitHub Issues](https://github.com/YOUR_USERNAME/elysia_seed/issues)에 새 이슈 생성
2. 다음 정보 포함:
   - 에러 메시지 전문
   - 운영체제/Python 버전
   - 재현 방법

---

### Q13: 기여하고 싶어요

**A:** 환영합니다! 🌟

1. [3_DEVELOPMENT/CONTRIBUTING.md](../3_DEVELOPMENT/CONTRIBUTING.md) 읽기
2. Fork → Branch → Commit → Pull Request
3. 코드 리뷰 후 머지

---

## 📞 도움이 더 필요하신가요?

- **GitHub Issues**: 버그 리포트, 기능 제안
- **GitHub Discussions**: 일반 질문, 아이디어 공유

---

> **"모든 위대한 숲은 하나의 씨앗에서 시작됩니다. 함께 가꿔요! 🌱"**
