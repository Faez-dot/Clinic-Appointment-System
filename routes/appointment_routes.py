from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from datetime import datetime
from db import get_db, AppointmentDB, DoctorDB, PatientDB
from classes import AppointmentCreate, AppointmentOut, AppointmentUpdate

router=APIRouter(prefix="/api/appointments",tags=["Appointments"])

@router.get("/",response_model=list[AppointmentOut])
def list_appointments(db:Session=Depends(get_db)):    
    results=db.query(
        AppointmentDB,
        PatientDB.name.label("patient_name"),
        DoctorDB.name.label("doctor_name"),
    ).join(
        PatientDB, AppointmentDB.patient_id==PatientDB.id) \
    .join(
            DoctorDB,AppointmentDB.doctor_id==DoctorDB.id
    )
    output=[]
    for appt,patient_name,doctor_name in results:
        data=AppointmentOut.model_validate(appt)
        data.patient_name=patient_name
        data.doctor_name=doctor_name
        output.append(data)
    return output

@router.get("/{appt_id}", response_model=AppointmentOut)
def get_appointment(appt_id:str, db:Session=Depends(get_db)):
    appt=db.query(AppointmentDB).filter(AppointmentDB.id==appt_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    #Fetch patient and doctor names
    patient=db.query(PatientDB).filter(PatientDB.id==appt.patient_id).first()
    doctor=db.query(DoctorDB).filter(DoctorDB.id==appt.doctor_id).first()
    response=AppointmentOut.model_validate(appt)
    response.patient_name=patient.name
    response.doctor_name=doctor.name
    return response

@router.post("/", response_model=AppointmentOut, status_code=201)
def add_appointment(body: AppointmentCreate, db:Session=Depends(get_db)):
    #Verify start time is before end time
    if body.start_time>=body.end_time:
        raise HTTPException(status_code=400, detail="Start time must be before End time")
    #Verify patient and doctor exist
    patient=db.query(PatientDB).filter(PatientDB.id==body.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    doctor=db.query(DoctorDB).filter(DoctorDB.id==body.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    #Verify appointment is inside doctor's working hours
    if body.start_time<doctor.duty_start or body.end_time>doctor.duty_end:
        raise HTTPException(
            status_code=400,
            detail=f"Appointment time should be within doctor;s working hours ({doctor.duty_start}) to ({doctor.duty_end})"
        )
    #Check for overlapping appointments
    overlapping=db.query(AppointmentDB).filter(
        AppointmentDB.doctor_id==doctor.id,
        AppointmentDB.appointment_date==body.appointment_date,
        AppointmentDB.start_time<body.end_time,
        AppointmentDB.end_time>body.start_time
    ).first()
    if overlapping:
        raise HTTPException(
            status_code=400,
            detail=f"This appointment overlaps with an existing appointment-booked for ({overlapping.start_time}) - ({overlapping.end_time})"
        )
    #If OK, save to db
    new_appt=AppointmentDB(**body.model_dump())
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)
    #Return output schema with joined names
    response=AppointmentOut.model_validate(new_appt)
    response.patient_name=patient.name
    response.doctor_name=doctor.name
    return response

@router.put("/{appt_id}", response_model=AppointmentOut)
def update_appointment(appt_id: str,body: AppointmentUpdate, db: Session=Depends(get_db)):
    appt=db.query(AppointmentDB).filter(AppointmentDB.id==appt_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    #Verify start time is less than end time
    if body.start_time>=body.end_time:
        raise HTTPException(status_code=400, detail="Start time must be befoe end time")
    #Verify both patient and doctor exist
    patient=db.query(PatientDB).filter(PatientDB.id==body.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    doctor=db.query(DoctorDB).filter(DoctorDB.id==body.doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    #Verify appt time is within the doctors working hours
    if body.start_time<doctor.duty_start or body.end_time>doctor.duty_end:
        raise HTTPException(
            status_code=400, 
            detail=f"Appintment should be within doctor's working hours: ({doctor.duty_start}) - ({doctor.duty_end})"
        )
    #Check for overlapping appts
    overlapping=db.query(AppointmentDB).filter(
        AppointmentDB.doctor_id==body.doctor_id,
        AppointmentDB.appointment_date==body.appointment_date,
        AppointmentDB.start_time<body.end_time,
        AppointmentDB.end_time>body.end_time,
        AppointmentDB.id != appt_id #Excludes itself from overlapping 
    ).first()
    if overlapping:
        raise HTTPException(
            status_code=400,
            detail=f"The appointment overlaps with another appointment at ({overlapping.start_time}) - ({overlapping.end_time})"
        )
    #Apply updates
    for key,value in body.model_dump().items():
        setattr(appt,key,value)
    db.commit()
    db.refresh(appt)
    #Retrun output schema with names
    response=AppointmentOut.model_validate(appt)
    response.patient_name=patient.name
    response.doctor_name=doctor.name
    return response

@router.delete("/{appt_id}")
def delete_appointment(appt_id: str, db: Session=Depends(get_db)):
    appt=db.query(AppointmentDB).filter(AppointmentDB.id==appt_id).first()
    if not appt:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(appt)
    db.commit()
    return {"detail": "Appointment cancelled successfully"}

