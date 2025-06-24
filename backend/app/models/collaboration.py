from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey, Float, Text, Integer,Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.db_base import Base

class Collaboration(Base):
    __tablename__ = "collaborations"

    collaboration_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    application_id = Column(UUID(as_uuid=True), ForeignKey("collab_applications.application_id"), unique=True)
    deliverables = Column(Text)
    agreed_budget = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String, default="active")  # active | completed | cancelled

    application = relationship("CollabApplication")