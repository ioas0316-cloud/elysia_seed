from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import math

from .tensor import SoulTensor

@dataclass
class Episode:
    tick: int
    kind: str
    data: Dict[str, Any]
    soul_signature: Optional[SoulTensor] = None # The "Embedding" of the moment


class RingMemory:
    """고정 길이 순환 버퍼 (Short-term Working Memory)."""

    def __init__(self, capacity: int = 1024):
        self.capacity = capacity
        self.buffer: List[Episode] = []
        self._index = 0

    def add(self, episode: Episode) -> None:
        if len(self.buffer) < self.capacity:
            self.buffer.append(episode)
        else:
            self.buffer[self._index] = episode
        self._index = (self._index + 1) % self.capacity

    def to_list(self) -> List[Dict[str, Any]]:
        return [e.__dict__ for e in self.buffer]


class SemanticMemory:
    """
    Akasha: The Long-term Associative Memory.
    Stores episodes and retrieves them based on 'Semantic Gravity' (Resonance).
    Acts as a pure Python Vector Database.
    """

    def __init__(self):
        self.memories: List[Episode] = []

    def encode(self, episode: Episode) -> None:
        """
        Stores an episode into the Akashic Record.
        """
        # In a real system, we might merge similar memories or decay old ones.
        # For this engine, we just append.
        self.memories.append(episode)

    def retrieve(self, query_soul: SoulTensor, limit: int = 5, min_resonance: float = 0.0) -> List[Episode]:
        """
        Finds memories that resonate with the query soul.
        Returns a list of episodes sorted by resonance strength.
        """
        if not self.memories:
            return []

        scored_memories = []

        for mem in self.memories:
            if not mem.soul_signature:
                continue

            # Calculate Resonance
            # We use the SoulTensor.resonate method
            res_data = query_soul.resonate(mem.soul_signature)
            score = res_data["resonance"]

            # Filter by threshold
            if score >= min_resonance:
                scored_memories.append((score, mem))

        # Sort by score (descending)
        scored_memories.sort(key=lambda x: x[0], reverse=True)

        # Return top N
        return [item[1] for item in scored_memories[:limit]]

    def get_structure_summary(self) -> str:
        """Returns a description of the memory landscape."""
        count = len(self.memories)
        if count == 0:
            return "The Akasha is empty."

        return f"The Akasha holds {count} echoes of the past."
