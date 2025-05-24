
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(
    prefix="/appointments",
    tags=["appointments"]
)

@router.post("/")
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    new_appt = models.Appointment(**appointment.dict())
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)
    return new_appt

@router.get("/")
def get_appointments(db: Session = Depends(get_db)):
    return db.query(models.Appointment).all()
