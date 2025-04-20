from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import ServiceCatalog
from app.schemas import ServiceCatalogCreate

router = APIRouter(prefix="/services", tags=["Service Catalog"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_services(db: Session = Depends(get_db)):
    return db.query(ServiceCatalog).all()

@router.post("/")
def create_service(service: ServiceCatalogCreate, db: Session = Depends(get_db)):
    new_service = ServiceCatalog(**service.dict())
    db.add(new_service)
    db.commit()
    db.refresh(new_service)
    return new_service
