from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.db.base_class import Base

class RoomParticipant(Base):
    __tablename__ = "room_participants"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    room_id = Column(Integer, ForeignKey("chat_rooms.id"))
    joined_at = Column(DateTime, default=datetime.utcnow)
    # Relationships
    user = relationship("User", back_populates="participant_rooms")
    room = relationship("ChatRoom", back_populates="participants")