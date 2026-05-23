class OrchestratorResponse(BaseModel):

    status: str
    strategy: str
    tasks: list
    routing: list
    agent_outputs: dict
