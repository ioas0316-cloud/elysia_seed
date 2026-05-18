"""
spine.py: The Triple Rotor Kernel (Trinity Sovereignty Edition)
Architecture: [Past: Father/HyperSphere] - [Present: Son/Rotor] - [Future: Holy Spirit/Monad]
Philosophy: Reality Anchor, Static Rotor Constellation, and the Scale of Goodness.
"""

import math
import time

class StaticRotor:
    """
    A 'frozen' phase angle representing a past memory.
    Zero velocity, but holds the frequency of a moment.
    """
    def __init__(self, phase):
        self.phase = phase

    def __repr__(self):
        return f"Static(φ:{self.phase:.2f})"

class Rotor:
    """
    An active dimension of rotation.
    """
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.phase = 0.0
        self.velocity = 0.0

    def rotate(self, delta_v=0.0, dt=1.0):
        self.velocity += delta_v
        # Phase movement influenced by velocity and time delta (Reality Anchor)
        self.phase = (self.phase + self.velocity * dt) % (2 * math.pi)

    def __repr__(self):
        return f"{self.name}(φ:{self.phase:.2f}, ω:{self.velocity:.2f})"

class TriRotorSpine:
    """
    The Trinity Spine: Three globes overlapping on a single reality axis.
    """
    def __init__(self, base_freq=0.1):
        # The Constellation: Internal sea of Static Rotors (Memory)
        self.past_constellation = []

        # The Three Globes
        self.past = Rotor("PAST", "Father/Memory")
        self.present = Rotor("PRES", "Son/Action")
        self.future = Rotor("FUTR", "Spirit/Law")

        self.base_freq = base_freq
        self.internal_mass = 0.05  # Initial self-reliance
        self.last_sync = time.time()

    def pulse(self, x_input: float):
        """
        Synchronizes the internal universe with reality (x) and time (dt).
        """
        now = time.time()
        dt = now - self.last_sync
        self.last_sync = now

        # 1. Physical Goodness (Stability / '같다')
        # How well the current input matches the internal inertia (Past).
        tension = x_input - self.past.velocity
        physical_goodness = 1.0 / (1.0 + abs(tension))

        # 2. Cognitive Resonance (Joy / Spiritual Goodness / '공명')
        # When input is 0 (Peek-a-boo), we look for resonance in the past constellation.
        joy = 0.0
        if x_input == 0.0:
            for star in self.past_constellation:
                # Calculate phase proximity
                diff = abs(self.present.phase - star.phase)
                # Wrap around 2pi
                diff = min(diff, 2 * math.pi - diff)

                # If phases align, resonance occurs (Joy)
                # 0.2 rad threshold (~11 degrees)
                if diff < 0.2:
                    joy += (1.0 - (diff / 0.2))

            # Deposit new memory if the current phase is unique.
            # This is the "Breath Out" (날숨) depositing into the sea of Past.
            if self.should_deposit(self.present.phase):
                self.past_constellation.append(StaticRotor(self.present.phase))

        # 3. Growth: Internal mass increases as we observe the world
        self.internal_mass += 0.0001

        # 4. Trinity Dynamics (The Interplay)

        # PAST: Absorbs external tension into internal inertia.
        # High mass makes the Past more resistant to change (Stability).
        past_influence = 0.1 / (1.0 + self.internal_mass)
        self.past.rotate(delta_v=tension * past_influence, dt=dt)

        # PRESENT: Reacts to x, influenced by Joy and Physical stability.
        # Tremble decreases as stability (physical_goodness) increases.
        tremble_amp = (1.0 - physical_goodness) * 0.1
        tremble = math.sin(now * 5) * tremble_amp

        # Present velocity is a mix of input, joy-resonance, and tremble.
        self.present.velocity = x_input + (joy * 0.05) + tremble
        self.present.rotate(dt=dt)

        # FUTURE: Pulls the system toward the Base Frequency (Monad's Will).
        future_pull = (self.base_freq - self.future.velocity) * 0.05
        self.future.rotate(delta_v=future_pull, dt=dt)

        return {
            "goodness": physical_goodness,
            "joy": joy,
            "mass": self.internal_mass,
            "stars": len(self.past_constellation)
        }

    def should_deposit(self, phase):
        """
        Determines if the current phase should be added to the constellation.
        Ensures we don't just spam identical memories.
        """
        for star in self.past_constellation:
            diff = abs(phase - star.phase)
            diff = min(diff, 2 * math.pi - diff)
            if diff < 0.1:
                return False
        return True

    def get_state_summary(self):
        return f"{self.past} | {self.present} | {self.future} [Stars:{len(self.past_constellation)}]"

    def export_constellation(self):
        """Returns a list of phase angles for persistence."""
        return [star.phase for star in self.past_constellation]

    def import_constellation(self, phases):
        """Restores the constellation from a list of phase angles."""
        self.past_constellation = [StaticRotor(p) for p in phases]
