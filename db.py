from sqlalchemy.orm import declarative_base #ORM for bridging python code and SQL db
from sqlalchemy.orm import sessionmaker #to manage transactions - COMMIT,ROLLBACK,BEGIN
#create_engine to connect python script to db
from sqlalchemy import create_engine, Column, String, Date, DateTime, INT, Enum, ForeignKey, Time
from datetime import datetime
from classes import Gender

DATABASE_URL="mysql+pymysql://root:@localhost/clinic_db"

engine=create_engine( #establishes primary conn between script and db
    DATABASE_URL,
    pool_recycle=3600, #creates db connection after 3600seconds to prevent errors during idle connections
    pool_pre_ping=True #sends a ping to check if connection is still alive
)

sessionLocal=sessionmaker(autoflush=False,bind=engine) #prevents sending pending changes to db
Base=declarative_base() #for tracking tables

class PatientDB(Base):
    __tablename__="patient"
    id=Column(String(36),primary_key=True)
    name=Column(String(50),nullable=False)
    date_of_birth=Column(Date,nullable=False)
    gender=Column(Enum(Gender),nullable=False)
    phone=Column(String(11),unique=True)
    email=Column(String(255),unique=True)
    address=Column(String(150),nullable=False)
    created_at=Column(DateTime,default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

class DoctorDB(Base):
    __tablename__="doctor"
    id=Column(String(36),primary_key=True)
    name=Column(String(40),nullable=False)
    specialization=Column(String(100), nullable=False)
    phone=Column(String(11),unique=True)
    email=Column(String(255),unique=True)
    experience=Column(INT, nullable=False)
    availability=Column(String(100),nullable=False)
    duty_start=Column(Time,nullable=False)
    duty_end=Column(Time,nullable=False)
    created_at=Column(DateTime, default=datetime.utcnow)
    updated_at=Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow)

class AppointmentDB(Base):
    __tablename__="appointment"
    id=Column(String(36),primary_key=True)
    patient_id=Column(String(36),ForeignKey("patient.id", ondelete="CASCADE"),nullable=False)
    doctor_id=Column(String(36),ForeignKey("doctor.id", ondelete="CASCADE"),nullable=False)
    appointment_date=Column(Date, nullable=False)
    start_time=Column(Time,nullable=False)
    end_time=Column(Time,nullable=False)
    created_at=Column(DateTime, default=datetime.utcnow)
    updated_at=Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


def get_db():
    db=sessionLocal() #opens fresh db connection before routes start
    try:
        yield db
    finally:
        db.close()


