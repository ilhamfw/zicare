from fastapi import FastAPI
from app.routes import clinic, patient, schedule, reservation  # Sesuaikan dengan rute yang Anda miliki

app = FastAPI()

# Menambahkan rute-rute ke aplikasi
app.include_router(clinic.router)
app.include_router(patient.router)
app.include_router(schedule.router)
app.include_router(reservation.router)

if __name__ == "__main__":
    import uvicorn

    # Menjalankan aplikasi menggunakan Uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
