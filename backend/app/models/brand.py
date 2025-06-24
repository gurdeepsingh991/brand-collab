from sqlalchemy import Column, String, Boolean, DateTime,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from app.db_base import Base

class BrandProfile(Base): 
    __tablename__= "brand_profile"

    brand_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    brand_name = Column(String, nullable=False)
    brand_industry = Column(String)
    brand_type = Column(String)
    country = Column(String)
    segment = Column(String)
    created_on = Column(DateTime, default=datetime.utcnow)
    created_by = Column(UUID(as_uuid=True), ForeignKey("users.user_id"))
    last_modified_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_modified_by = Column(String)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="brand")
    campaigns = relationship("Campaign",back_populates ="brand")