from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import RepairIntake
from app.schemas import RepairIntakeCreate
import datetime

router = APIRouter(prefix="/intakes", tags=["Repair Intakes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_intakes(db: Session = Depends(get_db)):
    return db.query(RepairIntake).all()

@router.post("/")
def create_intake(intake: RepairIntakeCreate, db: Session = Depends(get_db)):
    new_intake = RepairIntake(
        repair_order_id=intake.repair_order_id,
        string_gauge=intake.string_gauge,
        tuning=intake.tuning,
        case_provided=intake.case_provided,
        strings_provided=intake.strings_provided,
        terms_accepted=intake.terms_accepted,
        form_signed=intake.form_signed,
        created_at=datetime.datetime.utcnow()
    )
    db.add(new_intake)
    db.commit()
    db.refresh(new_intake)
    return new_intake
