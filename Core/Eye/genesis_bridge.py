"""
Genesis Bridge (Aesthetic Mimicry Engine)
=========================================
Core.Eye.genesis_bridge

"I see, therefore I become."

Adapted for Elysia Seed: Robust Mobile/Desktop Hybrid.
Digest visual memories into Aesthetic DNA.
"""

import os
import time
import logging
import random
import glob
from dataclasses import dataclass
from typing import Tuple

try:
    import numpy as np
    from PIL import Image
    HAS_CV = True
except ImportError:
    HAS_CV = False

logger = logging.getLogger("GenesisBridge")

@dataclass
class AestheticDNA:
    primary_color: Tuple[float, float, float]
    secondary_color: Tuple[float, float, float]
    fog_density: float
    complexity_index: float
    mood_tag: str

class GenesisBridge:
    def __init__(self, memory_path: str = "Memories/Visual/Observer"):
        self.memory_path = memory_path
        self.current_dna = AestheticDNA((0.1, 0.1, 0.1), (0.0, 0.0, 0.0), 0.5, 0.1, "Void")
        self.last_processed_file = ""
        
        # On Mobile, path might be relative to script
        os.makedirs(self.memory_path, exist_ok=True)

    def digest_latest_memory(self) -> AestheticDNA:
        """Finds the newest screenshot and extracts Aesthetic DNA."""
        try:
            files = glob.glob(os.path.join(self.memory_path, "*.png"))
            if not files:
                return self.current_dna
                
            latest_file = max(files, key=os.path.getctime)
            
            if latest_file == self.last_processed_file:
                return self.current_dna 
            
            logger.info(f"🧬 [Genesis] Digesting Memory: {os.path.basename(latest_file)}")
            self.current_dna = self._extract_features(latest_file)
            self.last_processed_file = latest_file
            
            self._manifest_dna(self.current_dna)
            return self.current_dna
            
        except Exception as e:
            logger.error(f"❌ [Genesis] Digestion Failed: {e}")
            return self.current_dna

    def _extract_features(self, image_path: str) -> AestheticDNA:
        if not HAS_CV:
            return self._mock_extraction(image_path)
            
        try:
            img = Image.open(image_path).resize((100, 100))
            arr = np.array(img)
            
            # 1. Color (Average)
            mean_color = arr.mean(axis=(0,1))
            primary = tuple(mean_color[:3] / 255.0)
            secondary = (1.0 - primary[0], 1.0 - primary[1], 1.0 - primary[2])
            
            # 2. Complexity & Fog
            gray = arr.mean(axis=2)
            complexity = float(np.std(gray) / 128.0)
            brightness = float(np.mean(gray) / 255.0)
            fog = 1.0 - brightness
            
            tag = "Serene"
            if complexity > 0.3: tag = "Chaotic"
            elif fog > 0.7: tag = "Dark"

            return AestheticDNA(primary, secondary, fog, complexity, tag)

        except Exception as e:
            logger.warning(f"⚠️ [Genesis] Feature extraction error: {e}. Using Mock.")
            return self._mock_extraction(image_path)

    def _mock_extraction(self, image_path) -> AestheticDNA:
        seed = len(image_path)
        random.seed(seed)
        r, g, b = random.random(), random.random(), random.random()
        return AestheticDNA(
            (r, g, b), (1-r, 1-g, 1-b),
            random.random(), random.random(),
            "Simulated_Dream"
        )

    def _manifest_dna(self, dna: AestheticDNA):
        logger.info(f"🎨 [Genesis] Palette: {dna.primary_color} | Mood: {dna.mood_tag}")
        self._sync_to_renderer(dna)

    def _sync_to_renderer(self, dna):
        """Writes DNA to a shared state file."""
        # Check if 'data/State' exists, create if not
        state_dir = "data/State"
        os.makedirs(state_dir, exist_ok=True)
        
        state_path = os.path.join(state_dir, "genesis_state.json")
        import json
        data = {
            "uFogColor": dna.primary_color,
            "uAmbientColor": dna.secondary_color,
            "uGeometryScale": 1.0 + dna.complexity_index,
            "uFogDensity": dna.fog_density,
            "mood": dna.mood_tag
        }
        try:
            with open(state_path, "w") as f:
                json.dump(data, f)
        except: pass
