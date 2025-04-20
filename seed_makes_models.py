from app.database import SessionLocal
from app.models import Make, Model

# Define makes and models
makes_and_models = [
    ("Fender", ["Stratocaster", "Telecaster", "Jazzmaster", "Jaguar"]),
    ("Gibson", ["Les Paul", "SG", "ES-335"]),
    ("Ibanez", ["RG", "S", "AZ"]),
    ("PRS", ["Custom 24", "Silver Sky", "McCarty"]),
    ("Martin", ["D-28", "OM-21", "000-15M"]),
    ("Taylor", ["814ce", "214ce", "GS Mini"]),
    ("Yamaha", ["Pacifica", "Revstar", "FG800"]),
    ("Gretsch", ["Electromatic", "Falcon", "Jet"]),
    ("Epiphone", ["Les Paul Standard", "Dot", "SG Special"]),
    ("Jackson", ["Soloist", "Dinky", "Rhoads"]),
]

db = SessionLocal()

for make_name, model_list in makes_and_models:
    make = Make(name=make_name)
    db.add(make)
    db.commit()  # So the ID gets generated
    db.refresh(make)

    for model_name in model_list:
        model = Model(name=model_name, make_id=make.id)
        db.add(model)

db.commit()
db.close()

print("✅ Makes and models seeded.")
