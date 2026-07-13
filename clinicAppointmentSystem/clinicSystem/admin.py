from django.contrib import admin
from .models import Patient, Doctor, Appointment
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','date_of_birth')
    search_fields=('name','phone','email')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display=('name', 'specialization', 'phone', 'experience')
    search_fields=('name','specialization', 'phone')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display=('patient','doctor','appointment_date','start_time','end_time')
    search_fields=('patient__name','doctor__name')

