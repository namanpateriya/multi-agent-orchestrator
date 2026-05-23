from fastapi import FastAPI

from app.schemas import (
    OrchestratorRequest,
    OrchestratorResponse
)

from app.service import OrchestratorService

app = FastAPI(
    title="Multi-Agent Orchestrator - Step 1"
)


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/plan", response_model=OrchestratorResponse)
def plan(request: OrchestratorRequest):

    return OrchestratorService.process(
        request.query,
        request.file_path
    )
