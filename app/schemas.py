from pydantic import BaseModel
from typing import List, Dict


class OrchestratorRequest(BaseModel):

    query: str
    file_path: str | None = None


class Task(BaseModel):

    task_id: str
    type: str


class OrchestratorResponse(BaseModel):

    status: str
    strategy: str
    tasks: List[Dict]
    routing: List[Dict]
