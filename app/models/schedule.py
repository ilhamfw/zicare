from sqlmodel import SQLModel

class Schedule(SQLModel):
    schedule_id: int = None
    clinic_id: int
    day_of_week: str
    start_time: str
    end_time: str
