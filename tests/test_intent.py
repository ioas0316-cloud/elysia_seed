import unittest
import sys
import os

# Ensure the package is in the path
sys.path.append(os.getcwd())

from elysia_engine.storyteller import StoryTeller

class TestIntent(unittest.TestCase):

    def test_body_keywords(self):
        """Test that aggression-related words increase Body force."""
        inputs = ["fight", "I want to kill", "use strength"]
        for text in inputs:
            forces = StoryTeller.parse_intent(text)
            self.assertGreater(forces["body"], 0.0, f"Failed for '{text}'")
            self.assertEqual(forces["soul"], 0.0)
            self.assertEqual(forces["spirit"], 0.0)

    def test_soul_keywords(self):
        """Test that connection-related words increase Soul force."""
        inputs = ["love", "help me", "protect them"]
        for text in inputs:
            forces = StoryTeller.parse_intent(text)
            self.assertGreater(forces["soul"], 0.0, f"Failed for '{text}'")
            self.assertEqual(forces["body"], 0.0)
            self.assertEqual(forces["spirit"], 0.0)

    def test_spirit_keywords(self):
        """Test that intellect-related words increase Spirit force."""
        inputs = ["think", "plan ahead", "focus magic"]
        for text in inputs:
            forces = StoryTeller.parse_intent(text)
            self.assertGreater(forces["spirit"], 0.0, f"Failed for '{text}'")
            self.assertEqual(forces["body"], 0.0)
            self.assertEqual(forces["soul"], 0.0)

    def test_mixed_intent(self):
        """Test that mixed sentences affect multiple axes."""
        text = "I will fight to protect my friends with magic"
        forces = StoryTeller.parse_intent(text)

        # fight -> body
        self.assertGreater(forces["body"], 0.0)
        # protect, friends -> soul
        self.assertGreater(forces["soul"], 0.0)
        # magic -> spirit
        self.assertGreater(forces["spirit"], 0.0)

    def test_normalization(self):
        """Test that values are capped at 1.0."""
        # Repeating 'fight' many times
        text = "fight fight fight fight fight fight fight"
        forces = StoryTeller.parse_intent(text)
        self.assertLessEqual(forces["body"], 1.0)

if __name__ == '__main__':
    unittest.main()
