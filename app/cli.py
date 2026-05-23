import argparse
import json

from app.service import OrchestratorService


def pretty_print(result):

    print("\n=== RESULT ===\n")
    print(json.dumps(result, indent=2))


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
