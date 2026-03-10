from pydantic import BaseModel
from datetime import datetime

class InteractionCreate(BaseModel):
    doctor_name: str
    interaction_type: str
    notes: str

class Interaction(BaseModel):
    id: int
    doctor_name: str
    interaction_type: str
    notes: str
    ai_summary: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True