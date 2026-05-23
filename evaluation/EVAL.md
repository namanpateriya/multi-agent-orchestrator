# Multi-Agent Evaluation

This framework evaluates the performance of a multi-agent AI system.

---

# Evaluation Layers

The system evaluates multiple layers:

1. Planning Accuracy  
   - Correct task decomposition

2. Routing Accuracy  
   - Correct agent selection

3. Agent Output Quality  
   - Usefulness of intermediate outputs

4. Final Output Quality  
   - Coherence and completeness

5. RAG Quality  
   - Relevance of retrieved content  
   - Grounding of generated answers  

---

# Metrics

- Semantic similarity (final output vs expected)
- Risk coverage score
- Action coverage score
- Planning correctness
- Routing correctness
- Composite score

---

# Evaluation Flow

```text
Test Case
    ↓
Multi-Agent Execution
    ↓
Agent Outputs
    ↓
Aggregation
    ↓
Final Output
    ↓
Metric Computation
```

---

# Running Evaluation

```bash
python -m evaluation.evaluator
```

---

# Running Optimization

```bash
python -m evaluation.optimizer
```

---

# Evaluation Philosophy

This repository follows a system-level evaluation approach:

```text
Not just "Is the answer correct?"

But:
- Was the system thinking correct?
- Were the right steps taken?
- Were the right agents used?
```

---

# Goal

Enable:

```text
Build → Evaluate → Diagnose → Improve
```

for multi-agent AI systems.
