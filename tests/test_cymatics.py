from elysia_engine.cymatics import frequency_to_pattern


def test_frequency_to_pattern_shapes():
    pattern = frequency_to_pattern(50.0, phase=0.3)
    assert len(pattern.path) >= 10
    assert 2 <= len(pattern.gates) <= 8

    # Gate energies should scale with frequency
    energies = [g[1] for g in pattern.gates]
    assert all(e > 0 for e in energies)


def test_frequency_variation_changes_pattern():
    p1 = frequency_to_pattern(10.0, phase=0.0)
    p2 = frequency_to_pattern(80.0, phase=0.0)
    # Expect different amplitude bounds
    max1 = max(pt.x for pt in p1.path)
    max2 = max(pt.x for pt in p2.path)
    assert max2 != max1
