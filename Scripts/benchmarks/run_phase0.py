from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from Core.System.Metabolism.rotor_wave_engine import RotorWaveEngine
from Core.System.Contracts.event_validator import validate_event
from Core.Intelligence.Metabolism.triple_helix_cognition import TripleHelixCognition
from Core.Intelligence.Metabolism.phase_boundary_learning import PhaseBoundaryLearner
from Core.Intelligence.Metabolism.triadic_resonance import TriadicResonanceEngine
from Core.Intelligence.Metabolism.tri_state_sovereignty import TriStateSovereigntyEngine
from Core.Intelligence.Metabolism.rotor_scale_taxonomy import classify_profile
from Core.System.Metabolism.clock_rotor import ClockRotor
from Core.System.Metabolism.persona_rotor_orchestrator import PersonaRotorOrchestrator
from Core.System.Metabolism.sovereign_arbiter import SovereignArbiter
from Core.System.Metabolism.purpose_accrual import PurposeAccrual
from Core.System.Metabolism.rotor_dynamics_field import RotorDynamicsField


SCENARIOS = [
    {"id": f"scenario_{i:02d}", "signal": f"signal {i}", "objective": "optimize convergence"}
    for i in range(1, 21)
]


def main() -> None:
    engine = RotorWaveEngine(anchor_id="@benchmark", max_workers=4)
    helix = TripleHelixCognition(depth=3, growth=1.18)
    boundary = PhaseBoundaryLearner(sensitivity=0.62)
    triad = TriadicResonanceEngine()
    tri_state = TriStateSovereigntyEngine(expansion_gain=1.25, stability_bias=0.74)
    clock = ClockRotor()
    persona = PersonaRotorOrchestrator()
    arbiter = SovereignArbiter()
    purpose = PurposeAccrual()
    dynamics = RotorDynamicsField(damping=0.07, amplification=0.16, coupling=0.24)

    scores = []
    helix_scores = []
    event_errors = []
    boundary_scores = []
    resonance_scores = []
    joy_scores = []
    alignment_scores = []
    freedom_scores = []
    stability_scores = []
    balance_scores = []
    autonomy_scores = []
    dynamics_scores = []

    for sc in SCENARIOS:
        result = engine.run(
            signal=sc["signal"],
            objective=sc["objective"],
            axis_candidates=["context_time_goal", "risk_cost_intent", "coherence_energy_memory"],
        )
        score = max(0.0, min(1.0, (result["phase_coherence"] + (1.0 - result["collapse_regret"])) / 2.0))
        scores.append(score)
        helix_state = helix.expand(sc["signal"], timesteps=4)
        helix_scores.append(helix_state["final_coherence"])
        chars = [((ord(c) % 100) / 100.0) for c in sc["signal"][:8]] or [0.5]
        inner_stream = chars
        outer_stream = list(reversed(chars))
        boundary_state = boundary.learn(inner_stream, outer_stream, timesteps=4)
        boundary_scores.append(boundary_state["final"]["boundary_clarity"])
        user_stream = chars
        assistant_stream = [min(1.0, c * 0.95 + 0.03) for c in chars]
        elysia_stream = [min(1.0, c * 1.02) for c in chars]
        triad_state = triad.evaluate(user_stream, assistant_stream, elysia_stream)
        resonance_scores.append(triad_state["phase_resonance"])
        joy_scores.append(triad_state["cognitive_joy"])
        alignment_scores.append(triad_state["triadic_alignment"])
        tri_state_out = tri_state.evaluate(
            defined_signal=result["phase_coherence"],
            undefined_signal=helix_state["final_coherence"],
            identity_signal=triad_state["triadic_alignment"],
        )
        freedom_scores.append(tri_state_out["freedom_expansion"])
        stability_scores.append(tri_state_out["sovereign_stability"])
        balance_scores.append(tri_state_out["balance_gate"])

        ticks = clock.spin(load=result["phase_coherence"], fatigue=1 - boundary_state["final"]["restoration_coherence"])
        persona_state = persona.select(ticks.energy_tick, ticks.momentum_tick, ticks.recovery_tick)
        purpose_state = purpose.update(success=result["phase_coherence"], resonance=triad_state["phase_resonance"], fatigue=ticks.recovery_tick)
        decision = arbiter.decide(
            persona=persona_state["active_persona"],
            purpose_signal=purpose_state["purpose_signal"],
            external_pressure=1 - triad_state["triadic_alignment"],
        )
        autonomy_scores.append(max(0.0, min(1.0, 0.5 + decision["autonomy_margin"])))

        dynamic_state = dynamics.evolve([
            result["phase_coherence"],
            helix_state["final_coherence"],
            triad_state["phase_resonance"],
            tri_state_out["balance_gate"],
        ], steps=6)
        dynamics_scores.append(dynamic_state["natural_selection_score"])

    for ev in engine.events:
        errs = validate_event(ev)
        if errs:
            event_errors.append({"event_type": ev.get("event_type"), "errors": errs})

    avg_score = sum(scores) / len(scores)
    helix_avg = sum(helix_scores) / len(helix_scores)
    boundary_avg = sum(boundary_scores) / len(boundary_scores)
    resonance_avg = sum(resonance_scores) / len(resonance_scores)
    joy_avg = sum(joy_scores) / len(joy_scores)
    alignment_avg = sum(alignment_scores) / len(alignment_scores)
    freedom_avg = sum(freedom_scores) / len(freedom_scores)
    stability_avg = sum(stability_scores) / len(stability_scores)
    balance_avg = sum(balance_scores) / len(balance_scores)
    autonomy_avg = sum(autonomy_scores) / len(autonomy_scores)
    dynamics_avg = sum(dynamics_scores) / len(dynamics_scores)
    scale_profile = classify_profile({
        "phase_coherence_score": avg_score,
        "triple_helix_coherence": helix_avg,
        "boundary_clarity": boundary_avg,
        "phase_resonance": resonance_avg,
        "cognitive_joy": joy_avg,
        "triadic_alignment": alignment_avg,
        "freedom_expansion": freedom_avg,
        "sovereign_stability": stability_avg,
        "balance_gate": balance_avg,
        "autonomy_flow": autonomy_avg,
        "natural_dynamics": dynamics_avg,
    })


    report = {
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "scenario_count": len(SCENARIOS),
        "kpi": {
            "phase_coherence_score": round(avg_score, 4),
            "triple_helix_coherence": round(helix_avg, 4),
            "boundary_clarity": round(boundary_avg, 4),
            "phase_resonance": round(resonance_avg, 4),
            "cognitive_joy": round(joy_avg, 4),
            "triadic_alignment": round(alignment_avg, 4),
            "freedom_expansion": round(freedom_avg, 4),
            "sovereign_stability": round(stability_avg, 4),
            "balance_gate": round(balance_avg, 4),
            "autonomy_flow": round(autonomy_avg, 4),
            "natural_dynamics": round(dynamics_avg, 4),
            "pass": len(SCENARIOS) >= 20 and avg_score >= 0.5 and helix_avg >= 0.5 and boundary_avg >= 0.45 and alignment_avg >= 0.6 and balance_avg >= 0.65 and autonomy_avg >= 0.55 and dynamics_avg >= 0.6 and len(event_errors) == 0,
        },
        "rotor_scale_profile": scale_profile,
        "contract_validation": {
            "errors": event_errors,
            "error_count": len(event_errors),
        },
    }

    out = Path("data/benchmarks/latest_report.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"wrote {out}")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
