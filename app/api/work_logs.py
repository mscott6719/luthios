from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import WorkLog
from app.schemas import WorkLogCreate
import datetime

router = APIRouter(prefix="/work-logs", tags=["Work Logs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_work_logs(db: Session = Depends(get_db)):
    return db.query(WorkLog).all()

@router.post("/")
def create_work_log(log: WorkLogCreate, db: Session = Depends(get_db)):
    new_log = WorkLog(**log.dict())
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log
