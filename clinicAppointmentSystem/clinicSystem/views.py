from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Patient,Doctor, Appointment, Prescription, Billing, MedicalRecord, LaboratoryTest
from .forms import PatientForm, DoctorForm, AppointmentForm, PrescriptionForm, BillingForm, MedicalRecordForm,LaboratoryTestForm
# Create your views here.
#def hello_world(request):
#    return HttpResponse("Hello, World!")


def home(request):
    return render(request, 'home.html')

def patient_list(request):
    patients=Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})

def patient_create(request):
    if request.method=='POST': # checks user clicked the submit btn
        form=PatientForm(request.POST)# takes the data user typed in (request.POST) and stuffs it into patient.form
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:patient_list') #redirect to patient list to see if patient added
    else: #if not POST, the will be GET request
        form=PatientForm() # Blank form if they just opened the page or error msgs if wrong input in fields
    return render(request, 'patients/form.html', {'form': form, 'title': 'Add Patient'})

def patient_update(request, pk):
    patient=get_object_or_404(Patient, pk=pk)#gets user if exisst if not error 404
    if request.method=='POST':
        form=PatientForm(request.POST, instance=patient)#instance tells django that we are updating an existing patient not creating new one
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:patient_list')
    else:#Triggers when user clciks edit and opens form for first time
        form=PatientForm(instance=patient)#creates a form wit that patients info so they see what they are editing
    return render(request, 'patients/form.html', {'form': form, 'title': 'Edit patient'})
    
def patient_delete(request, pk):
    patient=get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('clinicSystem:patient_list')

def doctor_list(request):
    doctors=Doctor.objects.all()
    return render(request, 'doctors/list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method=='POST':
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:doctor_list')
    else:
        form=DoctorForm()
    return render(request, 'doctors/form.html', {'form': form, 'title': 'Add Doctor'})

def doctor_update(request, pk):
    doctor=get_object_or_404(Doctor, pk=pk)
    if request.method=='POST':
        form=DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:doctor_list')
    else:
        form=DoctorForm(instance=doctor)
    return render(request, 'doctors/form.html',{'form':form, 'title': 'Edit doctor'})

def doctor_delete(request,pk):
    doctor=get_object_or_404(Doctor,pk=pk)
    doctor.delete()
    return redirect('clinicSystem:doctor_list')

def appointment_list(request):
    appointments=Appointment.objects.select_related('patient', 'doctor').all()
    return render(request, 'appointments/list.html', {'appointments': appointments})

def appointment_create(request):
    if request.method=='POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:appointment_list')
    else:
        form=AppointmentForm()
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Add Appointment'})

def appointment_update(request, pk):
    appointment=get_object_or_404(Appointment, pk=pk)
    if request.method=='POST':
        form=AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:appointment_list')
    else:
        form=AppointmentForm(instance=appointment)
    return render(request, 'appointments/form.html', {'form': form, 'title': 'Edit Appointment'})

def appointment_delete(request, pk):
    appointment=get_object_or_404(Appointment, pk=pk)
    appointment.delete()
    return redirect('clinicSystem:appointment_list')

def prescription_list(request):
    prescriptions=Prescription.objects.select_related('patient', 'doctor').all()
    return render(request, 'prescriptions/list.html', {'prescriptions': prescriptions})

def prescription_create(request):
    if request.method=='POST':
        form=PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:prescription_list')
    else:
        form=PrescriptionForm()
    return render(request, 'prescriptions/form.html', {'form': form, 'title': 'Add Prescription'})

def prescription_update(request, pk):
    prescription=get_object_or_404(Prescription, pk=pk)
    if request.method=='POST':
        form=PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:prescription_list')
    else:
        form=PrescriptionForm(instance=prescription)
    return render(request, 'prescriptions/form.html', {'form': form, 'title': 'Edit Prescription'})

def prescription_delete(request, pk):
    prescription=get_object_or_404(Prescription, pk=pk)
    prescription.delete()
    return redirect('clinicSystem:prescription_list')

def billing_list(request):
    billings=Billing.objects.select_related('patient','appointment').all()
    return render(request, 'billings/list.html', {'billings': billings})

def billing_create(request):
    if request.method=='POST':
        form=BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:billing_list')
    else:
        form=BillingForm()
    return render(request, 'billings/form.html', {'form': form,'title':'Add Billing'})

def billing_update(request, pk):
    billing=get_object_or_404(Billing, pk=pk)
    if request.method=='POST':
        form=BillingForm(request.POST, instance=billing)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:billing_list')
    else:
        form=BillingForm(instance=billing)
    return render(request, 'billings/form.html', {'form':form, 'title':'Edit Billing'})

def billing_delete(request,pk):
    billing=get_object_or_404(Billing, pk=pk)
    billing.delete()
    return redirect('clinicSystem:billing_list')



def medical_record_list(request):
    records=MedicalRecord.objects.select_related('patient','doctor','appointment').all()
    return render(request, 'medical_records/list.html', {'records': records})

def medical_record_create(request):
    if request.method=='POST':
        form=MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:medical_record_list')
    else:
        form=MedicalRecordForm()
    return render(request, 'medical_records/form.html', {'form': form, 'title': 'Add Medical Record'})

def medical_record_update(request, pk):
    record=get_object_or_404(MedicalRecord, pk=pk)
    if request.method=='POST':
        form=MedicalRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:medical_record_list')
    else:
        form=MedicalRecordForm(instance=record)
    return render(request, 'medical_records/form.html', {'form': form, 'title': 'Edit Medical Record'})

def medical_record_delete(request, pk):
    record=get_object_or_404(MedicalRecord, pk=pk)
    record.delete()
    return redirect('clinicSystem:medical_record_list')

def laboratory_test_list(request):
    tests=LaboratoryTest.objects.select_related('patient','doctor','appointment').all()
    return render(request, 'laboratory_tests/list.html', {'tests': tests})

def laboratory_test_create(request):
    if request.method=='POST':
        form=LaboratoryTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:laboratory_test_list')
    else:
        form=LaboratoryTestForm()
    return render(request, 'laboratory_tests/form.html', {'form': form, 'title': 'Add Laboratory Test'})

def laboratory_test_update(request, pk):
    test=get_object_or_404(LaboratoryTest, pk=pk)
    if request.method=='POST':
        form=LaboratoryTestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('clinicSystem:laboratory_test_list')
    else:
        form=LaboratoryTestForm(instance=test)
    return render(request, 'laboratory_tests/form.html', {'form': form,'title': 'Edit Laboratory Test'})

def laboratory_test_delete(request, pk):
    test=get_object_or_404(LaboratoryTest, pk=pk)
    test.delete()
    return redirect('clinicSystem:laboratory_test_list')

