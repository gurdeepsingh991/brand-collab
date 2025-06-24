from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey, Float, Text, Integer,Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.db_base import Base

class InfluencerService(Base):
    __tablename__ = "influencer_services"

    service_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    influencer_id = Column(UUID(as_uuid=True), ForeignKey("influencer_profile.influencer_id"))
    service_type = Column(String, nullable=False)  # e.g. product_review, mention
    charges_per_hour = Column(Float)
    currency = Column(String)
    is_active = Column(Boolean, default=True)

    influencer = relationship("InfluencerProfile", back_populates="services")