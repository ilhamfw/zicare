from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.models.patient import Patient
from app.db import get_session

router = APIRouter()

# Mendapatkan informasi tentang satu pasien berdasarkan ID
@router.get("/patients/{patient_id}", response_model=Patient)
def read_patient(patient_id: int, db: Session = Depends(get_session)):
    patient = db.exec(select(Patient).where(Patient.patient_id == patient_id)).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# Mendapatkan informasi tentang semua pasien
@router.get("/patients", response_model=list[Patient])
def read_all_patients(db: Session = Depends(get_session)):
    patients = db.exec(select(Patient)).all()
    return patients

# Menambahkan data pasien baru
@router.post("/patients", response_model=Patient)
def create_patient(patient: Patient, db: Session = Depends(get_session)):
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

# Memperbarui data pasien berdasarkan ID
@router.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, updated_patient: Patient, db: Session = Depends(get_session)):
    patient = db.exec(select(Patient).where(Patient.patient_id == patient_id)).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    for key, value in updated_patient.dict().items():
        setattr(patient, key, value)
    
    db.commit()
    db.refresh(patient)
    return patient

# Menghapus pasien berdasarkan ID
@router.delete("/patients/{patient_id}", response_model=Patient)
def delete_patient(patient_id: int, db: Session = Depends(get_session)):
    patient = db.exec(select(Patient).where(Patient.patient_id == patient_id)).first()
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    db.delete(patient)
    db.commit()
    return patient
