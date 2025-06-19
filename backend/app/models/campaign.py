from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey,relationship, Float, Text, Integer,Date
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from app.db import Base



class Campaign(Base):
    __tablename__ = "campaigns"
    
    id = Column(Integer, primary_key=True)
    brand_id = Column(ForeignKey("brand_profile.id"), nullable=False)
    
    title = Column(String, nullable=False)
    description = Column(Text)
    target_platform = Column(String)
    budget = Column(Float)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    goals = Column(Text)
    
    brand = relationship("BrandProfile", back_populates="campaigns")
