# app/models/user.py

from sqlalchemy import Column, String, Boolean, DateTime 
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.db import Base


class User(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String)
    middle_name = Column(String)
    last_name = Column(String)
    role = Column(String)  # e.g. brand, influencer, admin
    created_on = Column(DateTime, default=datetime.utcnow)
    user_type = Column(String)
    is_active = Column(Boolean, default=True)

    brand = relationship("BrandProfile", back_populates="user", uselist=False)
    influencer = relationship("InfluencerProfile", back_populates="user", uselist=False)


