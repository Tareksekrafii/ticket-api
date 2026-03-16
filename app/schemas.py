from datetime import datetime

from pydantic import BaseModel, Field

from app.models import TicketStatus


class TicketCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)


class TicketUpdate(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)
    description: str = Field(..., min_length=1)
    status: TicketStatus


class TicketRead(BaseModel):
    id: int
    title: str
    description: str
    status: TicketStatus
    created_at: datetime

    class Config:
        from_attributes = True