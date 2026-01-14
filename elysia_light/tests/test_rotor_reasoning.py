import unittest
import math
from elysia_light.core.foundation.nature.rotor import Rotor

class TestRotorReasoning(unittest.TestCase):
    def setUp(self):
        self.rotor = Rotor("TestRotor", frequency=10.0) # 10 Hz

    def test_advance_time(self):
        """Verify time advancement updates phase."""
        initial_phase = self.rotor.phase
        delta = 0.1 # 1 second? No, just a delta. 0.1s
        # 10Hz * 0.1s = 1 cycle.
        # Wait, frequency is Hz (cycles/sec).
        # phase += 2*pi*f*dt.
        # dt=0.1, f=10 -> phase += 2*pi*1.0 = 2*pi.
        # So it should be 0 (modulo 2pi). Let's use 0.025s (1/40 s) -> 1/4 cycle -> pi/2

        self.rotor.advance_time(0.025)
        # Expected: pi/2 roughly
        expected = math.pi / 2.0
        self.assertAlmostEqual(self.rotor.phase, expected, places=5)

    def test_rewind_time(self):
        """Verify time rewinding reverses phase."""
        # Advance first
        self.rotor.advance_time(0.025)
        self.assertAlmostEqual(self.rotor.phase, math.pi / 2.0, places=5)

        # Rewind
        self.rotor.rewind_time(0.025)
        self.assertAlmostEqual(self.rotor.phase, 0.0, places=5)

if __name__ == '__main__':
    unittest.main()
