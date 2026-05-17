from __future__ import annotations

from typing import Any, Dict, List

REQUIRED_ENVELOPE_FIELDS = {
    "event_id",
    "event_type",
    "event_version",
    "source_domain",
    "payload",
    "created_at",
}

ALLOWED_EVENT_TYPES = {
    "axis.selected",
    "axis.frozen",
    "projection.rotated",
    "wave.spawned",
    "wave.propagated",
    "wave.interfered",
    "wave.collapsed",
}

REQUIRED_PAYLOAD_KEYS = {
    "anchor_id",
    "trace_id",
    "axis_profile",
}


def validate_event(event: Dict[str, Any]) -> List[str]:
    errors: List[str] = []

    missing = REQUIRED_ENVELOPE_FIELDS.difference(event.keys())
    if missing:
        errors.append(f"missing_envelope_fields={sorted(missing)}")
        return errors

    event_type = event["event_type"]
    if event_type not in ALLOWED_EVENT_TYPES:
        errors.append(f"unregistered_event_type={event_type}")

    if event.get("event_version") != "v1":
        errors.append(f"invalid_event_version={event.get('event_version')}")

    payload = event.get("payload", {})
    if not isinstance(payload, dict):
        errors.append("payload_not_object")
        return errors

    missing_payload = REQUIRED_PAYLOAD_KEYS.difference(payload.keys())
    if missing_payload:
        errors.append(f"missing_payload_fields={sorted(missing_payload)}")

    return errors
