from app.database import SessionLocal
from app.models import ServiceCategory

db = SessionLocal()

# Category: Setup
if not db.query(ServiceCategory).filter_by(name="Setup").first():
    db.add(ServiceCategory(name="Setup", description="Includes full setup work such as truss rod adjustments, action height, nut slot tuning, and intonation for optimal playability."))
    db.commit()

# Category: Fretwork
if not db.query(ServiceCategory).filter_by(name="Fretwork").first():
    db.add(ServiceCategory(name="Fretwork", description="Covers fret leveling, crowning, polishing, and complete or partial refrets on various board types."))
    db.commit()

# Category: Electronics
if not db.query(ServiceCategory).filter_by(name="Electronics").first():
    db.add(ServiceCategory(name="Electronics", description="Involves diagnosis and repair of wiring, potentiometers, switches, jacks, grounding, and pickup-related work."))
    db.commit()

# Category: Structural
if not db.query(ServiceCategory).filter_by(name="Structural").first():
    db.add(ServiceCategory(name="Structural", description="Addresses neck angle corrections, crack repairs, brace work, or other integrity-related services."))
    db.commit()

# Category: Cleaning
if not db.query(ServiceCategory).filter_by(name="Cleaning").first():
    db.add(ServiceCategory(name="Cleaning", description="Deep cleaning and cosmetic detailing of guitars, including fretboard conditioning and hardware polishing."))
    db.commit()

# Category: Pickup Install
if not db.query(ServiceCategory).filter_by(name="Pickup Install").first():
    db.add(ServiceCategory(name="Pickup Install", description="Installation or replacement of one or more pickups, including active and passive systems."))
    db.commit()

# Category: Nut & Saddle
if not db.query(ServiceCategory).filter_by(name="Nut & Saddle").first():
    db.add(ServiceCategory(name="Nut & Saddle", description="Custom or pre-slotted nut and saddle shaping, replacement, and fitting for optimal tone and string height."))
    db.commit()

# Category: Bridge / Tremolo
if not db.query(ServiceCategory).filter_by(name="Bridge / Tremolo").first():
    db.add(ServiceCategory(name="Bridge / Tremolo", description="Repairs or adjustments to tremolo systems, bridges, or bridge saddles — includes Floyd Rose, Tune-O-Matic, etc."))
    db.commit()

# Category: Custom
if not db.query(ServiceCategory).filter_by(name="Custom").first():
    db.add(ServiceCategory(name="Custom", description="Unique or unusual modifications and one-off work not covered by other categories."))
    db.commit()

# Category: Other
if not db.query(ServiceCategory).filter_by(name="Other").first():
    db.add(ServiceCategory(name="Other", description="Catch-all category for uncategorized or miscellaneous services."))
    db.commit()

# Category: Customer Service
if not db.query(ServiceCategory).filter_by(name="Customer Service").first():
    db.add(ServiceCategory(name="Customer Service", description="Non-technical tasks such as customer feedback logging, intake confirmations, or post-service follow-up."))
    db.commit()

# Category: Restringing
if not db.query(ServiceCategory).filter_by(name="Restringing").first():
    db.add(ServiceCategory(name="Restringing", description="Simple string changes for all guitar types, including electric, acoustic, 12-string, nylon, and floating bridge setups."))
    db.commit()

# Category: Acoustic
if not db.query(ServiceCategory).filter_by(name="Acoustic").first():
    db.add(ServiceCategory(name="Acoustic", description="Services specific to acoustic instruments such as saddle shaping, bridge repairs, and top-related evaluations."))
    db.commit()

db.close()
print('✅ Service categories seeded.')