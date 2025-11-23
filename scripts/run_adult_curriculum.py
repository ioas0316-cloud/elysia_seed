"""
Adult-level curriculum runner (lightweight).

- Loads data/curriculum/adult_curriculum.json
- Prints scenarios with intent/goals to guide manual or scripted runs
- No external deps required.
"""
from __future__ import annotations

import json
from pathlib import Path


def load_curriculum(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    return data


def display_curriculum(data: dict) -> None:
    print(f"[Curriculum] version={data.get('version')} summary={data.get('summary')}")
    for scenario in data.get("scenarios", []):
        print(f"\n=== Scenario: {scenario.get('id')} ===")
        print(f"Intent: {scenario.get('intent')}")
        for step in scenario.get("steps", []):
            role = step.get("role")
            text = step.get("text")
            goal = step.get("goal")
            if text:
                print(f" {role:9s}: {text}")
            if goal:
                print(f"   goal    : {goal}")


def main() -> None:
    path = Path("data/curriculum/adult_curriculum.json")
    if not path.exists():
        raise SystemExit(f"Curriculum file not found: {path}")
    data = load_curriculum(path)
    display_curriculum(data)


if __name__ == "__main__":
    main()
