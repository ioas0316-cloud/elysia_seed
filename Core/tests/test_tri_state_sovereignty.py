from Core.Intelligence.Metabolism.tri_state_sovereignty import TriStateSovereigntyEngine


def test_tri_state_outputs_in_range():
    engine = TriStateSovereigntyEngine(expansion_gain=1.3, stability_bias=0.72)
    out = engine.evaluate(0.8, 0.6, 0.7)
    for k in [
        "defined_world",
        "undefined_world",
        "boundary_self",
        "freedom_expansion",
        "sovereign_stability",
        "balance_gate",
    ]:
        assert 0.0 <= out[k] <= 1.0


def test_tri_state_balance_prefers_stability_bias():
    hi = TriStateSovereigntyEngine(stability_bias=0.9).evaluate(0.7, 0.7, 0.8)
    lo = TriStateSovereigntyEngine(stability_bias=0.2).evaluate(0.7, 0.7, 0.8)
    assert hi["sovereign_stability"] >= lo["sovereign_stability"]
