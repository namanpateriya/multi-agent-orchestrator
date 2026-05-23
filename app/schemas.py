class OrchestratorResponse(BaseModel):

    status: str
    strategy: str
    tasks: list
    final_output: str
    structured: dict
