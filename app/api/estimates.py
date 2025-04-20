from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Estimate
from app.schemas import EstimateCreate

router = APIRouter(prefix="/estimates", tags=["Estimates"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_estimates(db: Session = Depends(get_db)):
    return db.query(Estimate).all()

@router.post("/")
def create_estimate(estimate: EstimateCreate, db: Session = Depends(get_db)):
    new_estimate = Estimate(**estimate.dict())
    db.add(new_estimate)
    db.commit()
    db.refresh(new_estimate)
    return new_estimate
