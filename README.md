# Multi-Agent Orchestrator

Multi-Agent Orchestrator is a purpose-driven AI system designed to simulate a Program Management Copilot using multiple collaborating agents.

It demonstrates how complex queries can be decomposed, routed, executed, and aggregated into structured business insights.

---

# Features

- Task decomposition using deterministic planning
- Agent-based execution (multi-agent system)
- Domain-specific agents for program management
- Structured aggregation of outputs
- Final executive-ready response generation
- CLI and API support
- Multi-agent evaluation and optimization framework

---

# Use Case

Program Management Copilot

Example query:

```text
Summarize project update and highlight risks and next actions
```

Output:

```text
Summary:
...

Key Risks:
- ...

Recommended Actions:
- ...
```

---

# Architecture Overview

```text
User Query
    ↓
Planner (task decomposition)
    ↓
Router (agent selection)
    ↓
Agents Execute
    ├── RAG Agent
    ├── Risk Agent
    ├── Action Agent
    ↓
Aggregator
    ↓
Summarizer Agent
    ↓
Final Structured Output
```

---

# Setup

Clone repository:

```bash
git clone <repo_url>
cd multi-agent-orchestrator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```text
GEMINI_API_KEY=your_api_key
MODEL_NAME=gemini-1.5-flash
```

---

# API Usage

Start server:

```bash
uvicorn app.main:app --reload
```

Endpoint:

```text
POST /plan
POST /execute (if extended)
```

Example request:

```json
{
  "query": "Summarize project and highlight risks and next actions"
}
```

---

# CLI Usage

Run from terminal:

```bash
python -m app.cli --query "Summarize project and highlight risks and next actions"
```

With document input:

```bash
python -m app.cli --query "Summarize project update" --file data/sample.pdf
```

---

# Evaluation & Optimization

This repository includes a multi-agent evaluation framework.

It evaluates:

- planning accuracy
- routing accuracy
- agent output quality
- final response quality

Run evaluation:

```bash
python -m evaluation.evaluator
```

Run optimization:

```bash
python -m evaluation.optimizer
```

---

# Engineering Highlights

- Multi-agent orchestration architecture
- Deterministic planning and routing
- Domain-specific agent design
- Structured aggregation layer
- Evaluation-driven AI system design
- Google Gemini integration

---

# Google Ecosystem Alignment

This repository aligns with modern AI system design patterns used with Google Gemini.

It demonstrates:

- multi-step reasoning
- agent-based workflows
- structured AI orchestration
- enterprise AI use cases

---

# Design Philosophy

This system is built as:

```text
modular, explainable, and production-minded AI system
```

Key principles:

- clarity over complexity
- deterministic orchestration
- reusable agent design
- measurable outputs

---

# Limitations

- no persistent memory
- no real document RAG integration (simplified in agents)
- evaluation depends on embedding quality
- no UI interface

---

# Future Enhancements

- integrate full RAG pipeline (Week 4 reuse)
- add memory-enabled agents
- introduce async agent execution
- build UI interface
- add multi-document workflows

---

# Summary

This repository demonstrates how to build:

```text
AI system that plans, delegates, executes, and synthesizes results using multiple agents
```

---

Built using Google Gemini for multi-agent AI system design.
