from app.orchestrator.planner import Planner
from app.orchestrator.router import Router
from app.orchestrator.aggregator import Aggregator

from app.agents.rag_agent import RAGAgent
from app.agents.risk_agent import RiskAgent
from app.agents.action_agent import ActionAgent
from app.agents.summarizer_agent import SummarizerAgent

from app.utils.logger import get_logger

logger = get_logger(__name__)


class OrchestratorService:

    @staticmethod
    def process(query: str, file_path: str = None):

        if not query.strip():
            return {"status": "error", "message": "empty query"}

        try:

            strategy, tasks = Planner.create_plan(query)
            routing = Router.route(tasks)

            agent_outputs = {}

            for r in routing:

                agent = r["agent"]

                if agent == "rag_agent":
                    out = RAGAgent.execute(query, file_path)

                elif agent == "risk_agent":
                    out = RiskAgent.execute(query)

                elif agent == "action_agent":
                    out = ActionAgent.execute(query)

                else:
                    out = "unsupported"

                if isinstance(out, str) and out.startswith("error"):
                    return {"status": "error", "message": out}

                agent_outputs[r["task_id"]] = {
                    "agent": agent,
                    "output": out
                }

            structured = Aggregator.collect(agent_outputs)

            final = SummarizerAgent.execute(structured)

            return {
                "status": "success",
                "strategy": strategy,
                "final_output": final,
                "structured": structured
            }

        except Exception as e:
            logger.error(e)
            return {"status": "error", "message": str(e)}
