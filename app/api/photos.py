from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import GuitarPhoto
from app.schemas import PhotoCreate

router = APIRouter(prefix="/photos", tags=["Photos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_photos(db: Session = Depends(get_db)):
    return db.query(GuitarPhoto).all()

@router.post("/")
def create_photo(photo: PhotoCreate, db: Session = Depends(get_db)):
    new_photo = GuitarPhoto(
        guitar_id=photo.guitar_id,
        repair_order_id=photo.repair_order_id,
        photo_url=photo.photo_url,
        caption=photo.caption
    )
    db.add(new_photo)
    db.commit()
    db.refresh(new_photo)
    return new_photo
