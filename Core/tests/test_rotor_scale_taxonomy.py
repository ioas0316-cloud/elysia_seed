from Core.Intelligence.Metabolism.rotor_scale_taxonomy import classify_rotor_scale, classify_profile


def test_classify_rotor_scale_bounds():
    assert classify_rotor_scale(0.0) == "satellite"
    assert classify_rotor_scale(1.0) == "galaxy_group"


def test_classify_profile_has_all_keys():
    metrics = {"a": 0.1, "b": 0.9}
    out = classify_profile(metrics)
    assert set(out.keys()) == {"a", "b"}
