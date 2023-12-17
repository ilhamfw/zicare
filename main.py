
from fastapi import FastAPI
from app.routes import clinic, patient, schedule, reservation

app = FastAPI()

app.include_router(clinic.router, prefix="/clinics", tags=["clinics"])
app.include_router(patient.router, prefix="/patients", tags=["patients"])
app.include_router(schedule.router, prefix="/schedules", tags=["schedules"])
app.include_router(reservation.router, prefix="/reservations", tags=["reservations"])
