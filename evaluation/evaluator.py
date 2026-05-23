import json

from evaluation.metrics import (
    semantic_similarity,
    list_coverage
)

from app.service import OrchestratorService


def evaluate():

    with open("evaluation/test_cases.json") as f:
        cases = json.load(f)

    results = []

    print("\n=== MULTI-AGENT EVALUATION ===\n")

    for case in cases:

        result = OrchestratorService.process(
            case["query"],
            case.get("file_path")
        )

        final_output = result.get("final_output", "")
        structured = result.get("structured", {})

        # --- Metrics ---

        similarity = semantic_similarity(
            final_output,
            case.get("expected_output", "")
        )

        risk_score = list_coverage(
            structured.get("risks", ""),
            case.get("expected_risks", [])
        )

        action_score = list_coverage(
            structured.get("actions", ""),
            case.get("expected_actions", [])
        )

        planning_correct = set(
            [t["type"] for t in result.get("tasks", [])]
        ) == set(case.get("expected_tasks", []))

        routing_correct = set(
            [r["agent"] for r in result.get("routing", [])]
        ) == set(case.get("expected_agents", []))

        overall_pass = (
            similarity > 0.5 and
            risk_score > 0.3 and
            action_score > 0.3
        )

        case_result = {
            "id": case["id"],
            "similarity": round(similarity, 3),
            "risk_score": round(risk_score, 3),
            "action_score": round(action_score, 3),
            "planning_correct": planning_correct,
            "routing_correct": routing_correct,
            "passed": overall_pass
        }

        results.append(case_result)

        print(case["id"], case_result)

    return results


if __name__ == "__main__":
    evaluate()
