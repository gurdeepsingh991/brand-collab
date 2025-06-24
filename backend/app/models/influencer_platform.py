
from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey, Float, Text, Integer,Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.db_base import Base


class InfluencerPlatform(Base):
    __tablename__ = "influencer_platforms"

    platform_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    influencer_id = Column(UUID(as_uuid=True), ForeignKey("influencer_profile.influencer_id"))
    platform_name = Column(String, nullable=False)  # e.g. Instagram, TikTok
    no_of_followers = Column(Integer)
    no_of_subscribers = Column(Integer)
    engagement_rate = Column(Float)
    is_primary = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    influencer = relationship("InfluencerProfile", back_populates="platforms")