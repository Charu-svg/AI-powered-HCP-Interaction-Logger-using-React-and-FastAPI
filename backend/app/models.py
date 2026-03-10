from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String, nullable=False)
    interaction_type = Column(String, nullable=False)
    notes = Column(String, nullable=False)
    ai_summary = Column(String, nullable=True)
    engagement_score = Column(Integer, default=0)
    products_discussed = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())