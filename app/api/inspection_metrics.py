from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import InspectionMetric
from app.schemas import InspectionMetricCreate

router = APIRouter(prefix="/metrics", tags=["Inspection Metrics"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_metrics(db: Session = Depends(get_db)):
    return db.query(InspectionMetric).all()

@router.post("/")
def create_metric(metric: InspectionMetricCreate, db: Session = Depends(get_db)):
    new_metric = InspectionMetric(**metric.dict())
    db.add(new_metric)
    db.commit()
    db.refresh(new_metric)
    return new_metric
