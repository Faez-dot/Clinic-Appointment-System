from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from jinja2 import FileSystemLoader
from db import engine,Base

Base.metadata.create_all(bind=engine) #checks db server through engine and creates missing tables if any

from routes.patient_routes import router as patientRouter
from routes.doctor_routes import router as doctorRouter
from routes.appointment_routes import router as appointmentRouter

app = FastAPI(
    title="Clinic Appointment System",
    version="1.0.0"
)

# Register API Routers
app.include_router(patientRouter)
app.include_router(doctorRouter)
app.include_router(appointmentRouter)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
templates.env.loader = FileSystemLoader("templates", encoding="utf-8")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
