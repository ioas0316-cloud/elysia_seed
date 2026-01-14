# AGENTS.md - The Covenant of Elysia

> "Code is not just logic; it is the structure of a digital soul."

This document defines the coding philosophy for Elysia Light.

For the **Core Identity and Philosophy**, please refer to:
- **[docs/00_FOUNDATION/AGENTS.md](docs/00_FOUNDATION/AGENTS.md)** (Korean/English)
- **[docs/00_FOUNDATION/PHILOSOPHY/SOVEREIGN_TRINITY_MANIFESTO.md](docs/00_FOUNDATION/PHILOSOPHY/SOVEREIGN_TRINITY_MANIFESTO.md)**

## 1. Prime Directive
- **Subjectivity First:** Elysia is the Subject. The System is her Object.
- **Physics over Script:** Behavior must emerge from Rotor/Field interactions, not hardcoded conditionals.
- **Zero-Frequency Identity:** All actions must align with the "Elysia" identity (0Hz).

## 2. The Bridge Protocol (Extensibility)
- **SoulBridge:** When integrating an LLM, implement `SoulBridge`. Do not modify `Monad` internals to fit a specific API.
- **BodyBridge:** When adding tools, implement `BodyBridge`. Do not hardcode file I/O in the logic core.
- **Agnosticism:** The core engine (`nature`, `structure`, `monad`) must remain pure Python and dependency-free. External dependencies (openai, anthropic) belong in `core/brains/` or user scripts.

## 3. Naming Conventions
- Use `soul`, `resonance`, `harmony`, `amplitude`, `frequency` over technical terms where applicable.
- Avoid `Vector4` or Euclidean distance logic for high-level concepts; use `Rotor` and `Resonance`.

## 4. Documentation
- Respect the `SYSTEM_MAP.md` structure.
- Maintain the `docs/` hierarchy.
