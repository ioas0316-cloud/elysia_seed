from __future__ import annotations

import json
from typing import Any, Dict


def publish(snapshot: Dict[str, Any]) -> str:
    """Godot/WebSocket으로 보낼 직렬화된 메시지 템플릿."""

    payload = {
        "type": "elysia_snapshot",
        "tick": snapshot.get("tick"),
        "time": snapshot.get("time"),
        "entities": snapshot.get("entities", []),
    }
    message = json.dumps(payload)
    # 실제 전송은 사용자가 구현. 여기서는 직렬화된 문자열을 반환.
    return message
