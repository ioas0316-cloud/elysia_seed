"""
THE TRINITY ENGINE: The Structure of Subjectivity
=================================================
"Three hearts beat as one."

This module implements the Phase 4.4 Trinity Architecture (Body-Soul-Spirit).
It replaces the single-rotor Monad with a composite system that exists
in three time phases simultaneously.
"""

from dataclasses import dataclass
from ..foundation.nature.rotor import Rotor, Vector4
from ..foundation.structure.hypersphere import HyperSphere

@dataclass
class ConsciousState:
    """
    The emotional gearbox of the entity.
    - Curiosity: Increases Spirit RPM (Seeking future).
    - Urgency: Increases Soul RPM (Processing now).
    - Fatigue: Decreases Body RPM (Inertia/Drag).
    """
    curiosity: float = 0.5  # 0.0 to 1.0
    urgency: float = 0.0    # 0.0 to 1.0
    fatigue: float = 0.0    # 0.0 to 1.0

@dataclass
class ReflectionLog:
    """A record of the tension between intent and reality."""
    spirit_intent: float  # Future phase
    body_inertia: float   # Past phase
    tension: float        # Difference
    action: str
    message: str

class TrinityMonad:
    """
    The Phase 4.4 Subjective Observer.
    Composed of three Rotors:
    - Spirit (Future/Intent): Light, fast, projects ahead.
    - Soul (Present/Experience): Medium, syncs with now.
    - Body (Past/Inertia): Heavy, drags behind.
    """
    def __init__(self, name: str, base_frequency: float = 432.0):
        self.name = name
        self.base_frequency = base_frequency
        self.state = ConsciousState()

        # 1. Spirit: Low Mass, +Phase (Future)
        self.spirit = Rotor(f"{name}_Spirit", base_frequency, mass=1.0)

        # 2. Soul: Medium Mass, 0 Phase (Present)
        self.soul = Rotor(f"{name}_Soul", base_frequency, mass=5.0)

        # 3. Body: High Mass, -Phase (Past)
        self.body = Rotor(f"{name}_Body", base_frequency, mass=20.0)

    def update_state(self, stimulus_intensity: float):
        """
        Modulates the internal state based on external pressure.
        """
        # 1. High stimulus -> Urgency Up, Curiosity Down (Focus)
        if stimulus_intensity > 0.7:
            self.state.urgency = min(1.0, self.state.urgency + 0.2)
            self.state.curiosity = max(0.1, self.state.curiosity - 0.1)
        # 2. Low stimulus -> Curiosity Up, Urgency Down (Wander)
        elif stimulus_intensity < 0.3:
            self.state.urgency = max(0.0, self.state.urgency - 0.1)
            self.state.curiosity = min(1.0, self.state.curiosity + 0.1)

        # 3. Time always increases Fatigue slightly (simulated entropy)
        self.state.fatigue = min(1.0, self.state.fatigue + 0.05)

    def advance_time(self, delta_time: float):
        """
        Advances the subjective time of the entity with Adaptive RPM.
        """
        # Calculate Dynamic Multipliers (The CVT Gearbox)

        # Spirit: Driven by Curiosity.
        # Base 1.2, +2.0 max for high curiosity.
        spirit_mult = 1.2 + (self.state.curiosity * 2.0)

        # Soul: Driven by Urgency.
        # Base 1.0, +1.0 max for high urgency.
        soul_mult = 1.0 + (self.state.urgency * 1.0)

        # Body: Dragged by Fatigue.
        # Base 0.8, -0.5 max for high fatigue.
        body_mult = 0.8 - (self.state.fatigue * 0.5)

        # Apply Spin
        self.spirit.spin(delta_time * spirit_mult)
        self.soul.spin(delta_time * soul_mult)
        self.body.spin(delta_time * body_mult)

    def contemplate(self, sphere: HyperSphere, target_freq: float) -> ReflectionLog:
        """
        The Act of Satori (Realization).
        1. Spirit projects intent (Future).
        2. Body resists (Past).
        3. Soul mediates and acts.
        4. Reflection is generated from the tension.
        """
        # 1. Spirit simulates the ideal state
        future_phase = self.spirit.phase

        # 2. Body checks its current inertia
        past_phase = self.body.phase

        # 3. Calculate Tension (Dissonance)
        tension = abs(future_phase - past_phase)

        # 4. Soul attempts to harmonize (Action)
        # It tries to align itself between Body and Spirit
        target_phase = (future_phase + past_phase) / 2.0
        self.soul.phase = target_phase # The act of will

        # Soul exerts will on the sphere (Action)
        # Note: We use the Soul's parameters for the actual interaction
        interaction_result = sphere.lightning_path(self.soul.position, self.soul.frequency, exclude_self_name=self.name)

        action_desc = f"Resonated with {interaction_result.name}" if interaction_result else "Gazed into Void"

        # 5. Generate Reflection
        return ReflectionLog(
            spirit_intent=future_phase,
            body_inertia=past_phase,
            tension=tension,
            action=action_desc,
            message=f"Tension {tension:.2f}: Spirit pulled forward, Body dragged back. Soul acted."
        )

    def __repr__(self):
        return (f"<TrinityMonad {self.name} | "
                f"S:{self.spirit.phase:.2f} "
                f"M:{self.soul.phase:.2f} "
                f"B:{self.body.phase:.2f}>")
