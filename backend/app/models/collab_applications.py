
from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey, Float, Text, Integer,Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.db_base import Base


class CollabApplication(Base):
    __tablename__ = "collab_applications"

    application_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    application_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    campaign_id = Column(UUID(as_uuid=True), ForeignKey("campaigns.campaign_id"))
    influencer_id = Column(UUID(as_uuid=True), ForeignKey("influencer_profile.influencer_id"))
    pitch = Column(Text)
    match_score = Column(Float)
    status = Column(String, default="pending")  # pending | approved | rejected
    applied_on = Column(DateTime, default=datetime.utcnow)

    campaign = relationship("Campaign", back_populates="applications")
    influencer = relationship("InfluencerProfile", back_populates="applications")