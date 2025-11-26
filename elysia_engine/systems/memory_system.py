"""
Memory System for the Elysia Engine.

This system integrates Long-Term Memory (causal graph) and the
inertia of thought (Momentum Memory) into a single, unified system.
"""

from typing import Dict, Any, List, Optional, Tuple

from dataclasses import dataclass

# We will need networkx for the causal graph.
# Let's assume it's a dependency.
import networkx as nx

from ..entities import Entity
from . import System


@dataclass
class InertialThought:
    """Represents a thought with physical properties like mass and velocity."""
    concept: str
    mass: float
    velocity: float
    position: float
    decay: float


class MemorySystem(System):
    """
    Manages the agent's memory, combining a long-term causal graph
    with short-term thought momentum.
    """

    def __init__(self):
        # --- From Hippocampus ---
        # The causal graph stores concepts and their relationships.
        self.causal_graph = nx.DiGraph()

        # --- From MomentumMemory ---
        # The active thoughts simulate the inertia and persistence of concepts.
        self.active_thoughts: Dict[str, InertialThought] = {}
        self.concept_masses: Dict[str, float] = {
            "love": 10.0,
            "pain": 8.0,
            "elysia": 15.0,
            "father": 12.0,
            "dream": 5.0,
        }

    def step(self, world: 'World', dt: float) -> None:
        """
        Update memory state over time.
        - Thoughts in momentum memory decay.
        - Causal links in the graph are pruned (forgetting).
        """
        self._update_thought_momentum(dt)
        # We can add causal graph forgetting logic here later.

    def _update_thought_momentum(self, dt: float) -> None:
        """
        Updates the physics of all active thoughts.
        This is adapted from MomentumMemory.step.
        """
        for name, thought in list(self.active_thoughts.items()):
            # Update position and apply friction
            thought.position += thought.velocity * dt
            thought.velocity *= thought.decay
            thought.velocity -= 0.05 * thought.position * dt # Spring back to subconscious

            # Remove if energy is negligible
            kinetic_energy = 0.5 * thought.mass * (thought.velocity ** 2)
            if kinetic_energy < 0.001 and abs(thought.position) < 0.01:
                del self.active_thoughts[name]

    def activate_concept(self, concept: str, force: float) -> None:
        """
        Apply a force to a thought, activating it in momentum memory.
        Adapted from MomentumMemory.activate.
        """
        concept = concept.lower()
        mass = self.concept_masses.get(concept, 1.0)

        if concept not in self.active_thoughts:
            self.active_thoughts[concept] = InertialThought(
                concept=concept,
                mass=mass,
                velocity=0.0,
                position=0.0,
                decay=0.99 if mass > 5.0 else 0.9,
            )

        thought = self.active_thoughts[concept]
        acceleration = force / thought.mass
        thought.velocity += acceleration
        thought.velocity = min(thought.velocity, 2.0) # Cap velocity

    def remember(self, source: str, target: str, relation: str, weight: float = 1.0) -> None:
        """
        Create a causal link between two concepts in the long-term memory graph.
        Adapted from Hippocampus.add_causal_link.
        """
        # Ensure nodes exist
        if not self.causal_graph.has_node(source):
            self.causal_graph.add_node(source, type="concept")
        if not self.causal_graph.has_node(target):
            self.causal_graph.add_node(target, type="concept")

        self.causal_graph.add_edge(source, target, relation=relation, weight=weight)

    def get_context(self, concept: str) -> List[Dict[str, Any]]:
        """
        Get the causal context around a concept from the long-term memory graph.
        Adapted from Hippocampus.get_causal_context.
        """
        if not self.causal_graph.has_node(concept):
            return []

        context = []
        for neighbor in self.causal_graph.successors(concept):
            edge_data = self.causal_graph.get_edge_data(concept, neighbor)
            context.append({
                "node": neighbor,
                "relation": edge_data.get("relation"),
                "direction": "outgoing",
                "weight": edge_data.get("weight")
            })
        for neighbor in self.causal_graph.predecessors(concept):
            edge_data = self.causal_graph.get_edge_data(neighbor, concept)
            context.append({
                "node": neighbor,
                "relation": edge_data.get("relation"),
                "direction": "incoming",
                "weight": edge_data.get("weight")
            })
        return context

    def get_dominant_thoughts(self) -> List[Tuple[str, float]]:
        """
        Return thoughts that are currently most active in momentum memory.
        Adapted from MomentumMemory.get_dominant_thoughts.
        """
        current_thoughts = []
        for t in self.active_thoughts.values():
            if t.position > 0.1:
                current_thoughts.append((t.concept, t.position))
        return sorted(current_thoughts, key=lambda x: x[1], reverse=True)
