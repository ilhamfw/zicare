from sqlmodel import SQLModel

class Patient(SQLModel):
    patient_id: int = None
    full_name: str
    date_of_birth: str
    gender: str
