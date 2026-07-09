import re
import uuid
from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, field_validator, Field, EmailStr
from datetime import date, datetime, time

class Gender(str, Enum): #enum so no other option is selected
    Male="Male"
    Female="Female"

PhoneNumber=re.compile(r"^03\d{9}$")

def _validate_Phone_Number(phone: str)->str:
    phone=phone.strip() #removes spaces
    if not PhoneNumber.match(phone):
        raise ValueError("Phone number must be in correct format beiginning with 03 and total of 11 digits")
    return phone


class PatientBase(BaseModel):
    name:str =Field(..., min_length=2, max_length=50, description="Patient Full Name")
    date_of_birth: date=Field(..., description="Patient's date of birth")
    gender:Gender
    phone:str=Field(..., description="Pakistani Phone number")
    email: EmailStr
    address: str=Field(..., min_length=5, max_length=150)

    @field_validator("phone")
    @classmethod
    def validate_phone(cls,phone:str)->str:
        return _validate_Phone_Number(phone)
    
    @field_validator("date_of_birth")
    @classmethod
    def validate_dob(cls,dob: str)->date:
        if dob>=date.today():
            raise ValueError("DOB is wrong.")
        return dob
    
#Inherits all fields from PatientBase after validating
class PatientCreate(PatientBase):
    id:str=Field(default_factory=lambda: str(uuid.uuid4()), description="Auto generated UUID")

class PatientUpdate(PatientBase):
    pass

class PatientOut(PatientBase): #to be send to client-contains all info
    id: str=Field(..., description="UUID Identifier")
    created_at: datetime
    updated_at: datetime
    model_config={
        "from_attributes":True, #allows pydantic to read and process db objects directly from sqlalchemy
        "json_encoders":{date: lambda v: v.isoformat(), datetime: lambda v: v.isoformat()}#configures date so it can be sent directly to json
    }

class DoctorBase(BaseModel):
    name: str=Field(..., min_length=2, max_length=40, description="Doctor's full name")
    specialization: str=Field(..., min_length=5, max_length=100)
    phone: str=Field(..., description="Pakistani Phone number")
    email: EmailStr
    experience: int=Field(..., ge=0,le=60, description="Years of experience")
    availability: str=Field(..., min_length=4, max_length=100, description="Mon-Fri 9AM-5PM")
    duty_start:time=Field(..., description="Doctor's shift start time")
    duty_end:time=Field(..., description="Doctor's shift end time")

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, phone:str)->str:
        return _validate_Phone_Number(phone)
    
    
class DoctorCreate(DoctorBase):
    id: str=Field(default_factory=lambda:str(uuid.uuid4()), description="Auto-generated UUID")

class DoctorUpdate(DoctorBase):
    pass

class DoctorOut(DoctorBase):
    id: str=Field(...,description="UUID Identifier")
    created_at:datetime
    updated_at:datetime
    model_config={
        "from_attributes":True,
        "json_encoders":{
            datetime: lambda v:v.isoformat(),
            date: lambda v:v.isoformat(),
            time: lambda v:v.isoformat()
        }
    }

class AppointmentBase(BaseModel):
    patient_id:str=Field(..., description="UUID of patient")
    doctor_id:str=Field(..., description="UUID of doctor")
    appointment_date:date=Field(...,description="Date of appointment")
    start_time:time=Field(...,description="Start time")
    end_time:time=Field(...,description="End time")

    @field_validator("appointment_date")
    @classmethod
    def validate_date(cls, v: date)->date:
        if v<date.today():
            raise ValueError("Appointment date cannot be in the past")
        return v
    
class AppointmentCreate(AppointmentBase):
    id:str=Field(default_factory=lambda: str(uuid.uuid4()), description="Auto-generated UUID")

class AppointmentOut(AppointmentBase):
    id:str
    patient_name: Optional[str]=None
    doctor_name: Optional[str]=None
    created_at: datetime
    updated_at:datetime

    model_config={
        "from_attributes":True,
        "json_encoders":{
            datetime:lambda v:v.isoformat(),
            date:lambda v:v.isoformat(),
            time:lambda v:v.isoformat()
        }
    }

class AppointmentUpdate(AppointmentBase):
    pass