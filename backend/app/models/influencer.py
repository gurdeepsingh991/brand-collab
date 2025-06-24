from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey, Float, Text, Integer,Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from sqlalchemy.orm import relationship
import uuid
from app.db_base import Base

class InfluencerProfile(Base): 
    __tablename__= "influencer_profile"

    influencer_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    city = Column(String)
    country = Column(String)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="influencer")
    services = relationship("InfluencerService", back_populates="influencer")
    platforms = relationship("InfluencerPlatform", back_populates="influencer")
    applications = relationship("CollabApplication", back_populates="influencer")
