import argparse
import json

from app.service import OrchestratorService


def pretty_print(result):

    print("\n=== MULTI-AGENT OUTPUT ===\n")

    if result.get("status") != "success":
        print("Error:", result.get("message"))
        return

    print("Strategy:", result.get("strategy"))

    print("\n--- Summary ---")
    print(result.get("structured", {}).get("summary", ""))

    print("\n--- Risks ---")
    print(result.get("structured", {}).get("risks", ""))

    print("\n--- Actions ---")
    print(result.get("structured", {}).get("actions", ""))

    print("\n--- Full Output ---")
    print(result.get("final_output", ""))


def main():

    parser = argparse.ArgumentParser(
        description="Multi-Agent Orchestrator CLI"
    )

    parser.add_argument(
        "--query",
        required=True,
        help="User query"
    )

    parser.add_argument(
        "--file",
        required=False,
        help="Optional document path"
    )

    args = parser.parse_args()

    result = OrchestratorService.process(
        query=args.query,
        file_path=args.file
    )

    pretty_print(result)


if __name__ == "__main__":
    main()
