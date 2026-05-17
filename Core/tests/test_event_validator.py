from Core.System.Contracts.event_validator import validate_event


def test_validate_event_ok():
    event = {
        "event_id": "1",
        "event_type": "axis.selected",
        "event_version": "v1",
        "source_domain": "System",
        "payload": {
            "anchor_id": "@test",
            "trace_id": "t1",
            "axis_profile": "context_time_goal",
        },
        "created_at": "2026-01-01T00:00:00+00:00",
    }
    assert validate_event(event) == []


def test_validate_event_missing_payload():
    event = {
        "event_id": "1",
        "event_type": "axis.selected",
        "event_version": "v1",
        "source_domain": "System",
        "payload": {"anchor_id": "@test"},
        "created_at": "2026-01-01T00:00:00+00:00",
    }
    errors = validate_event(event)
    assert any("missing_payload_fields" in e for e in errors)
