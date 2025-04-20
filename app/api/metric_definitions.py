from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import MetricDefinition
from app.schemas import MetricDefinitionCreate

router = APIRouter(prefix="/metrics/definitions", tags=["Metric Definitions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_metric_definitions(db: Session = Depends(get_db)):
    return db.query(MetricDefinition).all()

@router.post("/")
def create_metric_definition(defn: MetricDefinitionCreate, db: Session = Depends(get_db)):
    new_defn = MetricDefinition(**defn.dict())
    db.add(new_defn)
    db.commit()
    db.refresh(new_defn)
    return new_defn
