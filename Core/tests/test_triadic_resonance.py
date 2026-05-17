from Core.Intelligence.Metabolism.triadic_resonance import TriadicResonanceEngine


def test_triadic_resonance_scores_in_range():
    engine = TriadicResonanceEngine()
    out = engine.evaluate([0.1, 0.2, 0.3], [0.12, 0.25, 0.28], [0.11, 0.22, 0.31])
    for key in ["phase_resonance", "cognitive_joy", "triadic_alignment"]:
        assert 0.0 <= out[key] <= 1.0


def test_triadic_resonance_empty_streams():
    engine = TriadicResonanceEngine()
    out = engine.evaluate([], [], [])
    assert out == {"phase_resonance": 0.0, "cognitive_joy": 0.0, "triadic_alignment": 0.0}
