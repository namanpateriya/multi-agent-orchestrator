from app.orchestrator.planner import Planner
from app.orchestrator.router import Router

from app.agents.rag_agent import RAGAgent
from app.agents.risk_agent import RiskAgent
from app.agents.action_agent import ActionAgent

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

            agent_outputs = {}

            for route in routing:

                task_id = route["task_id"]
                agent_name = route["agent"]

                if agent_name == "rag_agent":
                    output = RAGAgent.execute(query, file_path)

                elif agent_name == "risk_agent":
                    output = RiskAgent.execute(query)

                elif agent_name == "action_agent":
                    output = ActionAgent.execute(query)

                else:
                    output = "unsupported agent"

                agent_outputs[task_id] = {
                    "agent": agent_name,
                    "output": output
                }

            return {
                "status": "success",
                "strategy": strategy,
                "tasks": tasks,
                "routing": routing,
                "agent_outputs": agent_outputs
            }

        except Exception as e:

            logger.error(f"Execution failed: {e}")

            return {
                "status": "error",
                "message": str(e)
            }
