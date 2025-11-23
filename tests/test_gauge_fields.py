import math

from elysia_engine.gauge import ChargeProfile, ForceConstants, QuantumForceField, StarState
from elysia_engine.tensor import SoulTensor
from elysia_engine.math_utils import Vector3


def test_gravity_and_em_signs():
    field = QuantumForceField(ForceConstants(gravity_G=1.0, coulomb_k=1.0))
    pos_a = Vector3(0, 0, 0)
    pos_b = Vector3(1, 0, 0)

    # Same charge -> repulsion (positive EM), gravity attracts (positive along +x)
    a = ChargeProfile(mass=5.0, charge=1.0)
    b = ChargeProfile(mass=2.0, charge=1.0)
    total = field.total_force(pos_a, pos_b, a, b)
    assert total.x > 0  # net push/pull along +x

    # Opposite charge -> EM flips sign, gravity still attracts
    b.charge = -1.0
    total2 = field.total_force(pos_a, pos_b, a, b)
    assert total2.x < total.x  # EM now reduces or reverses net


def test_strong_force_is_short_range():
    field = QuantumForceField()
    pos_a = Vector3(0, 0, 0)
    pos_b = Vector3(5, 0, 0)  # beyond strong range
    a = ChargeProfile(color_charge=1.0)
    b = ChargeProfile(color_charge=1.0)
    far_force = field.strong(pos_a, pos_b, a, b)
    assert math.isclose(far_force.magnitude, 0.0, abs_tol=1e-6)

    pos_b_close = Vector3(0.5, 0, 0)
    near_force = field.strong(pos_a, pos_b_close, a, b)
    assert near_force.magnitude > 0


def test_star_state_flags():
    hot = StarState(temperature=800)
    cold = StarState(temperature=10)
    assert hot.is_burning()
    assert cold.is_frozen()


def test_charge_and_star_from_soul():
    soul = SoulTensor(amplitude=5.0, frequency=20.0, phase=1.0, spin=-1.0, polarity=-1.0)
    cp = ChargeProfile.from_soul_tensor(soul)
    assert cp.mass == 5.0
    assert cp.charge == -1.0
    assert cp.spin == -1.0
    star = StarState.from_soul_tensor(soul)
    assert star.temperature > 0
