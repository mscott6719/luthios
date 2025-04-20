from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import RepairLineItem, ServiceCatalog
from app.schemas import RepairLineItemCreate

router = APIRouter(prefix="/line-items", tags=["Repair Line Items"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_line_items(db: Session = Depends(get_db)):
    return db.query(RepairLineItem).all()

@router.post("/")
def create_line_item(item: RepairLineItemCreate, db: Session = Depends(get_db)):
    # Fetch the default service info
    service = db.query(ServiceCatalog).get(item.service_id)

    new_item = RepairLineItem(
        repair_id=item.repair_id,
        service_id=item.service_id,
        name=item.name or service.name,
        description=item.description or service.description,
        custom_cost=item.custom_cost,
        is_completed=item.is_completed
    )

    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
