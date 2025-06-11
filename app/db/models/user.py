from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.db.base_class import Base
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    # Relationships
    participant_rooms = relationship("RoomParticipant", back_populates="user")
    sent_messages = relationship("ChatMessage", back_populates="sender")