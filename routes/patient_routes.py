from fastapi import APIRouter, HTTPException, Depends #Depends allows you to share db connection function(get_db) accross api endpoints
#APIRouter for grouping related API endpoints together(instead of all into one file main.py-organize into separate files)
from db import get_db,PatientDB
from classes import PatientCreate, PatientUpdate, PatientOut
from sqlalchemy.orm import Session


router=APIRouter(prefix="/api/patients", tags=["Patients"])#prefix so we dont have to write it for all apis and tag to group endpoints in swagger

@router.get("/", response_model=list[PatientOut])
def list_patients(db: Session=Depends(get_db)):
    return db.query(PatientDB).all() #Returns all patients

@router.get("/{patient_id}", response_model=PatientOut)
def get_patient(patient_id: str, db: Session=Depends(get_db)):
    patient=db.query(PatientDB).filter(PatientDB.id==patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.post("/", response_model=PatientCreate, status_code=201) #201 for successful creation
def add_patient(body: PatientCreate, db:Session=Depends(get_db)):  #Creates a new patient
    newPatient=PatientDB(**body.model_dump()) #converts API req to db ready obj
    db.add(newPatient)
    db.commit() #saves the changes
    db.refresh(newPatient) #reloads the updated version
    return newPatient

@router.put("/{patient_id}", response_model=PatientOut)
def update_patient(patient_id:str, body: PatientUpdate, db:Session=Depends(get_db)): 
    patient=db.query(PatientDB).filter(PatientDB.id==patient_id).first()
    if not patient:
         raise HTTPException(status_code=404, detail="Patient id not found")
    for key, value in body.model_dump().items(): #loops through all incoming fields in the update request
        setattr(patient, key, value) #sets attributes on an object
    db.commit()
    db.refresh(patient)
    return patient
    

@router.delete("/{patient_id}")
def delete_patient(patient_id:str, db:Session=Depends(get_db)): #Deletes patient by its UUID
    patient=db.query(PatientDB).filter(PatientDB.id==patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient Id not found")
    db.delete(patient)
    db.commit()
    return {"detail": "Patient deleted successfully"}

