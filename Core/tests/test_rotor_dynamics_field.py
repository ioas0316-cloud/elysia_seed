from Core.System.Metabolism.rotor_dynamics_field import RotorDynamicsField


def test_rotor_dynamics_field_evolves_with_signals():
    field = RotorDynamicsField()
    out = field.evolve([0.2, 0.7, 0.8], steps=5)
    assert len(out["trajectory"]) == 5
    assert 0.0 <= out["final_coherence"] <= 1.0
    assert 0.0 <= out["natural_selection_score"] <= 1.0


def test_rotor_dynamics_field_empty_signal_safe():
    field = RotorDynamicsField()
    out = field.evolve([], steps=4)
    assert out["trajectory"] == []
    assert out["natural_selection_score"] == 0.0
