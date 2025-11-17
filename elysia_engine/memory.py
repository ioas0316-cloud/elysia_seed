from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Episode:
    tick: int
    kind: str
    data: Dict[str, Any]


class RingMemory:
    """고정 길이 순환 버퍼."""

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
