from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, List, Tuple


@dataclass
class ScalarField:
    name: str
    dimensions: Tuple[int, ...]
    values: List[float] = field(default_factory=list)
    description: str = ""

    def index(self, coords: Iterable[int]) -> int:
        coord_tuple = tuple(coords)
        if len(coord_tuple) != len(self.dimensions):
            raise ValueError("Coordinate dimensionality mismatch")

        idx = 0
        stride = 1
        for size, c in zip(reversed(self.dimensions), reversed(coord_tuple)):
            idx += c * stride
            stride *= size
        return idx


class FieldRegistry:
    def __init__(self) -> None:
        self._fields: Dict[str, ScalarField] = {}

    def register(self, field: ScalarField) -> None:
        self._fields[field.name] = field

    def get(self, name: str) -> ScalarField | None:
        return self._fields.get(name)

    def sample(self, name: str, coords: Iterable[int]) -> float:
        field = self._fields.get(name)
        if field is None:
            raise KeyError(f"Field '{name}' not found")
        idx = field.index(coords)
        if idx >= len(field.values):
            raise IndexError("Coordinate outside of field data")
        return field.values[idx]

    def to_dict(self) -> Dict[str, Dict]:
        return {
            name: {
                "dimensions": field.dimensions,
                "description": field.description,
            }
            for name, field in self._fields.items()
        }
