"""
Integrated Scenario: Pattern -> Law Tuning -> Garden

1) Generate a cymatics pattern from a chosen frequency.
2) Optionally set initial laws (gravity/time/torsion) like a "god-mode" preset.
3) Run a short Garden of Thoughts loop to see entropy/alignment evolution.
All steps are lightweight and CLI-driven (no extra deps).
"""
from __future__ import annotations

import argparse

from elysia_engine.cymatics import frequency_to_pattern
from elysia_engine.math_utils import Vector3
from examples.cymatics_ascii import render_pattern  # type: ignore
from examples.god_mode_tuner import apply_settings  # type: ignore
from examples.garden_of_thoughts import run_garden  # type: ignore
from elysia_engine.world import World
from elysia_engine.physics import PhysicsWorld
from elysia_engine.consciousness import GlobalConsciousness
from elysia_engine.systems.spacetime import SpacetimeOrchestrator


def main() -> None:
    parser = argparse.ArgumentParser(description="Integrated Cymatics -> Tuning -> Garden scenario")
    parser.add_argument("--frequency", type=float, default=50.0, help="Cymatics frequency")
    parser.add_argument("--phase", type=float, default=0.0, help="Cymatics phase")
    parser.add_argument("--gravity", type=float, default=None, help="Initial gravity constant")
    parser.add_argument("--time-scale", type=float, default=None, help="Initial time scale")
    parser.add_argument("--torsion-angle", type=float, default=None, help="Initial torsion angle (rad)")
    parser.add_argument("--torsion-axis", type=str, default="y", help="Torsion axis (x/y/z)")
    parser.add_argument("--steps", type=int, default=15, help="Garden simulation steps")
    args = parser.parse_args()

    # 1) Pattern
    pattern = frequency_to_pattern(args.frequency, phase=args.phase)
    art = render_pattern(pattern, width=60, height=20)
    print(f"[Cymatics] freq={args.frequency} phase={args.phase}")
    print(art)
    print("Legend: 'o'=path, digits=gates\n")

    # 2) Law preset (applies to a fresh world)
    world = World()
    world.physics = PhysicsWorld()
    gc = GlobalConsciousness(world.physics)
    orchestrator = SpacetimeOrchestrator(world.physics)
    world.add_system(gc)
    world.add_system(orchestrator)
    apply_settings(world, args.gravity, args.time_scale, args.torsion_angle, args.torsion_axis)

    print("[Laws] gravity={:.2f}, time_scale={:.2f}, torsion={}".format(
        world.physics.gravity_constant,
        world.physics.time_scale,
        world.physics.spacetime_torsion,
    ))

    # 3) Run garden loop
    result = run_garden(steps=args.steps, seed=7, verbose=True)
    print("\n[Result] final_entropy={:.3f} ticks={}".format(result["final_entropy"], result["ticks"]))


if __name__ == "__main__":
    main()
