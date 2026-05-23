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

        for _, data in agent_outputs.items():

            agent = data["agent"]
            output = data["output"]

            if not output:
                continue

            if agent == "rag_agent":
                structured["summary"] += "\n" + output

            elif agent == "risk_agent":
                structured["risks"] += "\n" + output

            elif agent == "action_agent":
                structured["actions"] += "\n" + output

        logger.info("Aggregation complete")

        return structured
