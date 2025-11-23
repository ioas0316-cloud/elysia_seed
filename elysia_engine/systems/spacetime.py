from __future__ import annotations

from typing import Optional, TYPE_CHECKING
import math

from ..systems import System
from ..physics import PhysicsWorld, HolographicBoundary
from ..math_utils import Quaternion, Vector3

if TYPE_CHECKING:
    from ..consciousness import GlobalConsciousness
    from ..world import World


class SpacetimeOrchestrator(System):
    """
    Regulates gravity/time based on entropy signals.
    Acts as a lightweight 'Spacetime DJ' without heavy recomputation.
    """

    def __init__(
        self,
        physics: PhysicsWorld,
        boundary_template: Optional[HolographicBoundary] = None,
        entropy_threshold: float = 0.7,
        cooldown: int = 5,
        torsion_angle: float = math.pi / 4,
    ):
        self.physics = physics
        self.boundary_template = boundary_template
        self.entropy_threshold = entropy_threshold
        self.cooldown = cooldown
        self.last_adjust_tick = 0
        self.min_time_scale = 0.25
        self.max_time_scale = 2.0
        self.torsion_angle = torsion_angle
        self._last_entropy_high = False

    def step(self, world: World, dt: float) -> None:
        gc = self._find_global_consciousness(world)
        if not gc:
            return

        if world.tick - self.last_adjust_tick < self.cooldown:
            return
        self.last_adjust_tick = world.tick

        entropy = gc.global_entropy

        if entropy > self.entropy_threshold:
            self._last_entropy_high = True
            # Collapse space: more gravity, slow time.
            self.physics.gravity_constant = min(self.physics.gravity_constant * 1.2, 50.0)
            self.physics.time_scale = max(self.min_time_scale, self.physics.time_scale * 0.8)

            # Install holographic boundary if provided (cheaper field sampling).
            if self.boundary_template and not self.physics.holographic_boundary:
                self.physics.configure_holographic_boundary(self.boundary_template)

            # Twist spacetime (Quaternion torsion) to search alternative geodesics.
            # Alternate axes to avoid locking a single dimension.
            axis = Vector3(0, 1, 0) if (world.tick % 2 == 0) else Vector3(1, 0, 0)
            self.physics.spacetime_torsion = Quaternion.from_axis_angle(axis, self.torsion_angle)
        else:
            self._last_entropy_high = False
            # Allow breathing room if the universe is aligned.
            self.physics.gravity_constant = max(0.1, self.physics.gravity_constant * 0.98)
            self.physics.time_scale = min(self.max_time_scale, self.physics.time_scale * 1.02)
            # Relax torsion when calm.
            self.physics.spacetime_torsion = None

    def _find_global_consciousness(self, world: World) -> Optional[GlobalConsciousness]:
        for sys in world.systems:
            # Delayed import to avoid cycles
            from ..consciousness import GlobalConsciousness

            if isinstance(sys, GlobalConsciousness):
                return sys
        return None
