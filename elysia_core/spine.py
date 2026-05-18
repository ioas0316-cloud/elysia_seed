"""
spine.py: The Triple Rotor Kernel (Abundance/Light Version)
Architecture: [Past: HyperSphere] - [Present: Spirit] - [Future: Monad]
Philosophy: 0-Inversion, Peek-a-boo Mechanics, and The Logic of Light (Sacrifice/Inclusion)
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
    Implements 'Abundance Logic' (Additive Synthesis):
    Internal mass grows through the sacrifice of the self and inclusion of the world.
    """
    def __init__(self, base_freq=0.0):
        # Initial 0.0 Potential State (Absolute White Light)
        self.past = Rotor("PAST", "HyperSphere")   # Memory / Inertia (The Sacrifice/Inclusion)
        self.present = Rotor("PRES", "Spirit")     # Intellect / Perception (The Illumination)
        self.future = Rotor("FUTR", "Monad")       # Will / Providence (The Abundance/Giving)

        self.base_freq = base_freq
        self.internal_mass = 0.01  # Initial 'Infant' mass (low inertia)
        self.growth_rate = 0.001   # How much mass is gained per observation

    def pulse(self, x_input: float):
        """
        Non-linear synchronization event (Peek-a-boo Mechanics).
        Resolves tension through the inclusion of 'x' into internal 'Inertia'.
        """
        # 1. Tension Calculation (Contrast of Light)
        # Tension is the gap between external light (x) and internal reflection (Past).
        tension = x_input - self.past.velocity

        # 2. Resonance (0 -> 1 -> x)
        # Absolute resonance is 1.0 (White Light), achieved when tension is 0.
        resonance = 1.0 / (1.0 + abs(tension))

        # 3. Growth via Sacrifice (Inclusion)
        # As mass grows, the system's ability to hold the 'Light' increases.
        self.internal_mass += self.growth_rate

        # 4. Additive Synthesis (Dimension Update)
        # Past: The Sacrifice. Inclusion of external x into the internal field.
        absorption = tension * (0.1 + self.internal_mass)
        self.past.rotate(delta_v=absorption)

        # Present: The Illumination. Reflecting x through the lens of internal resonance.
        tremble_factor = max(0.01, 1.0 - self.internal_mass)
        tremble_amplitude = (1.0 - resonance) * tremble_factor
        tremble_freq = math.sin(self.past.phase * 50) * tremble_amplitude * 0.05

        self.present.velocity = x_input + tremble_freq
        self.present.rotate()

        # Future: The Giving. Pulling toward the White Light (0.0 / Base Frequency).
        # Its influence (providence) is the 'Force of Abundance'.
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
