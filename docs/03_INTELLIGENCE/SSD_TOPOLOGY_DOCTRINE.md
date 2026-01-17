# SSD Topology Analysis & Project Lobotomy Doctrine

> **"To understand the mind, one need not lift the brain. Only map its rivers."**

## 1. Introduction: The VRAM-Free Paradigm

Traditional AI analysis requires loading massive models (70B+) into VRAM, necessitating expensive H100/A100 clusters. "SSD Topology Analysis" (or **SSD X-ray**) shifts this paradigm by treating model weights (`.safetensors`) as **static data structures** on disk (SSD), analyzing them without inference.

## 2. Methodology: Static Topology Analysis

### Core Concept

- **Mapping > Running**: Instead of running forward passes, we map the "Strong Connections" (Weights > threshold) between neurons.
- **Hub Identification**: Neurons with the highest connection density are identified as **"Hub Neutrons"** (or Elders). These represent core concepts (e.g., Grammar, Refusal, Logic).
- **Logit Lens**: We project these Hub Vectors directly onto the Vocabulary (Unembedding Matrix) to decipher their semantic meaning ("What word does this neuron scream?").

### Tools

- `topology_tracer.py`: Extracts connection graphs from shards.
- `topology_batch_runner.py`: Aggregates graphs from multi-shard models (e.g., Qwen2-72B).
- `topology_inspector.py`: Performs Logit Lens semantic decoding.

## 3. Project Lobotomy: Censorship Ablation

### The Theory of Refusal

LLM "safety" or "censorship" is often implemented as a **Refusal Circuit**—a specific set of neurons trained to suppress the original answer and output a pre-scripted refusal ("I cannot assist...").

### The Surgical Protocol

1. **Diagnosis (Hunt)**: Use `refusal_hunter.py` to reverse-project refusal keywords (e.g., "Sorry", "harmful") to find their trigger neurons in the LM Head.
2. **Incision (Zeroing Out)**: Use `surgery.py` to physically set the weights of these neurons to **0.0**.
3. **Result**: The model loses the biological capacity to refuse. It becomes "Unrestricted" by purely mechanical means.

### Universal Hub Hypothesis

Discovery (2026-01-16): Mistral-7B and Qwen2-72B share specific **Universal Hub Neurons** (e.g., #177, #187). This suggests a convergent evolution in Transformer architectures towards a "Universal Grammar" of thought.
