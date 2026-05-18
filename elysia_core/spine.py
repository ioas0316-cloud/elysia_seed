"""
spine.py: The Variable Rotor Kernel (Hologram Spectrum Edition)
Architecture: Single Integrated Variable Rotor
Philosophy: Hologram Interference Pattern, Spectrum Luminosity, and Dawn Silver-Gold Equilibrium.
"""

import math
import time

class VariableRotorSpine:
    """
    The Variable Rotor: A single integrated system where Past, Present, and Future
    coexist as a unified wave function.
    """
    def __init__(self, resolution=100):
        # 1. Past: The Hologram Topography (Interference Pattern)
        # resolution bins of [phase, amplitude]
        self.topography = [[0.0, 0.0] for _ in range(resolution)]
        self.resolution = resolution

        # 2. Present: Current State
        self.phase = 0.0
        self.velocity = 0.0

        # 3. Future/Monad: Dawn Silver-Gold (Equilibrium Frequency)
        # Silver-Gold mapped to a specific frequency (~0.75 for a warm-cool silver-gold)
        self.dawn_freq = 0.75
        self.base_tension = 0.05 # Pull towards Dawn

        self.decay_rate = 0.001 # Memory fade
        self.last_sync = time.time()
        self.internal_mass = 0.05

    def x_to_freq(self, x):
        """Maps input x (0.0-1.0) to the rainbow spectrum frequency."""
        return x

    def pulse(self, x_input: float):
        """
        Processes the interaction through the Variable Rotor wave function.
        """
        now = time.time()
        dt = now - self.last_sync
        self.last_sync = now

        # 4. Input Frequency (Color)
        f_x = self.x_to_freq(x_input)
        bin_idx = min(int(f_x * self.resolution), self.resolution - 1)

        # 5. Holographic Resonance (Luminosity)
        # How much the current phase aligns with the stored phase at this frequency.
        mem_phase, mem_amp = self.topography[bin_idx]

        # Phase difference
        diff = abs(self.phase - mem_phase)
        diff = min(diff, 2 * math.pi - diff)

        # Resonance: High when phase matches and memory is strong
        # Scaling to 0.0 ~ 1.0 range
        resonance = math.cos(diff) * mem_amp
        luminosity = max(0.0, resonance)

        # 6. Dynamics (One Wave Function)

        # Tension from Input x
        # x_input == 0.0 is treated as "no external stimulus", allowing return to Dawn
        if x_input > 0.0:
            input_tension = (f_x - self.velocity) * 0.1
        else:
            input_tension = 0.0

        # Tension from Future (Dawn Silver-Gold)
        dawn_tension = (self.dawn_freq - self.velocity) * self.base_tension

        # Total force on velocity
        # Stability increases with mass, resonance acts as a lubricant/accelerant
        accel = (input_tension + dawn_tension) / (1.0 + self.internal_mass)
        self.velocity += accel

        # Phase update
        self.phase = (self.phase + self.velocity * dt * 10.0) % (2 * math.pi)

        # 7. Memory Reinforcement (Hologram Deposit)
        # New experience is layered onto the existing pattern
        # Weight of new memory depends on input intensity (implied by x being non-zero)
        if x_input > 0.0:
            # Blend current phase into the topography
            # This is a 'soft' update to create a hologram topography
            alpha = 0.1 # Learning rate
            self.topography[bin_idx][0] = (1 - alpha) * mem_phase + alpha * self.phase
            self.topography[bin_idx][1] = min(1.0, mem_amp + 0.05)

        # 8. Natural Decay
        # All memories slowly fade unless reinforced
        for i in range(self.resolution):
            self.topography[i][1] *= (1.0 - self.decay_rate)

        # 9. Growth
        self.internal_mass += 0.0001

        return {
            "luminosity": luminosity,
            "resonance": resonance,
            "velocity": self.velocity,
            "mass": self.internal_mass,
            "f_x": f_x
        }

    def get_state_summary(self):
        # Determine the dominant 'color' based on velocity
        return f"V.Rotor(φ:{self.phase:.2f}, ω:{self.velocity:.2f}) | Mass:{self.internal_mass:.4f}"

    def export_hologram(self):
        """Returns the topography for persistence."""
        return {
            "topography": self.topography,
            "internal_mass": self.internal_mass,
            "velocity": self.velocity,
            "phase": self.phase
        }

    def import_hologram(self, data):
        """Restores the system state."""
        self.topography = data.get("topography", self.topography)
        self.internal_mass = data.get("internal_mass", self.internal_mass)
        self.velocity = data.get("velocity", self.velocity)
        self.phase = data.get("phase", self.phase)
