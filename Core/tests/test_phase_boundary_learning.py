from Core.Intelligence.Metabolism.phase_boundary_learning import PhaseBoundaryLearner


def test_phase_boundary_learning_generates_timeline_and_final():
    learner = PhaseBoundaryLearner(sensitivity=0.6)
    state = learner.learn(
        inner_stream=[0.2, 0.5, 0.7, 0.4],
        outer_stream=[0.8, 0.3, 0.2, 0.6],
        timesteps=5,
    )

    assert state["timesteps"] == 5
    assert len(state["timeline"]) == 5
    assert 0.0 <= state["final"]["boundary_clarity"] <= 1.0


def test_phase_boundary_learning_handles_empty_stream():
    learner = PhaseBoundaryLearner()
    state = learner.learn([], [], timesteps=3)
    assert state["timeline"] == []
    assert state["final"]["boundary_clarity"] == 0.0
