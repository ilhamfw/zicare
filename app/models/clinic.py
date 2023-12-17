from sqlmodel import SQLModel

class Clinic(SQLModel):
    clinic_id: int = None
    clinic_name: str
