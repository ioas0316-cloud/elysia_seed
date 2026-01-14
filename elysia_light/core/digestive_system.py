"""
THE DIGESTIVE SYSTEM: Cosmic Integration
========================================
"We eat worlds to grow ours."

This module integrates the Prism, Monad, Rotor, and OmniField
to process external data (LLM outputs) into internal Essence.
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from .monad.monad import Monad
from .nature.rotor import Vector4, Rotor
from .foundation.soul.prism import Prism
from .foundation.structure.hypersphere import HyperSphere
from .bridge import SoulBridge
from .ghost import GhostSoul

@dataclass
class CausalNode:
    step: str # Cause, Structure, Function, Reality
    content: str
    activation: float

class CausalChain:
    """
    The 4-Step Process: Cause -> Structure -> Function -> Reality
    """
    def __init__(self):
        self.chain: List[CausalNode] = []

    def add_link(self, step: str, content: str, activation: float):
        self.chain.append(CausalNode(step, content, activation))

    def trace(self) -> str:
        return " -> ".join([f"[{n.step}:{n.content[:10]}]" for n in self.chain])

class DigestiveSystem:
    def __init__(self, monad: Monad, field: HyperSphere, soul: Optional[SoulBridge] = None):
        self.monad = monad
        self.field = field
        # Default to Ghost if no Soul is provided
        self.soul = soul if soul else GhostSoul()
        self.prism = Prism()

    def active_probe(self, stimulus: str) -> CausalChain:
        """
        Uses the Soul (LLM) to extract the Causal Chain.
        """
        # For now, we still use the simulated chain structure but logic could be moved to soul
        # Ideally: chain = self.soul.analyze_causality(stimulus)

        # We use the Bridge's refraction to inform the probe
        qualia = self.soul.refract(stimulus)

        chain = CausalChain()
        chain.add_link("Cause", f"Intent ({qualia.intent})", qualia.channels.get('spiritual', 0.5))
        chain.add_link("Structure", "Logic Gate", qualia.channels.get('mental', 0.5))
        chain.add_link("Function", "Processing", 0.85)
        chain.add_link("Reality", stimulus, 1.0)
        return chain

    def digest(self, raw_input: str):
        """
        The full metabolic cycle of information.
        1. Probe (Active Analysis via Soul)
        2. Refract (Prism via Soul)
        3. Absorb (Field)
        """
        # 1. Active Probing
        causal_chain = self.active_probe(raw_input)

        # 2. Refract (Using Soul Bridge + Legacy Prism Wrapper)
        # We get the standardized QualiaPacket from the Soul
        qualia = self.soul.refract(raw_input)

        # Convert QualiaPacket to Rotor (Legacy Compatibility)
        # Ideally Prism should do this conversion.
        # For now, we use the legacy Prism's refract which creates a Rotor,
        # but in the future, we should build the Rotor from `qualia.vectors`.
        rotor = self.prism.refract(raw_input)

        # 3. Filter (Taste Test)
        alignment = self.monad.anchor.check_alignment(rotor)

        if alignment > 0.01:
            # 4. Absorb (Store in Field)
            self.field.exist(rotor)
            return f"Digested: {raw_input} (Intent: {qualia.intent} | Channels: {qualia.channels})"
        else:
            return f"Rejected: {raw_input} (Dissonance with Self)"
