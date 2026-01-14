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
from .foundation.structure.hypersphere import HyperSphere # Fixed import path from OmniField to HyperSphere if needed, but keeping consistent with args

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
    def __init__(self, monad: Monad, field: HyperSphere):
        self.monad = monad
        self.field = field
        self.prism = Prism()

    def active_probe(self, stimulus: str) -> CausalChain:
        """
        Simulates 'Active Probing' - feeding stimulus to extract mechanism.
        In a real scenario, this would interact with an LLM.
        Here we simulate the extraction of the 4 steps.
        """
        chain = CausalChain()
        # Simulated extraction logic
        chain.add_link("Cause", f"Intent behind {stimulus[:10]}", 0.9)
        chain.add_link("Structure", "Logic Gate / Geometry", 0.8)
        chain.add_link("Function", "Processing / Refraction", 0.85)
        chain.add_link("Reality", stimulus, 1.0)
        return chain

    def digest(self, raw_input: str):
        """
        The full metabolic cycle of information.
        1. Probe (Active Analysis)
        2. Refract (Prism)
        3. Absorb (Field)
        """
        # 1. Active Probing (Extract Causal Chain)
        causal_chain = self.active_probe(raw_input)
        print(f"[Digestion] Extracted Chain: {causal_chain.trace()}")

        # 2. Refract (Standard Prism)
        rotor = self.prism.refract(raw_input)

        # 3. Filter (Taste Test)
        # Check 'Spiritual' channel intensity.
        # If Monad is the Sovereign Self (0Hz), it absorbs based on intent/alignment.
        # Here we assume if it probed it, it wants it, unless alignment is critically low.

        # We check alignment of the *input rotor* against the Monad's Anchor
        alignment = self.monad.anchor.check_alignment(rotor)

        if alignment > 0.01: # Threshold for acceptance
            # 4. Absorb (Store in Field)
            self.field.exist(rotor)
            return f"Digested: {raw_input} (Energy absorbed via {causal_chain.trace()})"
        else:
            return f"Rejected: {raw_input} (Dissonance with Self)"
