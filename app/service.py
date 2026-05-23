from app.orchestrator.planner import Planner
from app.orchestrator.router import Router

from app.utils.logger import get_logger

logger = get_logger(__name__)


class OrchestratorService:

    @staticmethod
    def process(query: str, file_path: str = None):

        if not query or not query.strip():
            return {
                "status": "error",
                "message": "empty query"
            }

        try:

            strategy, tasks = Planner.create_plan(query)

            routing = Router.route(tasks)

            return {
                "status": "success",
                "strategy": strategy,
                "tasks": tasks,
                "routing": routing
            }

        except Exception as e:

            logger.error(f"Orchestration failed: {e}")

            return {
                "status": "error",
                "message": str(e)
            }
