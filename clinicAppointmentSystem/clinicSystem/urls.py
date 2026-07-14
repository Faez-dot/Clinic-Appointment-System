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
    path('appointments/<uuid:pk>/delete/', views.appointment_delete, name='appointment_delete')
]
