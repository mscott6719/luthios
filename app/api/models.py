from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Model
from app.schemas import ModelCreate

router = APIRouter(prefix="/models", tags=["Models"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_models(make_id: int = Query(None), db: Session = Depends(get_db)):
    query = db.query(Model)
    if make_id:
        query = query.filter(Model.make_id == make_id)
    return query.all()

@router.post("/")
def create_model(model: ModelCreate, db: Session = Depends(get_db)):
    new_model = Model(name=model.name, make_id=model.make_id)
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model
