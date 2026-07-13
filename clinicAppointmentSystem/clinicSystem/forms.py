from django import forms
from .models import Patient, Doctor, Appointment

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

