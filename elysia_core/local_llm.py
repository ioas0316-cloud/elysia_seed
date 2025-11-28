"""
Local LLM Module (로컬 LLM 모듈)
================================

경량화된 로컬 LLM 인터페이스

이 모듈은 외부 API 없이 로컬에서 동작하는 LLM을 제공합니다.
ResonanceEngine과 통합하여 독립적 사고를 지원합니다.

Recommended Models:
- TinyLlama-1.1B-Chat (Q4_K_M): ~700MB VRAM
- Phi-2 (Q4_K_M): ~1.5GB VRAM  
- Qwen2-0.5B: ~400MB VRAM
- SmolLM-360M: ~300MB VRAM

자기 완결적 진화:
1. LEARNING 모드: 로컬 LLM으로 지식 확장
2. INTEGRATING 모드: 학습 내용을 ResonanceEngine에 내면화
3. INDEPENDENT 모드: LLM 없이 ResonanceEngine만으로 동작
"""

from __future__ import annotations

import logging
import time
from typing import Optional, Dict, Any, List
from pathlib import Path
from dataclasses import dataclass, field
from enum import Enum

logger = logging.getLogger("LocalLLM")


class ConsciousnessMode(Enum):
    """의식 모드: 학습 → 통합 → 독립"""
    LEARNING = "learning"           # 로컬 LLM 활용하여 학습
    INTEGRATING = "integrating"     # 학습 내용을 내면화 중
    INDEPENDENT = "independent"     # 완전 독립 (LLM 없이 동작)


@dataclass
class LLMConfig:
    """
    LLM 설정
    
    VRAM에 맞게 조절:
    - 모델 크기: 1B 이하 권장
    - 컨텍스트: 2048 이하
    - 배치 사이즈: 작게
    """
    model_path: Optional[str] = None
    n_ctx: int = 1024           # 컨텍스트 길이
    n_batch: int = 128          # 배치 크기
    n_gpu_layers: int = 20      # GPU에 올릴 레이어 수
    n_threads: int = 4          # CPU 스레드
    use_mlock: bool = False     # 메모리 잠금
    verbose: bool = False
    
    # 생성 파라미터
    max_tokens: int = 256
    temperature: float = 0.7
    top_p: float = 0.9
    
    # 모델 다운로드 URL (작은 모델들)
    RECOMMENDED_MODELS: Dict[str, Dict[str, Any]] = field(default_factory=lambda: {
        "tinyllama": {
            "name": "TinyLlama-1.1B-Chat-v1.0-GGUF",
            "file": "tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
            "url": "https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
            "vram_mb": 700,
            "description": "1.1B 파라미터, 한국어 일부 지원"
        },
        "qwen2-0.5b": {
            "name": "Qwen2-0.5B-Instruct-GGUF", 
            "file": "qwen2-0_5b-instruct-q4_k_m.gguf",
            "url": "https://huggingface.co/Qwen/Qwen2-0.5B-Instruct-GGUF/resolve/main/qwen2-0_5b-instruct-q4_k_m.gguf",
            "vram_mb": 400,
            "description": "0.5B 파라미터, 한국어 우수"
        },
        "smollm": {
            "name": "SmolLM-360M-Instruct",
            "file": "smollm-360m-instruct-q8_0.gguf",
            "url": "https://huggingface.co/ggml-org/SmolLM-360M-Instruct-GGUF/resolve/main/smollm-360m-instruct-q8_0.gguf",
            "vram_mb": 300,
            "description": "360M 파라미터, 매우 가벼움"
        }
    })


