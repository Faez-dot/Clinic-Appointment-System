# Clinic Appointment System

A Django-based web application for managing patients, doctors, appointments, prescriptions, and billing using MySQL.

## 🚀 Features

- **Patient Management**
  - Add, edit, view, and delete patients.
  - Store name, date of birth, gender, phone, email, and address.
- **Doctor Management**
  - Add, edit, view, and delete doctors.
  - Track specialization, contact, experience, availability, and duty times.
- **Appointment Scheduling**
  - Create, edit, view, and delete appointments.
  - Link appointments to patients and doctors.
- **Prescription Management**
  - Create and manage prescriptions for patients from doctors.
  - Store medicine name, dosage, instructions, and prescription date.
- **Billing Management**
  - Create and manage billing records.
  - Link billing to patients and optional appointments.
  - Track amount, payment status, and payment date.
- **Admin Interface**
  - Manage patients, doctors, appointments, prescriptions, and billings via Django admin.
- **Static assets**
  - CSS served from Django static files.

---

## 🛠 Tech Stack

- **Backend**: Django
- **Database**: MySQL
- **Frontend**: HTML, CSS, Django templates

---

## 📂 Project Structure

```text
clinicAppointmentSystem/
├── clinicAppointmentSystem/    # Django project settings and URLs
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── clinicSystem/              # Django app for clinic management
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   ├── patients/
│   │   ├── doctors/
│   │   ├── appointments/
│   │   ├── prescriptions/
│   │   └── billings/
│   └── static/
├── manage.py
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.11+ installed.
- MySQL Server running on `localhost`.

### 2. Database Setup
Create a new MySQL database named `clinic_db`:
```sql
CREATE DATABASE clinic_db;
```
If your MySQL user or password differs, update the `DATABASES` settings in `clinicAppointmentSystem/settings.py`.

### 3. Install Dependencies
Use your Python environment and install Django and MySQL client packages.

If you are using pip:
```bash
pip install django mysqlclient
```

### 4. Run Migrations
Generate and apply migrations for the clinic app:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
Create a Django admin user to manage data:
```bash
python manage.py createsuperuser
```

### 6. Run the Application
Start the local Django server:
```bash
python manage.py runserver
```

Open the application in your browser at:
- [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Admin panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## ✅ Usage Notes

- Use the home page tabs to navigate to Patients, Doctors, Appointments, Prescriptions, and Billings.
- The Django admin lets you manage all models from one interface.
- Static CSS files are served through Django's static files system.

---

## 📌 Important Files

- `clinicSystem/models.py` — model definitions for patients, doctors, appointments, prescriptions, and billings.
- `clinicSystem/admin.py` — admin registration for all models.
- `clinicSystem/urls.py` — app URL routes.
- `clinicSystem/views.py` — view logic for CRUD operations.
- `clinicAppointmentSystem/settings.py` — database and static file configuration.

---

## 🧪 Troubleshooting

- If static files do not load, verify `STATICFILES_DIRS` in `clinicAppointmentSystem/settings.py` and ensure `style.css` is in the configured folder.
- If migrations appear applied but tables are missing, check the database schema and `django_migrations` table for consistency.
- If delete URLs return 404, confirm the URL patterns use trailing slashes consistently with your templates.
