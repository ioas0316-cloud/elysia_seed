from Core.System.Metabolism.rotor_wave_engine import RotorWaveEngine


def test_rotor_wave_engine_emits_required_events():
    engine = RotorWaveEngine(anchor_id="@test", max_workers=3)
    result = engine.run(
        signal="parallelize this topology",
        objective="optimize convergence",
        axis_candidates=["context_time_goal", "risk_cost_intent"],
    )

    assert result["anchor_id"] == "@test"
    assert result["parallel_gain"] >= 1

    event_types = [event["event_type"] for event in engine.events]
    for required in [
        "axis.selected",
        "axis.frozen",
        "wave.spawned",
        "wave.interfered",
        "wave.collapsed",
        "projection.rotated",
        "wave.propagated",
    ]:
        assert required in event_types


def test_wave_collapsed_payload_contains_regret():
    engine = RotorWaveEngine()
    engine.run(
        signal="observe rotate freeze",
        objective="stability",
        axis_candidates=["a", "b", "c"],
    )

    collapsed = [e for e in engine.events if e["event_type"] == "wave.collapsed"]
    assert len(collapsed) == 1
    payload = collapsed[0]["payload"]
    assert "collapse_regret" in payload
    assert payload["collapse_regret"] >= 0.0
