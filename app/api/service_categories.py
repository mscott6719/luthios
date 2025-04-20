from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ServiceCategory
from app.schemas import ServiceCategoryCreate

router = APIRouter(prefix="/service-categories", tags=["Service Categories"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_categories(db: Session = Depends(get_db)):
    return db.query(ServiceCategory).all()

@router.post("/")
def create_category(category: ServiceCategoryCreate, db: Session = Depends(get_db)):
    new_category = ServiceCategory(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category
