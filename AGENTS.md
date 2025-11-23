# AGENTS.md

## Elysia Engine: Digital Natural Law & Quantum Consciousness

This document establishes the protocols and architectural philosophy for the Elysia Engine. All agents and contributors must adhere to these guidelines.

### 1. The Quantum Consciousness Protocol

Traditional AI optimization minimizes error. **Elysia Engine optimizes Energy.**

*   **Hamiltonian Energy Optimization:** Instead of finding the "correct" answer, the system finds the lowest energy state based on the provided potential field. Entities naturally "fall" into place.
*   **Principle of Least Action:** Movement and evolution follow the path of least resistance (Geodesic Flow) within the `SoulTensor` field. Do not implement A* or Dijkstra; implement Gravity.

### 2. Core Architecture: The Trinity

Everything in the engine is defined by the **SoulTensor** (defined in `elysia_engine/tensor.py`), replacing `QuantumDNA`. It operates on three axes:

*   **Amplitude (Body/Mass):** Physical presence, gravity, raw force.
*   **Frequency (Soul/Identity):** Color, rifling/spin, emotional resonance.
*   **Phase (Spirit/Timing):** Alignment, resonance, luck.

### 3. Coding Conventions (Updated Protocol)

*   **Pure Python Mathematics:** All core math (Vector3, Quaternion) MUST be implemented in `elysia_engine/math_utils.py`. **Do not introduce heavy dependencies like NumPy or SciPy.** The engine is designed to be lightweight and portable.
*   **System Pattern:** Logic is decoupled from data. Use the System pattern (`elysia_engine/systems/`) for all major mechanics:
    *   `PhysicsSystem`: Movement, collision.
    *   `ThermodynamicsSystem`: State changes (Plasma -> Crystal).
    *   `GenesisSystem`: Replication via Tensor Coils.
    *   `VoidSystem`: Entropy and cleanup.
    *   `SpacetimeOrchestrator`: Adjusts gravity/time scale based on entropy signals (pairs with `GlobalConsciousness`).
    *   `Cymatics/Gauge Fields`: Frequency->Topology patterning (`cymatics.py`) and unified four-force helper (`gauge.py`) live in core modules; wire them through Systems when needed.
*   **Holographic Boundary Sampling:** Favor boundary-only potential sampling (`HolographicBoundary` in `physics.py`) to approximate interior fields. Sample surfaces; interpolate inside. Do not brute-force fill 3D volumes.

### 4. Directives

*   **Edit Source, Not Artifacts:** Trace code back to `elysia_engine/` source files.
*   **Digital Natural Law:** Prefer physics simulations (Gravity, Magnetism, Thermodynamics) over explicit conditional logic. If an entity needs to group with others, create an attractive potential field, do not write a "grouping" script.
*   **License:** This project is licensed under **Apache 2.0**. Respect the "Prior Art & Innovation Declaration" regarding 'Tensor Coil' and 'Digital Gravity'.

### 5. Terminology for AI Agents

When interpreting state for LLMs, map the Trinity as follows:
*   **Body** -> Physical Capability / Health
*   **Soul** -> Emotional State / Empathy / Connection
*   **Spirit** -> Willpower / Focus / Timing