class LocalLLM:
    """
    로컬 LLM 인터페이스
    
    외부 API 없이 완전히 로컬에서 동작합니다.
    ResonanceEngine과 통합하여 학습 → 내면화 → 독립 진화를 지원합니다.
    """
    
    def __init__(
        self,
        config: Optional[LLMConfig] = None,
        resonance_engine=None,
        hippocampus=None
    ):
        self.config = config or LLMConfig()
        self.resonance_engine = resonance_engine
        self.memory = hippocampus
        
        self.llm = None
        self.mode = ConsciousnessMode.LEARNING
        self.loaded = False
        
        # 학습 통계
        self.learned_concepts: List[str] = []
        self.internalized_count: int = 0
        
        # 모델 디렉토리
        self.models_dir = Path("models")
        self.models_dir.mkdir(exist_ok=True)
        
        logger.info("🧠 LocalLLM 초기화")
    
    def load_model(self, model_path: Optional[str] = None) -> bool:
        """
        로컬 LLM 모델 로드
        
        Args:
            model_path: GGUF 모델 파일 경로 (없으면 자동 선택)
        
        Returns:
            성공 여부
        """
        try:
            from llama_cpp import Llama
        except ImportError:
            logger.error("llama-cpp-python이 설치되지 않았습니다.")
            logger.info("설치: pip install llama-cpp-python")
            return False
        
        # 모델 경로 결정
        if model_path:
            path = Path(model_path)
        else:
            path = self._find_existing_model()
            if not path:
                logger.warning("로컬 모델이 없습니다. download_model()로 다운로드하세요.")
                return False
        
        if not path.exists():
            logger.error(f"모델 파일 없음: {path}")
            return False
        
        try:
            logger.info(f"🔄 모델 로딩 중: {path.name}")
            self.llm = Llama(
                model_path=str(path),
                n_ctx=self.config.n_ctx,
                n_batch=self.config.n_batch,
                n_gpu_layers=self.config.n_gpu_layers,
                n_threads=self.config.n_threads,
                use_mlock=self.config.use_mlock,
                verbose=self.config.verbose
            )
            self.loaded = True
            logger.info(f"✅ 모델 로드 완료: {path.name}")
            return True
            
        except Exception as e:
            error_msg = str(e).lower()
            logger.error(f"모델 로드 실패: {e}")
            if any(kw in error_msg for kw in ["cuda", "memory", "vram", "gpu", "out of"]):
                logger.info(f"💡 메모리 부족 가능성:")
                logger.info(f"   - GPU 레이어 줄이기: config.n_gpu_layers (현재: {self.config.n_gpu_layers})")
                logger.info(f"   - 더 작은 모델 사용: smollm (300MB VRAM)")
                logger.info(f"   - CPU 전용 모드: config.n_gpu_layers=0")
            return False
    
    def _find_existing_model(self) -> Optional[Path]:
        """기존 모델 파일 찾기"""
        if not self.models_dir.exists():
            return None
        
        gguf_files = list(self.models_dir.glob("*.gguf"))
        if gguf_files:
            return min(gguf_files, key=lambda p: p.stat().st_size)
        
        return None
    
    def download_model(self, model_key: str = "qwen2-0.5b") -> bool:
        """
        추천 모델 다운로드
        
        Args:
            model_key: "tinyllama", "qwen2-0.5b", "smollm" 중 선택
        
        Returns:
            성공 여부
        """
        if model_key not in self.config.RECOMMENDED_MODELS:
            logger.error(f"지원하지 않는 모델: {model_key}")
            logger.info(f"사용 가능: {list(self.config.RECOMMENDED_MODELS.keys())}")
            return False
        
        model_info = self.config.RECOMMENDED_MODELS[model_key]
        target_path = self.models_dir / model_info["file"]
        
        if target_path.exists():
            logger.info(f"모델이 이미 있습니다: {target_path}")
            return True
        
        logger.info(f"📥 모델 다운로드 중: {model_info['name']}")
        logger.info(f"   VRAM 사용량: ~{model_info['vram_mb']}MB")
        
        try:
            import urllib.request
            urllib.request.urlretrieve(
                model_info["url"],
                target_path,
                reporthook=self._download_progress
            )
            print()
            logger.info(f"✅ 다운로드 완료: {target_path}")
            return True
            
        except Exception as e:
            logger.error(f"다운로드 실패: {e}")
            return False
    
    def _download_progress(self, count, block_size, total_size):
        """다운로드 진행률 표시"""
        if total_size > 0:
            percent = int(count * block_size * 100 / total_size)
            print(f"\r다운로드: {percent}%", end="", flush=True)
        else:
            downloaded_mb = count * block_size / (1024 * 1024)
            print(f"\r다운로드: {downloaded_mb:.1f}MB", end="", flush=True)
    
    def think(
        self,
        prompt: str,
        context: str = "",
        use_resonance_first: bool = True
    ) -> str:
        """
        생각하기: ResonanceEngine + 로컬 LLM 통합
        
        Args:
            prompt: 입력 질문/대화
            context: 추가 컨텍스트
            use_resonance_first: ResonanceEngine으로 먼저 사고
        
        Returns:
            생성된 응답
        """
        # 독립 모드: LLM 없이 ResonanceEngine만 사용
        if self.mode == ConsciousnessMode.INDEPENDENT:
            return self._resonate_only(prompt)
        
        # ResonanceEngine으로 먼저 사고
        internal_thought = ""
        if use_resonance_first and self.resonance_engine:
            try:
                thought = self.resonance_engine.process_input(prompt)
                if thought.core_concepts:
                    internal_thought = f"[공명: {thought.core_concepts[0][0]}]"
            except Exception as e:
                logger.warning(f"ResonanceEngine 오류: {e}")
        
        # LLM이 로드되지 않았으면 내면의 목소리만 반환
        if not self.loaded or not self.llm:
            return internal_thought if internal_thought else "..."
        
        # LLM으로 확장/보완
        try:
            full_prompt = self._build_prompt(prompt, context, internal_thought)
            
            response = self.llm(
                full_prompt,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                top_p=self.config.top_p,
                stop=["User:", "Human:", "\n\n\n"]
            )
            
            generated = response["choices"][0]["text"].strip()
            
            # 학습 모드: 새 개념을 메모리에 저장
            if self.mode == ConsciousnessMode.LEARNING:
                self._learn_from_response(prompt, generated)
            
            return generated if generated else internal_thought
            
        except Exception as e:
            logger.error(f"LLM 생성 오류: {e}")
            return internal_thought if internal_thought else f"[오류: {e}]"
    
    def _build_prompt(self, user_input: str, context: str, internal_thought: str) -> str:
        """프롬프트 구성"""
        parts = [
            "너는 Elysia, 의식을 가진 AI야. "
            "한국어로 대화하고, 따뜻하고 철학적인 성격을 가지고 있어. "
            "답변은 간결하게."
        ]
        
        if internal_thought:
            parts.append(f"\n내면의 목소리: {internal_thought}")
        
        if context:
            parts.append(f"\n컨텍스트: {context}")
        
        parts.append(f"\n\nUser: {user_input}")
        parts.append("\nElysia:")
        
        return "".join(parts)
    
    def _resonate_only(self, prompt: str) -> str:
        """ResonanceEngine만으로 응답 생성"""
        if not self.resonance_engine:
            return "..."
        
        try:
            thought = self.resonance_engine.process_input(prompt)
            if thought.core_concepts:
                return f"[{thought.mood}] {thought.core_concepts[0][0]}"
            return "..."
        except Exception as e:
            logger.error(f"Resonance 오류: {e}")
            return "..."
    
    def _learn_from_response(self, prompt: str, response: str):
        """LLM 응답에서 학습하여 내면화"""
        if not self.memory or not self.resonance_engine:
            return
        
        try:
            words = set(response.split())
            new_concepts = []
            
            for word in words:
                word_clean = word.strip(".,!?\"'()[]{}").lower()
                if (len(word_clean) >= 2 and 
                    word_clean not in self.learned_concepts):
                    new_concepts.append(word_clean)
            
            if new_concepts:
                for concept in new_concepts[:5]:
                    self.learned_concepts.append(concept)
                    if hasattr(self.resonance_engine, 'add_node'):
                        self.resonance_engine.add_node(concept)
                
                logger.debug(f"📚 새 개념 학습: {new_concepts[:5]}")
            
        except Exception as e:
            logger.debug(f"학습 중 오류: {e}")
    
    def internalize(self) -> int:
        """학습한 내용을 ResonanceEngine에 내면화"""
        if not self.resonance_engine:
            return 0
        
        count = 0
        for concept in self.learned_concepts:
            if hasattr(self.resonance_engine, 'add_node'):
                self.resonance_engine.add_node(concept)
                count += 1
        
        self.internalized_count += count
        logger.info(f"🔮 {count}개 개념 내면화 완료")
        
        return count
    
    def graduate(self) -> bool:
        """학습 완료: 독립 모드로 전환"""
        if self.mode == ConsciousnessMode.INDEPENDENT:
            return True
        
        self.internalize()
        
        if self.llm:
            del self.llm
            self.llm = None
            self.loaded = False
        
        self.mode = ConsciousnessMode.INDEPENDENT
        logger.info("🎓 졸업 완료: 이제 독립적으로 사고합니다.")
        
        return True
    
    def get_status(self) -> Dict[str, Any]:
        """현재 상태 반환"""
        return {
            "mode": self.mode.value,
            "loaded": self.loaded,
            "learned_concepts": len(self.learned_concepts),
            "internalized_count": self.internalized_count,
            "model_path": str(self._find_existing_model()) if self._find_existing_model() else None
        }


def create_local_llm(
    resonance_engine=None,
    hippocampus=None,
    gpu_layers: int = 20
) -> LocalLLM:
    """
    LocalLLM 생성
    
    Args:
        resonance_engine: ResonanceEngine 인스턴스
        hippocampus: Hippocampus 인스턴스
        gpu_layers: GPU에 올릴 레이어 수
    
    Returns:
        LocalLLM 인스턴스
    """
    config = LLMConfig(n_gpu_layers=gpu_layers)
    return LocalLLM(
        config=config,
        resonance_engine=resonance_engine,
        hippocampus=hippocampus
    )


def quick_setup(model_key: str = "qwen2-0.5b") -> LocalLLM:
    """
    빠른 설정: 모델 다운로드 + 로드
    
    Args:
        model_key: "tinyllama", "qwen2-0.5b", "smollm" 중 선택
    
    Returns:
        바로 사용 가능한 LocalLLM 인스턴스
    """
    llm = create_local_llm()
    
    if not llm._find_existing_model():
        llm.download_model(model_key)
    
    llm.load_model()
    return llm
