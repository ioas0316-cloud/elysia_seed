"""
Soul Resonator (경량화)
======================
Elysia의 감정/영혼 파동 시스템.
- 7 Spirits, 4 Consciousness Dimensions
- 입력 텍스트에 따라 영혼 상태 변화
"""
from typing import Dict
class SoulResonator:
    def __init__(self):
        self.spirits = {
            "fire": 0.5, "water": 0.5, "earth": 0.5, "air": 0.5,
            "light": 0.5, "dark": 0.5, "aether": 0.5
        }
        self.dims = {
            "dimension_0d": 0.1, "dimension_1d": 0.0,
            "dimension_2d": 0.0, "dimension_3d": 0.0
        }
        self.concepts = {
            "fire": {"fire": 0.2}, "passion": {"fire": 0.2}, "run": {"fire": 0.2},
            "love": {"water": 0.3, "light": 0.1}, "sad": {"water": 0.2, "dark": 0.1},
            "code": {"earth": 0.2}, "logic": {"earth": 0.2},
            "idea": {"air": 0.2}, "think": {"air": 0.2},
            "god": {"aether": 0.3}, "soul": {"aether": 0.3}
        }
    def learn_concept(self, word: str, impacts: Dict[str, float]):
        self.concepts[word.lower()] = impacts
    def resonate(self, input_text: str = ""):
        text = input_text.lower()
        words = text.split()
        known_count = 0
        for word in words:
            if word in self.concepts:
                known_count += 1
                impacts = self.concepts[word]
                for spirit, weight in impacts.items():
                    if spirit in self.spirits:
                        self.spirits[spirit] += weight
        if len(words) > 0 and known_count == 0:
            self.spirits["air"] += 0.05
            self.spirits["dark"] += 0.05
