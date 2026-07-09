from fastapi import APIRouter, HTTPException,Depends #API Router for grouping, HTTP Exception for errors
from db import DoctorDB, get_db
from classes import DoctorCreate, DoctorOut, DoctorUpdate
from sqlalchemy.orm import Session

router=APIRouter(prefix="/api/doctors", tags=["Doctors"])

@router.get("/", response_model=list[DoctorOut])
def list_doctors(db:Session=Depends(get_db)):
    return db.query(DoctorDB).all() #Returns all doctors

@router.get("/{doctor_id}", response_model=DoctorOut)
def get_doctor(doctor_id: str, db: Session=Depends(get_db)):
    doctor=db.query(DoctorDB).filter(DoctorDB.id==doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor id not found")
    return doctor

@router.post("/", response_model=DoctorOut, status_code=201)
def add_doctor(body: DoctorCreate, db:Session=Depends(get_db)):
    newDoctor=DoctorDB(**body.model_dump()) #converts API req into db ready object
    db.add(newDoctor)
    db.commit()
    db.refresh(newDoctor)
    return newDoctor

@router.put("/{doctor_id}", response_model=DoctorOut)
def update_doctor(doctor_id: str, body: DoctorUpdate, db: Session=Depends(get_db)):
    doctor=db.query(DoctorDB).filter(DoctorDB.id==doctor_id).first()
    if not doctor:
         raise HTTPException(status_code=404, detail="Doctor id not found")
    for key, value in body.model_dump().items(): #loops through all incoming objects in update req
        setattr(doctor,key,value) #sets attributes to objects
    db.commit()
    db.refresh(doctor)
    return doctor

@router.delete("/{doctor_id}")
def delete_doctor(doctor_id: str, db: Session=Depends(get_db)):
    doctor=db.query(DoctorDB).filter(DoctorDB.id==doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor id not found")
    db.delete(doctor)
    db.commit()
    return {"detail":"Doctor deleted successfully"}