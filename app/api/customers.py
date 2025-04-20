from fastapi import APIRouter
from app.database import SessionLocal
from app.models import Customer

router = APIRouter(prefix="/customers", tags=["Customers"])

@router.get("/")
def get_customers():
    db = SessionLocal()
    customers = db.query(Customer).all()
    return [
        {
            "id": c.id,
            "first_name": c.first_name,
            "last_name": c.last_name,
            "email": c.email,
            "phone": c.phone,
            "marketing_opt_in": c.marketing_opt_in,
        }
        for c in customers
    ]
from fastapi import Depends
from app.schemas import CustomerCreate
from app.database import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    new_customer = Customer(
        first_name=customer.first_name,
        last_name=customer.last_name,
        email=customer.email,
        phone=customer.phone,
        marketing_opt_in=customer.marketing_opt_in
    )
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return {
        "id": new_customer.id,
        "first_name": new_customer.first_name,
        "last_name": new_customer.last_name
    }
