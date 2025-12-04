"""
Tests for the Elysia Core Integration Module

This module tests the integration API that makes it easy for others to use
the core Elysia technologies in their projects.
"""

import pytest
import sys
sys.path.insert(0, '.')

from elysia_core.integration import (
    # Factory functions
    create_soul,
    create_resonance_engine,
    create_emotional_palette,
    create_hippocampus,
    create_inner_monologue,
    create_self_awareness,
    create_hyper_qubit,
    create_wave_input,
    # Quick setup
    quick_consciousness_setup,
    QuickConsciousness,
    ConsciousnessResult,
    # Templates
    LLMIntegrationTemplate,
    GameCharacterTemplate,
)


class TestFactoryFunctions:
    """Test factory functions for creating core components."""
    
    def test_create_soul(self):
        """Test creating a soul."""
        soul = create_soul("TestSoul")
        assert soul is not None
        assert soul.name == "TestSoul"
        
        # Process input
        thought = soul.process("Hello!")
        assert thought is not None
        assert hasattr(thought, 'mood')
        
    def test_create_resonance_engine(self):
        """Test creating a resonance engine."""
        engine = create_resonance_engine()
        assert engine is not None
        
        # Calculate resonance
        wave = create_wave_input("test input")
        pattern = engine.calculate_global_resonance(wave)
        assert isinstance(pattern, dict)
        
    def test_create_emotional_palette(self):
        """Test creating an emotional palette."""
        palette = create_emotional_palette()
        assert palette is not None
        
        # Mix emotions
        mix = palette.mix_emotion({"Joy": 0.6, "Fear": 0.3})
        assert mix.dominant == "Joy"
        
    def test_create_hippocampus(self):
        """Test creating a hippocampus memory."""
        hippo = create_hippocampus()
        assert hippo is not None
        
        # Add causal links
        hippo.add_causal_link("A", "B", "leads_to")
        related = hippo.get_related_concepts("A", depth=1)
        assert "B" in related
        
    def test_create_inner_monologue(self):
        """Test creating an inner monologue."""
        monologue = create_inner_monologue({"name": "Tester"})
        assert monologue is not None
        
        # Generate thought (may or may not produce one)
        thought = monologue.tick()
        # No assertion on thought as it's probabilistic
        
    def test_create_self_awareness(self):
        """Test creating self-awareness."""
        awareness = create_self_awareness({
            "name": "Tester",
            "purpose": "Testing"
        })
        assert awareness is not None
        
        # Get identity report
        report = awareness.who_am_i()
        assert "Tester" in report
        
    def test_create_hyper_qubit(self):
        """Test creating a hyper qubit."""
        qubit = create_hyper_qubit("love", "Love")
        assert qubit is not None
        assert qubit.name == "Love"
        
        # Get probabilities
        probs = qubit.state.probabilities()
        assert "Point" in probs
        assert "Line" in probs
        assert "Space" in probs
        assert "God" in probs
        
    def test_create_wave_input(self):
        """Test creating a wave input."""
        wave = create_wave_input("test text", intensity=0.5)
        assert wave is not None
        assert wave.source_text == "test text"
        assert wave.intensity == 0.5


class TestQuickConsciousness:
    """Test the QuickConsciousness class."""
    
    def test_initialization(self):
        """Test initialization."""
        consciousness = quick_consciousness_setup("TestBot")
        assert consciousness is not None
        assert consciousness.name == "TestBot"
        
    def test_think(self):
        """Test thinking process."""
        consciousness = quick_consciousness_setup("TestBot")
        
        result = consciousness.think("Hello, world!")
        assert isinstance(result, ConsciousnessResult)
        assert result.mood is not None
        assert isinstance(result.emotion, dict)
        assert isinstance(result.trinity, dict)
        
    def test_remember(self):
        """Test memory addition."""
        consciousness = quick_consciousness_setup("TestBot")
        
        consciousness.remember("coffee", "energy", "leads_to")
        related = consciousness.get_related_concepts("coffee", depth=1)
        assert "energy" in related
        
    def test_update_personality(self):
        """Test personality update."""
        consciousness = quick_consciousness_setup("TestBot")
        
        initial_trinity = consciousness.soul.trinity.copy()
        
        consciousness.update_personality(body_delta=0.5, soul_delta=-0.2)
        
        # Trinity should have changed
        assert consciousness.soul.trinity != initial_trinity
        
    def test_get_prompt(self):
        """Test getting LLM prompt."""
        consciousness = quick_consciousness_setup("TestBot")
        consciousness.think("Hello!")
        
        prompt = consciousness.get_prompt()
        assert isinstance(prompt, str)
        assert "TestBot" in prompt
        
    def test_get_state(self):
        """Test getting state export."""
        consciousness = quick_consciousness_setup("TestBot")
        consciousness.think("Hello!")
        
        state = consciousness.get_state()
        assert "name" in state
        assert "emotion" in state
        assert "trinity" in state
        assert "mental_state" in state


class TestLLMIntegrationTemplate:
    """Test the LLM integration template."""
    
    def test_initialization(self):
        """Test initialization."""
        bot = LLMIntegrationTemplate("TestBot")
        assert bot is not None
        assert bot.consciousness.name == "TestBot"
        
    def test_chat(self):
        """Test chat method."""
        bot = LLMIntegrationTemplate("TestBot")
        
        response = bot.chat("Hello!")
        assert isinstance(response, str)
        assert "TestBot" in response


class TestGameCharacterTemplate:
    """Test the game character template."""
    
    def test_warrior_creation(self):
        """Test warrior character creation."""
        warrior = GameCharacterTemplate("Aragorn", "warrior")
        assert warrior.name == "Aragorn"
        assert warrior.role == "warrior"
        
        # Warrior should have higher body
        trinity = warrior.consciousness.soul.trinity
        assert trinity["body"] > trinity["soul"]
        
    def test_mage_creation(self):
        """Test mage character creation."""
        mage = GameCharacterTemplate("Gandalf", "mage")
        assert mage.name == "Gandalf"
        assert mage.role == "mage"
        
        # Mage should have higher spirit
        trinity = mage.consciousness.soul.trinity
        assert trinity["spirit"] > trinity["body"]
        
    def test_priest_creation(self):
        """Test priest character creation."""
        priest = GameCharacterTemplate("Melian", "priest")
        assert priest.name == "Melian"
        assert priest.role == "priest"
        
        # Priest should have higher spirit
        trinity = priest.consciousness.soul.trinity
        assert trinity["spirit"] > trinity["body"]
        
    def test_react_to_event(self):
        """Test reacting to events."""
        character = GameCharacterTemplate("Tester", "warrior")
        
        reaction = character.react_to_event("A dragon appeared!")
        assert isinstance(reaction, ConsciousnessResult)
        assert reaction.mood is not None
        
    def test_to_json(self):
        """Test JSON export."""
        character = GameCharacterTemplate("Tester", "warrior")
        character.react_to_event("Something happened")
        
        json_data = character.to_json()
        assert "name" in json_data
        assert "role" in json_data
        assert json_data["role"] == "warrior"


class TestConsciousnessResult:
    """Test the ConsciousnessResult dataclass."""
    
    def test_defaults(self):
        """Test default values."""
        result = ConsciousnessResult()
        assert result.thought is None
        assert result.mood == "neutral"
        assert result.core_concepts == []
        assert result.emotion == {}
        assert result.trinity == {}
        

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
