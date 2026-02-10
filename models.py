from pydantic import BaseModel
from typing import List, Optional

class AssignmentRequest(BaseModel):
    project_id: str
    skill: Optional[str] = None
    capability: Optional[str] = None
    location: Optional[str] = None

class AssignmentResponse(BaseModel):
    status: str
    pilot_id: Optional[str] = None
    drone_id: Optional[str] = None
    issues: List[str] = []
