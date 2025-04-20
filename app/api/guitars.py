from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Guitar
from app.schemas import GuitarCreate

router = APIRouter(prefix="/guitars", tags=["Guitars"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_guitars(db: Session = Depends(get_db)):
    guitars = db.query(Guitar).all()
    return [
        {
            "id": g.id,
            "customer_id": g.customer_id,
            "make_id": g.make_id,
            "model_id": g.model_id,
            "serial_number": g.serial_number,
            "type": g.type,
            "year": g.year,
            "color": g.color,
            "pickup_config": g.pickup_config,
            "estimated_value": g.estimated_value,
            "string_count": g.string_count
        }
        for g in guitars
    ]

@router.post("/")
def create_guitar(guitar: GuitarCreate, db: Session = Depends(get_db)):
    new_guitar = Guitar(**guitar.dict())
    db.add(new_guitar)
    db.commit()
    db.refresh(new_guitar)
    return {"id": new_guitar.id}
