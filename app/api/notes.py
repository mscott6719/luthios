from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Note
from app.schemas import NoteCreate
import datetime

router = APIRouter(prefix="/notes", tags=["Notes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_notes(db: Session = Depends(get_db)):
    return db.query(Note).all()

@router.post("/")
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    new_note = Note(**note.dict(), date_added=datetime.datetime.utcnow())
    db.add(new_note)
    db.commit()
    db.refresh(new_note)
    return new_note
