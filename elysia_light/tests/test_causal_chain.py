import unittest
from elysia_light.core.digestive_system import DigestiveSystem, CausalChain
from elysia_light.core.monad.monad import Monad
from elysia_light.core.foundation.structure.hypersphere import HyperSphere

class TestCausalChain(unittest.TestCase):
    def setUp(self):
        self.monad = Monad("TestMonad")
        self.field = HyperSphere()
        self.digestive = DigestiveSystem(self.monad, self.field)

    def test_active_probe_structure(self):
        """Verify the 4-step chain is generated correctly."""
        stimulus = "Hello World"
        chain = self.digestive.active_probe(stimulus)

        # Check node count
        self.assertEqual(len(chain.chain), 4)

        # Check steps in order
        expected_steps = ["Cause", "Structure", "Function", "Reality"]
        for i, node in enumerate(chain.chain):
            self.assertEqual(node.step, expected_steps[i])

    def test_digestion_integration(self):
        """Verify digestion triggers probing and field storage."""
        result = self.digestive.digest("Test Input")
        self.assertTrue("Digested" in result)
        self.assertEqual(self.field.population, 1)

if __name__ == '__main__':
    unittest.main()
