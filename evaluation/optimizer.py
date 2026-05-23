from evaluation.evaluator import evaluate


def optimize():

    results = evaluate()

    for r in results:

        print(f"\nCase {r['id']}")

        if r["similarity"] < 0.5:
            print("- Improve summarizer prompt")

        if r["risk_coverage"] < 0.5:
            print("- Improve risk agent")

        if r["action_coverage"] < 0.5:
            print("- Improve action agent")
