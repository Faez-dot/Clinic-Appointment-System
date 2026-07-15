from django import forms
from .models import Patient, Doctor, Appointment,Prescription,Billing,MedicalRecord, LaboratoryTest

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['name', 'date_of_birth','gender', 'phone', 'email', 'address']

class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields=['name', 'specialization', 'phone', 'email', 'experience', 'availability','duty_start', 'duty_end']



class AppointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields=['patient', 'doctor', 'appointment_date','start_time','end_time']

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model=Prescription
        fields=['patient', 'doctor', 'medicine_name', 'dosage', 'instructions', 'prescription_date']

class BillingForm(forms.ModelForm):
    class Meta:
        model=Billing
        fields=['patient', 'appointment', 'amount', 'payment_status', 'payment_date']

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model=MedicalRecord
        fields=['patient','doctor','appointment','diagnosis','symptoms','treatment','notes']

class LaboratoryTestForm(forms.ModelForm):
    class Meta:
        model=LaboratoryTest
        fields=['patient','doctor','appointment','test_name','test_date','result','status']

