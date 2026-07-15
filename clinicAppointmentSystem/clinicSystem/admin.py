from django.contrib import admin
from .models import Patient, Doctor, Appointment,Prescription,Billing, MedicalRecord, LaboratoryTest
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

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display=('patient','doctor','medicine_name','dosage','prescription_date')
    search_fields=('patient__name','doctor__name','medicine_name')
    list_filter=('prescription_date',)

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display=('patient','appointment','amount','payment_status','payment_date')
    search_fields=('patient__name','appointment__patient__name','payment_status')
    list_filter=('payment_status','payment_date')

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display=('patient','doctor','appointment','created_at')
    search_fields=('patient__name','doctor__name','diagnosis','symptoms')
    list_filter=('doctor','created_at')

@admin.register(LaboratoryTest)
class LaboratoryTestAdmin(admin.ModelAdmin):
    list_display=('patient','doctor','appointment','test_name','test_date','status')
    search_fields=('patient__name','doctor__name','test_name','status')
    list_filter=('status','test_date')