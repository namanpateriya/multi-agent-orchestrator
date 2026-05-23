import json
from sentence_transformers import SentenceTransformer
import numpy as np

from app.service import OrchestratorService

model = SentenceTransformer("all-MiniLM-L6-v2")


def similarity(a, b):
    emb = model.encode([a, b])
    return float(np.dot(emb[0], emb[1]) /
                 (np.linalg.norm(emb[0])*np.linalg.norm(emb[1])))


def evaluate():

    with open("evaluation/test_cases.json") as f:
        cases = json.load(f)

    results = []

    for c in cases:

        res = OrchestratorService.process(
            c["query"],
            c.get("file_path")
        )

        structured = res.get("structured") or {}
        final = res.get("final_output", "")

        sim = similarity(final, c["expected_output"])

        risk_cov = sum(
            k in structured.get("risks", "").lower()
            for k in c["expected_risks"]
        ) / len(c["expected_risks"])

        action_cov = sum(
            k in structured.get("actions", "").lower()
            for k in c["expected_actions"]
        ) / len(c["expected_actions"])

        score = (sim + risk_cov + action_cov) / 3

        results.append({
            "id": c["id"],
            "similarity": sim,
            "risk_coverage": risk_cov,
            "action_coverage": action_cov,
            "score": score
        })

        print(results[-1])

    return results
