from Core.System.Metabolism.clock_rotor import ClockRotor
from Core.System.Metabolism.persona_rotor_orchestrator import PersonaRotorOrchestrator
from Core.System.Metabolism.sovereign_arbiter import SovereignArbiter
from Core.System.Metabolism.purpose_accrual import PurposeAccrual


def test_sovereign_runtime_flow_basic_cycle():
    clock = ClockRotor()
    persona = PersonaRotorOrchestrator()
    arbiter = SovereignArbiter()
    purpose = PurposeAccrual()

    ticks = clock.spin(load=0.7, fatigue=0.2)
    p = persona.select(ticks.energy_tick, ticks.momentum_tick, ticks.recovery_tick)
    signal = purpose.update(success=0.8, resonance=0.9, fatigue=0.2)
    decision = arbiter.decide(
        persona=p["active_persona"],
        purpose_signal=signal["purpose_signal"],
        external_pressure=0.4,
    )

    assert p["active_persona"] in {"work", "rest", "play", "reflect"}
    assert 0.0 <= signal["purpose_signal"] <= 1.0
    assert "action_mode" in decision
