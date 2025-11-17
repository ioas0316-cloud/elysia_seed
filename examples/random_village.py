from __future__ import annotations

import argparse
import json
import random
from pathlib import Path
from typing import Dict, List

CLASS_DEFAULTS: Dict[str, Dict[str, float]] = {
    "warrior": {"body": 0.60, "soul": 0.25, "spirit": 0.15},
    "guardian": {"body": 0.55, "soul": 0.35, "spirit": 0.10},
    "swordsman": {"body": 0.65, "soul": 0.25, "spirit": 0.10},
    "lancer": {"body": 0.62, "soul": 0.23, "spirit": 0.15},
    "berserker": {"body": 0.70, "soul": 0.15, "spirit": 0.15},
    "wizard": {"body": 0.20, "soul": 0.60, "spirit": 0.20},
    "alchemist": {"body": 0.25, "soul": 0.55, "spirit": 0.20},
    "illusionist": {"body": 0.20, "soul": 0.55, "spirit": 0.25},
    "scholar": {"body": 0.15, "soul": 0.65, "spirit": 0.20},
    "elementalist": {"body": 0.25, "soul": 0.55, "spirit": 0.20},
    "priest": {"body": 0.20, "soul": 0.30, "spirit": 0.50},
    "paladin": {"body": 0.40, "soul": 0.20, "spirit": 0.40},
    "druid": {"body": 0.25, "soul": 0.25, "spirit": 0.50},
    "oracle": {"body": 0.10, "soul": 0.25, "spirit": 0.65},
    "monk": {"body": 0.30, "soul": 0.20, "spirit": 0.50},
    "rogue": {"body": 0.55, "soul": 0.30, "spirit": 0.15},
    "shadow": {"body": 0.50, "soul": 0.30, "spirit": 0.20},
    "ranger": {"body": 0.50, "soul": 0.35, "spirit": 0.15},
    "assassin": {"body": 0.60, "soul": 0.20, "spirit": 0.20},
    "operative": {"body": 0.45, "soul": 0.40, "spirit": 0.15},
    "merchant": {"body": 0.30, "soul": 0.55, "spirit": 0.15},
    "broker": {"body": 0.25, "soul": 0.60, "spirit": 0.15},
    "caravan_master": {"body": 0.35, "soul": 0.50, "spirit": 0.15},
    "smuggler": {"body": 0.40, "soul": 0.45, "spirit": 0.15},
    "banker": {"body": 0.25, "soul": 0.50, "spirit": 0.25},
    "noble": {"body": 0.25, "soul": 0.35, "spirit": 0.40},
    "diplomat": {"body": 0.20, "soul": 0.55, "spirit": 0.25},
    "governor": {"body": 0.30, "soul": 0.30, "spirit": 0.40},
    "envoy": {"body": 0.20, "soul": 0.50, "spirit": 0.30},
    "heir": {"body": 0.25, "soul": 0.35, "spirit": 0.40},
    "blacksmith": {"body": 0.50, "soul": 0.35, "spirit": 0.15},
    "engineer": {"body": 0.35, "soul": 0.50, "spirit": 0.15},
    "architect": {"body": 0.30, "soul": 0.45, "spirit": 0.25},
    "weaver": {"body": 0.25, "soul": 0.55, "spirit": 0.20},
    "artificer": {"body": 0.35, "soul": 0.40, "spirit": 0.25},
}

CLASS_LIST: List[str] = list(CLASS_DEFAULTS.keys())

NAMES = [
    "Aren", "Bryn", "Caro", "Dain", "Ela", "Faris", "Garo", "Hina",
    "Isla", "Jory", "Kallen", "Lysa", "Marek", "Nora", "Orin", "Pavel",
    "Quen", "Riva", "Soren", "Talia", "Ulan", "Vessa", "Wyre", "Xara",
    "Yunis", "Zale", "Ilya", "Mira", "Loren", "Kira", "Daro", "Ember",
    "Rugo", "Sela", "Thane", "Verris"
]


def random_weights(base: Dict[str, float], noise: float) -> Dict[str, float]:
    values = {k: max(0.0, base[k] + random.uniform(-noise, noise)) for k in base}
    total = sum(values.values())
    if total == 0:
        total = 1.0
    return {k: round(v / total, 4) for k, v in values.items()}


def generate(size: int, noise: float) -> Dict[str, List[Dict[str, object]]]:
    villagers: List[Dict[str, object]] = []
    for idx in range(size):
        job = random.choice(CLASS_LIST)
        base = CLASS_DEFAULTS[job]
        weights = random_weights(base, noise)
        name = f"{random.choice(NAMES)} {random.choice(['of Dawn','Stone','Vale','Mire','Grove','Harbor'])}".strip()
        villagers.append(
            {
                "id": f"villager_{idx:02d}",
                "name": name,
                "class": job,
                "weights": weights,
            }
        )
    return {"villagers": villagers}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a random village roster")
    parser.add_argument("--size", type=int, default=30)
    parser.add_argument("--noise", type=float, default=0.05)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--out", type=Path, default=Path("village.json"))
    args = parser.parse_args()

    random.seed(args.seed)
    data = generate(args.size, args.noise)
    args.out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved {args.size} villagers to {args.out}")


if __name__ == "__main__":
    main()
