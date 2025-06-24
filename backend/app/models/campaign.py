from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey, Float, Text, Integer,Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.db_base import Base

class Campaign(Base):
    __tablename__ = "campaigns"
    
    campaign_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand_id = Column(ForeignKey("brand_profile.brand_id"), nullable=False)
    
    title = Column(String, nullable=False)
    description = Column(Text)
    target_platform = Column(String)
    budget = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    goals = Column(Text)
    priority = Column(String, default="normal")
    
    brand = relationship("BrandProfile", back_populates="campaigns")
