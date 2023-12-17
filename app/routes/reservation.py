# routes/reservation.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.reservation import Reservation
from app.db import get_session

router = APIRouter()

@router.get("/reservations/{reservation_id}", response_model=Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(get_session)):
    reservation = db.exec(select(Reservation).where(Reservation.reservation_id == reservation_id)).first()
    if reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation
