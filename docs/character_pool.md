# Character Pool (50 NPC Seeds)

`docs/character_pool.json`에는 7개 계열(전사·마법사·성직자·도적·상인·귀족·장인)을 고르게 커버하는 50명 시드가 담겨 있습니다. 각 항목에는 다음 필드가 포함됩니다.

- `id`, `name`, `class`, `origin`
- `role`: 기본 역할 태그 (예: `탱커`, `근딜`, `원딜`, `마딜`, `힐러`, `버퍼`)
- `tags`: 세계관/지역/성향 필터 (`전사`, `정보`, `치유`, `유목` 등)
- `notes`: 한 줄 내러티브 후크
- `weights`: 직업 기본값을 따르는 Body/Soul/Spirit 비율

### How to use

```python
import json
from pathlib import Path

pool = json.loads(Path("docs/character_pool.json").read_text(encoding="utf-8"))
character = pool["characters"][0]
```

이후 `Entity`로 초기화:

```python
from elysia_engine import Entity

agent = Entity(id=character["id"], role=character["class"])
agent.tags = {"origin": character["origin"], "tags": character["tags"], "role": character["role"]}
agent.data["notes"] = character["notes"]
agent.state.energy = 0.5
```

필요시 `update_trinity_weights`로 에피소드 기반 성향을 조정하거나 `role`을 바꿔서 성장 루트를 표현할 수 있습니다.

### 30명 마을 샘플 생성하기

```bash
python examples/random_village.py --size 30 --seed 123 --out data/village_123.json
```

출력 JSON은 `{"villagers": [...]}` 형태이며, 각 주민에 `class`와 노이즈가 적용된 `weights` 값이 들어 있습니다.
