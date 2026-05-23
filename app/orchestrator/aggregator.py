from app.utils.logger import get_logger

logger = get_logger(__name__)


class Aggregator:

    @staticmethod
    def collect(agent_outputs):

        structured = {
            "summary": "",
            "risks": "",
            "actions": ""
        }

        for task_id, data in agent_outputs.items():

            agent = data["agent"]
            output = data["output"]

            if agent == "rag_agent":
                structured["summary"] = output

            elif agent == "risk_agent":
                structured["risks"] = output

            elif agent == "action_agent":
                structured["actions"] = output

        logger.info("Aggregation complete")

        return structured
