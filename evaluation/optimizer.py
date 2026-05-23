from evaluation.evaluator import evaluate


def optimize():

    results = evaluate()

    issues = {
        "planning_errors": 0,
        "routing_errors": 0,
        "low_similarity": 0,
        "weak_risks": 0,
        "weak_actions": 0
    }

    for r in results:

        if not r["planning_correct"]:
            issues["planning_errors"] += 1

        if not r["routing_correct"]:
            issues["routing_errors"] += 1

        if r["similarity"] < 0.5:
            issues["low_similarity"] += 1

        if r["risk_score"] < 0.3:
            issues["weak_risks"] += 1

        if r["action_score"] < 0.3:
            issues["weak_actions"] += 1

    print("\n=== OPTIMIZATION REPORT ===\n")

    print(issues)

    print("\nRecommendations:\n")

    if issues["planning_errors"] > 0:
        print("- Improve planner rules (query parsing)")

    if issues["routing_errors"] > 0:
        print("- Improve router mapping logic")

    if issues["low_similarity"] > 0:
        print("- Improve summarizer prompt")

    if issues["weak_risks"] > 0:
        print("- Improve risk agent prompt")

    if issues["weak_actions"] > 0:
        print("- Improve action agent prompt")


if __name__ == "__main__":
    optimize()
