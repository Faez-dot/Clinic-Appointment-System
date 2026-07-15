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
        db_table='clinicsystem_patient'

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
        db_table='clinicsystem_doctor'

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
        db_table='clinicsystem_appointment'

    def __str__(self):
        return f"{self.patient.name} -> {self.doctor.name}"

class Prescription(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient=models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='prescriptions')
    doctor=models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='prescriptions')
    medicine_name=models.CharField(max_length=200)
    dosage=models.CharField(max_length=100)
    instructions=models.TextField()
    prescription_date=models.DateField()

    class Meta:
        db_table='clinicsystem_prescriptions'

    def __str__(self):
        return f"{self.patient.name} - {self.medicine_name}"
    
class Billing(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient=models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='billings')
    appointment=models.ForeignKey('Appointment', on_delete=models.SET_NULL, null=True, blank=True, related_name='billings')
    amount=models.DecimalField(max_digits=8, decimal_places=2)
    payment_status=models.CharField(max_length=50, default='Pending')
    payment_date=models.DateField(null=True, blank=True)

    class Meta:
        db_table='clinicsystem_billing'

    def __str__(self):
        return f"{self.patient.name} - {self.amount}"
    

class MedicalRecord(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient=models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='medical_records')
    doctor=models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='medical_records')
    appointment=models.OneToOneField('Appointment', on_delete=models.CASCADE, related_name='medical_records')
    diagnosis=models.TextField()
    symptoms=models.TextField()
    treatment=models.TextField()
    notes=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table='clinicsystem_medical_record'

    def __str__(self):
        return f"{self.patient.name} - {self.appointment.appointment_date}"
    
class LaboratoryTest(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient=models.ForeignKey('Patient', on_delete=models.CASCADE, related_name='lab_tests')
    doctor=models.ForeignKey('Doctor', on_delete=models.CASCADE, related_name='lab_tests')
    appointment=models.ForeignKey('Appointment', on_delete=models.CASCADE, related_name='lab_tests')
    test_name=models.CharField(max_length=30)
    test_date=models.DateField()
    result=models.TextField()
    status=models.CharField(max_length=20,choices=[('Pending','Pending'),('Completed','Completed')],default='Pending')

    class Meta:
        db_table='clinicsystem_lab_test'

    def __str__(self):
        return f"{self.patient.name} - {self.test_name}"
