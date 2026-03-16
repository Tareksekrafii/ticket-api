import enum
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, Integer, String

from app.db import Base


class TicketStatus(str, enum.Enum):
    open = "open"
    stalled = "stalled"
    closed = "closed"


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(TicketStatus), nullable=False, default=TicketStatus.open)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)