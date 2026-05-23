from app.utils.logger import get_logger

logger = get_logger(__name__)


class Router:

    @staticmethod
    def route(tasks):

        routing = []

        for task in tasks:

            task_type = task["type"]

            if task_type == "summarize":
                agent = "rag_agent"

            elif task_type == "risk_analysis":
                agent = "risk_agent"

            elif task_type == "action_recommendation":
                agent = "action_agent"

            else:
                agent = "rag_agent"

            routing.append({
                "task_id": task["task_id"],
                "agent": agent
            })

        logger.info(f"Routing: {routing}")

        return routing
