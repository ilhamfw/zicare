# routes/clinic.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List
from app.models.clinic import Clinic
from app.db import get_session

router = APIRouter()

@router.get("/clinics/{clinic_id}", response_model=Clinic)
def read_clinic(clinic_id: int, db: Session = Depends(get_session)):
    clinic = db.exec(select(Clinic).where(Clinic.clinic_id == clinic_id)).first()
    if clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    return clinic

@router.get("/clinics", response_model=List[Clinic])
def read_all_clinics(db: Session = Depends(get_session)):
    clinics = db.exec(select(Clinic)).all()
    return clinics

@router.post("/clinics", response_model=Clinic)
def create_clinic(clinic: Clinic, db: Session = Depends(get_session)):
    db.add(clinic)
    db.commit()
    db.refresh(clinic)
    return clinic

@router.put("/clinics/{clinic_id}", response_model=Clinic)
def update_clinic(clinic_id: int, updated_clinic: Clinic, db: Session = Depends(get_session)):
    clinic = db.exec(select(Clinic).where(Clinic.clinic_id == clinic_id)).first()
    if clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    for key, value in updated_clinic.dict().items():
        setattr(clinic, key, value)
    db.commit()
    db.refresh(clinic)
    return clinic

@router.delete("/clinics/{clinic_id}", response_model=Clinic)
def delete_clinic(clinic_id: int, db: Session = Depends(get_session)):
    clinic = db.exec(select(Clinic).where(Clinic.clinic_id == clinic_id)).first()
    if clinic is None:
        raise HTTPException(status_code=404, detail="Clinic not found")
    db.delete(clinic)
    db.commit()
    return clinic
