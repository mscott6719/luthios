from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import InspectionSession
from app.schemas import InspectionSessionCreate
import datetime

router = APIRouter(prefix="/inspections", tags=["Inspections"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_sessions(db: Session = Depends(get_db)):
    return db.query(InspectionSession).all()

@router.post("/")
def create_session(session: InspectionSessionCreate, db: Session = Depends(get_db)):
    new_session = InspectionSession(
        guitar_id=session.guitar_id,
        repair_order_id=session.repair_order_id,
        technician=session.technician,
        date=datetime.datetime.utcnow()
    )
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

