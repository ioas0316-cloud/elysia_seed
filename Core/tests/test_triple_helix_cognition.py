from Core.Intelligence.Metabolism.triple_helix_cognition import TripleHelixCognition


def test_triple_helix_expands_timeline():
    model = TripleHelixCognition(depth=3, growth=1.2)
    state = model.expand("sensory memory resonance", timesteps=4)

    assert state["depth"] == 3
    assert state["timesteps"] == 4
    assert len(state["timeline"]) == 4
    assert 0.0 <= state["final_coherence"] <= 1.0


def test_triple_helix_has_layered_states():
    model = TripleHelixCognition(depth=2)
    state = model.expand("abc", timesteps=2)
    for frame in state["timeline"]:
        assert len(frame["layers"]) == 2
        for layer in frame["layers"]:
            assert set(layer.keys()) == {"sense", "experience", "meaning"}
