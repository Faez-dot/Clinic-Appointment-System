from django.db import models
import uuid
# Create your models here.
class Gender(models.TextChoices):
    MALE='Male'
    FEMALE='Female'

class Patient(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=10, choices= Gender.choices)
    phone=models.CharField(max_length=11, unique=True)
    email=models.EmailField(unique=True)
    address=models.CharField(max_length=150)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Meta: #to handle table names
    db_table='patient'

def __str__(self):
    return self.name

class Doctor(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=40)
    specialization=models.CharField(max_length=50)
    phone=models.CharField(max_length=11, unique=True)
    email=models.EmailField(unique=True)
    experience=models.PositiveIntegerField()
    availability=models.CharField(max_length=100)
    duty_start=models.TimeField()
    duty_end=models.TimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Meta:
    db_table='doctor'

def __str__(self):
    return self.name

class Appointment(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    appointment_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Meta:
    db_table='appointment'

def __str__(self):
    return f"{self.patient.name} -> {self.doctor.name}"

