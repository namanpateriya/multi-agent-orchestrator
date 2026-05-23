# Multi-Agent Orchestrator

Multi-Agent Orchestrator is a purpose-driven AI system that simulates a Program Management Copilot using multiple collaborating agents.

It combines:
- task decomposition
- agent-based execution
- document-aware reasoning (RAG)
- structured aggregation
- evaluation and optimization

---

# Features

- Deterministic task decomposition (planner)
- Intelligent agent routing
- Multi-agent execution (RAG, Risk, Action)
- Real document-based RAG pipeline
- Context-grounded reasoning
- Structured aggregation layer
- Executive-ready output generation
- CLI and API support
- Multi-agent evaluation and optimization

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

# System Capabilities

This system demonstrates:

- task decomposition and orchestration
- multi-agent collaboration
- document-aware reasoning (RAG)
- structured business insights generation
- evaluation-driven AI improvement loop

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
    ├── RAG Agent (real retrieval pipeline)
    ├── Risk Agent
    ├── Action Agent
    ↓
Aggregator
    ↓
Summarizer Agent
    ↓
Final Output
```

---

# RAG Integration

The system includes a real Retrieval-Augmented Generation (RAG) pipeline:

- PDF ingestion using PyMuPDF
- semantic chunking
- embedding generation (sentence-transformers)
- cosine similarity retrieval
- context-grounded answer generation

This is used inside the RAG Agent to provide document-aware insights.

---

# Setup

```bash
git clone <repo_url>
cd multi-agent-orchestrator
pip install -r requirements.txt
```

Create `.env` file:

```text
GEMINI_API_KEY=your_api_key
MODEL_NAME=gemini-1.5-flash
```

---

# API Usage

```bash
uvicorn app.main:app --reload
```

Example:

```json
POST /plan
{
  "query": "Summarize project and highlight risks and next actions"
}
```

---

# CLI Usage

```bash
python -m app.cli --query "Summarize project and highlight risks and next actions"
```

With document:

```bash
python -m app.cli --query "Summarize project" --file data/sample.pdf
```

---

# Evaluation & Optimization

The system includes a multi-agent evaluation framework.

Run:

```bash
python -m evaluation.evaluator
```

Optimize:

```bash
python -m evaluation.optimizer
```

This enables:

```text
Build → Evaluate → Diagnose → Improve
```

---

# Engineering Highlights

- Multi-agent orchestration architecture
- Real RAG integration
- Deterministic planning and routing
- Structured aggregation
- Evaluation-driven system design
- Google Gemini integration

---

# Google Ecosystem Alignment

This repository aligns with modern AI system patterns using Google Gemini.

It demonstrates:
- multi-step reasoning
- agent-based workflows
- enterprise AI orchestration
- structured decision systems

---

# Limitations

- no persistent memory
- synchronous execution
- evaluation depends on embedding quality
- no UI interface

---

# Future Enhancements

- memory-enabled agents
- async orchestration
- UI interface
- multi-document workflows
- hybrid retrieval (BM25 + vector)

---

# Summary

This repository demonstrates:

```text
AI system that plans, delegates, executes, retrieves, and synthesizes results using multiple agents
```

---

Built using Google Gemini for multi-agent AI system design.
