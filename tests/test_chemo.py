from elysia_engine.chemo import map_chemo


def test_map_chemo_known_tag():
    sig = map_chemo("vanilla")
    assert sig.soul.frequency == 432.0
    assert sig.soul.amplitude > 0
    assert "vanilla" in sig.note


def test_map_chemo_unknown_tag_hash():
    sig1 = map_chemo("mystery_tag")
    sig2 = map_chemo("mystery_tag")
    assert sig1.soul.frequency == sig2.soul.frequency  # deterministic hash
    assert sig1.soul.frequency >= 200.0
