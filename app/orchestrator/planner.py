from app.utils.logger import get_logger

logger = get_logger(__name__)


class Planner:

    @staticmethod
    def create_plan(query: str):

        q = query.lower()

        tasks = []

        if "summarize" in q or "summary" in q:
            tasks.append({"task_id": "1", "type": "summarize"})

        if any(k in q for k in ["risk", "issue", "blocker", "challenge"]):
            tasks.append({"task_id": str(len(tasks)+1), "type": "risk_analysis"})

        if any(k in q for k in ["action", "next step", "recommend"]):
            tasks.append({"task_id": str(len(tasks)+1), "type": "action_recommendation"})

        if not tasks:
            tasks.append({"task_id": "1", "type": "summarize"})

        strategy = "multi_step" if len(tasks) > 1 else "single_step"

        logger.info(f"Plan: {tasks}")

        return strategy, tasks
