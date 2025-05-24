from app.database import SessionLocal
from app.models import Make, Model

db = SessionLocal()

makes = [
    "Fender",
    "Gibson",
    "Martin",
    "Taylor",
    "PRS",
]

models = [
    {"name": "Stratocaster", "make_name": "Fender", "guitar_type": "Electric"},
    {"name": "Telecaster", "make_name": "Fender", "guitar_type": "Electric"},
    {"name": "Les Paul", "make_name": "Gibson", "guitar_type": "Electric"},
    {"name": "SG", "make_name": "Gibson", "guitar_type": "Electric"},
    {"name": "D-28", "make_name": "Martin", "guitar_type": "Acoustic"},
    {"name": "000-15M", "make_name": "Martin", "guitar_type": "Acoustic"},
    {"name": "214ce", "make_name": "Taylor", "guitar_type": "Acoustic"},
    {"name": "814ce", "make_name": "Taylor", "guitar_type": "Acoustic"},
    {"name": "Custom 24", "make_name": "PRS", "guitar_type": "Electric"},
]

for make_name in makes:
    make = db.query(Make).filter_by(name=make_name).first()
    if not make:
        make = Make(name=make_name)
        db.add(make)
        db.commit()
        db.refresh(make)

for model in models:
    make = db.query(Make).filter_by(name=model["make_name"]).first()
    if make:
        existing_model = db.query(Model).filter_by(name=model["name"], make_id=make.id).first()
        if not existing_model:
            new_model = Model(
                name=model["name"],
                make_id=make.id,
                guitar_type=model["guitar_type"]
            )
            db.add(new_model)
            db.commit()

print("✅ Makes and Models seeded successfully.")
