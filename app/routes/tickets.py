from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.db import get_db

router = APIRouter(prefix="/tickets", tags=["tickets"])


@router.post("/", response_model=schemas.TicketRead,
             status_code=status.HTTP_201_CREATED)
def create_ticket(ticket_in: schemas.TicketCreate, db: Session = Depends(get_db)):
    return crud.create_ticket(db, ticket_in)


@router.get("/", response_model=list[schemas.TicketRead])
def list_tickets(db: Session = Depends(get_db)):
    return crud.get_tickets(db)


@router.get("/{ticket_id}", response_model=schemas.TicketRead)
def get_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return ticket


@router.put("/{ticket_id}", response_model=schemas.TicketRead)
def update_ticket(ticket_id: int, ticket_in: schemas.TicketUpdate,
                  db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return crud.update_ticket(db, ticket, ticket_in)


@router.patch("/{ticket_id}/close", response_model=schemas.TicketRead)
def close_ticket(ticket_id: int, db: Session = Depends(get_db)):
    ticket = crud.get_ticket(db, ticket_id)
    if not ticket:
        raise HTTPException(status_code=404, detail="Ticket not found")
    return crud.close_ticket(db, ticket)