from sqlalchemy.orm import Session

from app import models, schemas


def create_ticket(db: Session, ticket_in: schemas.TicketCreate) -> models.Ticket:
    ticket = models.Ticket(
        title=ticket_in.title,
        description=ticket_in.description,
        status=models.TicketStatus.open,
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def get_tickets(db: Session) -> list[models.Ticket]:
    return db.query(models.Ticket).all()


def get_ticket(db: Session, ticket_id: int) -> models.Ticket | None:
    return db.query(models.Ticket).filter(models.Ticket.id == ticket_id).first()


def update_ticket(
    db: Session,
    ticket: models.Ticket,
    ticket_in: schemas.TicketUpdate,
) -> models.Ticket:
    ticket.title = ticket_in.title
    ticket.description = ticket_in.description
    ticket.status = ticket_in.status
    db.commit()
    db.refresh(ticket)
    return ticket


def close_ticket(db: Session, ticket: models.Ticket) -> models.Ticket:
    ticket.status = models.TicketStatus.closed
    db.commit()
    db.refresh(ticket)
    return ticket