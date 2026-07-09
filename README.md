# Clinic Appointment System

A modern, fast, and responsive web application built with **FastAPI** and **MySQL** to manage patient records, doctors, and appointment scheduling.

## 🚀 Features

- **Patient Management**:
  - Full CRUD operations (Add, View, Edit, Delete).
  - Real-time frontend validations.
  - Backend validations using Pydantic (e.g. Pakistani phone format `03XXXXXXXXX`, past date-of-birth constraints).
- **Doctor Management**:
  - Full CRUD operations.
  - Track experience, specialization, contact details, and weekly availability.
- **Modern UI/UX**:
  - Tab-based navigation (Patients, Doctors, and planned Appointments).
  - Glassmorphic overlays with slide-in modals.
  - Animated toast alerts for success/error feedback.
  - Responsive layout tailored for desktop, tablet, and mobile views.
- **Database & Architecture**:
  - Relational MySQL storage using SQLAlchemy ORM.
  - Separate routers for clean API structuring.
  - Alembic integration for database migrations.

---

## 🛠 Tech Stack

- **Backend**: FastAPI, Python 3.x, SQLAlchemy (ORM), Pydantic v2 (Validation), Jinja2 (Templating)
- **Database**: MySQL (via PyMySQL connector)
- **Frontend**: Semantic HTML5, Custom Vanilla CSS, Vanilla JavaScript

---

## 📂 Project Structure

```text
Clinic_Appointment_System/
├── routes/                  # API routers (patient, doctor, etc.)
│   ├── patient_routes.py
│   └── doctor_routes.py
├── static/                  # Static assets (CSS styles)
│   └── style.css
├── templates/               # Jinja2 HTML templates
│   └── index.html
├── data/                    # JSON metadata/data stores
├── alembic/                 # Alembic DB migration configuration
├── classes.py               # Pydantic Schemas & Validators
├── db.py                    # Database connection & SQLAlchemy Models
├── main.py                  # App entry point
└── README.md                # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.8+ installed on your system.
- MySQL Server (e.g., via XAMPP, WampServer, or direct installation) running on `localhost`.

### 2. Database Setup
Create a new MySQL database named `clinic_db`. By default, the database URI is configured for a passwordless root user:
```sql
CREATE DATABASE clinic_db;
```
*(If your MySQL configuration has a password or a different port, update the `DATABASE_URL` in `db.py`)*.

### 3. Install Dependencies
Install all required Python packages:
```bash
pip install fastapi uvicorn sqlalchemy pymysql pydantic[email] jinja2
```

### 4. Run the Application
Start the development server using Uvicorn:
```bash
uvicorn main:app --reload
```

Open your browser and navigate to:
- **Web App**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive Swagger Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 API Endpoints

### Patients
- `GET /api/patients/` - Fetch all patient records.
- `GET /api/patients/{id}` - Fetch single patient.
- `POST /api/patients/` - Create a new patient record.
- `PUT /api/patients/{id}` - Update a patient record.
- `DELETE /api/patients/{id}` - Delete patient record.

### Doctors
- `GET /api/doctors/` - Fetch all doctor records.
- `GET /api/doctors/{id}` - Fetch single doctor.
- `POST /api/doctors/` - Create a new doctor record.
- `PUT /api/doctors/{id}` - Update a doctor record.
- `DELETE /api/doctors/{id}` - Delete doctor record.
