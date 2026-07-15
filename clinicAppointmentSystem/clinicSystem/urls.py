from django.urls import path 
from . import views

app_name='clinicSystem'

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/<uuid:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<uuid:pk>/delete/', views.patient_delete,name='patient_delete'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.doctor_create, name='doctor_create'),
    path('doctors/<uuid:pk>/edit/', views.doctor_update, name='doctor_update'),
    path('doctors/<uuid:pk>/delete/', views.doctor_delete, name='doctor_delete'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/add/', views.appointment_create, name='appointment_create'),
    path('appointments/<uuid:pk>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<uuid:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('prescriptions/add/', views.prescription_create, name='prescription_create'),
    path('prescriptions/<uuid:pk>/edit/', views.prescription_update, name='prescription_update'),
    path('prescriptions/<uuid:pk>/delete/', views.prescription_delete, name='prescription_delete'),
    path('billings/', views.billing_list, name='billing_list'),
    path('billings/add/', views.billing_create, name='billing_create'),
    path('billings/<uuid:pk>/edit/', views.billing_update, name='billing_update'),
    path('billings/<uuid:pk>/delete/', views.billing_delete, name='billing_delete'),
    path('medical-records/', views.medical_record_list, name='medical_record_list'),
    path('medical-records/add/',views.medical_record_create,name='medical_record_create'),
    path('medical-records/<uuid:pk>/edit/',views.medical_record_update,name='medical_record_update'),
    path('medical-records/<uuid:pk>/delete/',views.medical_record_delete,name='medical_record_delete'),
    path('laboratory-tests/',views.laboratory_test_list, name='laboratory_test_list'),
    path('laboratory-tests/add/',views.laboratory_test_create, name='laboratory_test_create'),
    path('laboratory-tests/<uuid:pk>/edit/',views.laboratory_test_update,name='laboratory_test_update'),
    path('laboratory-tests/<uuid:pk>/delete/',views.laboratory_test_delete,name='laboratory_test_delete'),   
]
