from sqlmodel import SQLModel

class Reservation(SQLModel):
    reservation_id: int = None
    patient_id: int
    schedule_id: int
    reservation_date: str
    queue_number: int
