from app.utils.logger import get_logger

logger = get_logger(__name__)


class Planner:

    @staticmethod
    def create_plan(query: str):

        query_lower = query.lower()

        tasks = []

        # Rule-based planning (stable + deterministic)

        if "summarize" in query_lower:
            tasks.append({
                "task_id": "1",
                "type": "summarize"
            })

        if "risk" in query_lower:
            tasks.append({
                "task_id": str(len(tasks) + 1),
                "type": "risk_analysis"
            })

        if "action" in query_lower or "next step" in query_lower:
            tasks.append({
                "task_id": str(len(tasks) + 1),
                "type": "action_recommendation"
            })

        # Default fallback
        if not tasks:
            tasks.append({
                "task_id": "1",
                "type": "summarize"
            })

        strategy = "multi_step" if len(tasks) > 1 else "single_step"

        logger.info(f"Plan created: {tasks}")

        return strategy, tasks
