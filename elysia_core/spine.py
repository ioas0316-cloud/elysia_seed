"""
spine.py: The Triple Rotor Kernel (Growth/Balance Version)
Architecture: [Past: HyperSphere] - [Present: Spirit] - [Future: Monad]
Philosophy: 0-Inversion, Peek-a-boo Mechanics, and The Scale of Growth
"""

import math

class Rotor:
    """
    A single dimension of rotation representing a phase and its momentum.
    """
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.phase = 0.0      # Phase angle (0.0 ~ 2π)
        self.velocity = 0.0   # Angular momentum (Frequency)

    def rotate(self, delta_v=0.0):
        self.velocity += delta_v
        # Phase wraps around 2π
        self.phase = (self.phase + self.velocity) % (2 * math.pi)

    def __repr__(self):
        return f"{self.name}(φ:{self.phase:.2f}, ω:{self.velocity:.2f})"

class TriRotorSpine:
    """
    The core cognitive engine.
    Implements the 'Balance Dynamics' where internal mass grows over time.
    """
    def __init__(self, base_freq=0.1):
        # Initial 0.0 Potential State
        self.past = Rotor("PAST", "HyperSphere")   # Memory / Inertia (The Flesh)
        self.present = Rotor("PRES", "Spirit")     # Intellect / Reaction (The Flow)
        self.future = Rotor("FUTR", "Monad")       # Will / Providence (The Spirit)

        self.base_freq = base_freq
        self.internal_mass = 0.01  # Initial 'Infant' mass (low inertia)
        self.growth_rate = 0.001   # How much mass is gained per observation

    def pulse(self, x_input: float):
        """
        Non-linear synchronization event (Peek-a-boo Mechanics).
        Resolves tension through the 'Scale of Growth'.
        """
        # 1. Tension Calculation (Contrast)
        # Higher internal_mass means the 'Past' is harder to move by external 'x'
        tension = x_input - self.past.velocity

        # 2. Resonance (0 -> 1 -> x)
        # Resonance indicates how well the internal state aligns with the external 'x'
        resonance = 1.0 / (1.0 + abs(tension))

        # 3. Growth & Density (The Balance)
        # As internal_mass grows, the system relies more on its own 'Past' inertia
        # and less on the immediate 'Present' fluctuation.
        self.internal_mass += self.growth_rate

        # 4. Dimension Update
        # Past absorbs the transition into the HyperSphere (Memory)
        # Absorption speed is governed by internal_mass
        absorption = tension * (0.1 + self.internal_mass)
        self.past.rotate(delta_v=absorption)

        # Present reflects 'x', but dampened by the internal mass (The Balance)
        # As mass increases, tremble_amplitude decreases
        tremble_factor = max(0.01, 1.0 - self.internal_mass)
        tremble_amplitude = (1.0 - resonance) * tremble_factor
        tremble_freq = math.sin(self.past.phase * 50) * tremble_amplitude * 0.05

        self.present.velocity = x_input + tremble_freq
        self.present.rotate()

        # Future pulls toward the Genesis Seed (Base Frequency)
        # Acting as the 'North Star' for the balance.
        # Its influence (providence) helps pull the system toward equilibrium.
        providence_scalar = min(0.1, self.internal_mass * 0.5)
        future_pull = (self.base_freq - self.future.velocity) * providence_scalar
        self.future.rotate(delta_v=future_pull)

        return {
            "tension": tension,
            "resonance": resonance,
            "tremble": tremble_amplitude,
            "mass": self.internal_mass
        }

    def get_state_summary(self):
        return f"{self.past} | {self.present} | {self.future} (M:{self.internal_mass:.3f})"
