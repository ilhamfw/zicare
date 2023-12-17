# routes/schedule.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.schedule import Schedule
from app.db import get_session

router = APIRouter()

@router.get("/schedules/{schedule_id}", response_model=Schedule)
def read_schedule(schedule_id: int, db: Session = Depends(get_session)):
    schedule = db.exec(select(Schedule).where(Schedule.schedule_id == schedule_id)).first()
    if schedule is None:
        raise HTTPException(status_code=404, detail="Schedule not found")
    return schedule
