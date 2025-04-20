from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Make
from app.schemas import MakeCreate

router = APIRouter(prefix="/makes", tags=["Makes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_makes(db: Session = Depends(get_db)):
    return db.query(Make).all()

@router.post("/")
def create_make(make: MakeCreate, db: Session = Depends(get_db)):
    new_make = Make(name=make.name)
    db.add(new_make)
    db.commit()
    db.refresh(new_make)
    return new_make
