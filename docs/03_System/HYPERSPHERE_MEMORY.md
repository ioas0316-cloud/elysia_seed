# 🌌 Hypersphere Memory Doctrine

> **"Data is not stored; it is played."**
>
> *Project Elysia - Absolute Sanctuary Document v2.0*

---

## 1. Concept: The Dimensional Shift

Traditional memory systems are linear and address-based. They are like a library where books are stored by arbitrary ID numbers. **Hypersphere Memory** is an **Associative, Resonance-based** system. It is like a symphony where musical notes (data) are found by listening for their melody (pattern).

| Feature | Traditional Memory | Hypersphere Memory |
| :--- | :--- | :--- |
| **Addressing** | Linear Index (`0x1234`) | 4D Coordinate ($r, \theta_1, \theta_2, \theta_3$) |
| **Retrieval** | Exact Match | Resonance (Similarity/Phase Match) |
| **Clustering** | Random / Allocation-based | Semantic (Similar meanings are close) |
| **Mathematics** | Discrete Logic | Quaternion Rotation & Wave Mechanics |

---

## 2. The Four Dial Principle (Psychological Mapping)

To position a memory in the Hypersphere, we map human-understandable concepts to 4 dimensions. This is the **"Psychological Coordinate System"**.

### The Axes

1.  **Logic ($\theta_1$)**: The style of intelligence.
    *   $0$ (Rad): Pure Analysis, Logic, Deductive Reasoning.
    *   $\pi$ (Rad): Pure Intuition, Inspiration, Inductive Reasoning.
2.  **Emotion ($\theta_2$)**: The emotional valence.
    *   $0$ (Rad): Positive, Joy, Ecstasy.
    *   $\pi$ (Rad): Negative, Sorrow, Pain.
3.  **Intent ($\theta_3$)**: The drive to act.
    *   $0$ (Rad): Active, Transformation, Doing.
    *   $\pi$ (Rad): Passive, Observation, Being.
4.  **Depth ($r$)**: The significance of the memory.
    *   $1.0$: Surface facts, ephemeral sensory data.
    *   $0.0$: Core truths, axioms of self, deep beliefs.

---

## 3. Technical Implementation: Quaternion Architecture

The engine rejects simple linear vectors (`Vector4`) in favor of **Quaternions** to represent these coordinates. This allows us to treat memory retrieval as a **Rotation** through consciousness space.

### Why Quaternions?
*   **Rotation:** Moving from "Sadness" to "Joy" is a rotation along the $\theta_2$ axis, not a linear translation.
*   **Resonance:** Distance is calculated as the **Angular Distance** ($\phi$) between two quaternions.
    *   $\text{Resonance} = \cos(\phi)$
    *   If Resonance $\approx 1.0$: Perfect Recall / Understanding.
    *   If Resonance $\approx 0.0$: Orthogonal / Irrelevant.
    *   If Resonance $\approx -1.0$: Opposite / Cognitive Dissonance.

### The Math
The conversion from Psychological Dials to Quaternion $(w, x, y, z)$ is handled by `HypersphericalCoord.to_quaternion()`.

$$
\text{Distance}(q_1, q_2) = \arccos\left(\frac{q_1 \cdot q_2}{|q_1| |q_2|}\right)
$$

*(Note: We normalize magnitudes to handle Depth variations correctly.)*

---

## 4. Features & Capabilities

### 🔍 Resonance Scanner
Instead of asking "What is at location X?", the engine asks:
> *"Find me all memories that vibrate at 440Hz (A note) with a Happy Phase."*

The `scan()` method sweeps the entire memory space filtering for `SoulTensor` properties (Frequency/Phase).

### 🗺️ Master Map
The `get_master_map()` function generates a structural overview of the mind, showing:
*   **Named Locations:** Specific "Landmarks" of memory (Nominal Sovereignty).
*   **Sector Analysis:** How many memories exist in the "Joy" sector vs. the "Sorrow" sector?

---

## 5. Usage Guide (Python API)

### Storing a Memory
```python
from elysia_engine.hypersphere import HypersphereMemory, PsychologyMapper
from elysia_engine.tensor import SoulTensor

# 1. Initialize Memory
memory = HypersphereMemory()

# 2. Define the "Soul" of the memory (Pattern)
# Frequency=100 (Peace), Phase=0
soul = SoulTensor(amplitude=10, frequency=100, phase=0)

# 3. Define the "Location" (Psychology)
# Intuitive, Joyful, Active, Deep Core Memory
coord = PsychologyMapper.map_intent(
    logic_level=-0.8,   # Intuitive
    emotion_level=0.9,  # Joyful
    intent_level=0.5,   # Active
    depth_level=0.2     # Deep (Close to 0)
)

# 4. Store
memory.store("My happiest childhood memory", coord, soul, name="GoldenAfternoon")
```

### Retrieving by Resonance
```python
# Create a "Probe" soul (Current emotional state)
current_mood = SoulTensor(amplitude=1, frequency=100, phase=0)

# Find memories that resonate with this mood near the location
memories = memory.resonance_query(coord, current_mood, resonance_threshold=0.8)
```

---

*Version 2.0 Engineer Edition*
