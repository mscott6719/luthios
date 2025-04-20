from app.database import SessionLocal
from app.models import ServiceCatalog, ServiceCategory

db = SessionLocal()

# Cache category name → ID
category_lookup = {}

# Create category: Electronics
cat = db.query(ServiceCategory).filter_by(name='Electronics').first()
if not cat:
    cat = ServiceCategory(name='Electronics', description='Electronics services')
    db.add(cat)
    db.commit()
    db.refresh(cat)
category_lookup['Electronics'] = cat.id

# Create category: Electronics Cavity Shielding
cat = db.query(ServiceCategory).filter_by(name='Electronics Cavity Shielding').first()
if not cat:
    cat = ServiceCategory(name='Electronics Cavity Shielding', description='Electronics Cavity Shielding services')
    db.add(cat)
    db.commit()
    db.refresh(cat)
category_lookup['Electronics Cavity Shielding'] = cat.id

# Create category: Fretwork
cat = db.query(ServiceCategory).filter_by(name='Fretwork').first()
if not cat:
    cat = ServiceCategory(name='Fretwork', description='Fretwork services')
    db.add(cat)
    db.commit()
    db.refresh(cat)
category_lookup['Fretwork'] = cat.id

# Create category: Nut & Saddle
cat = db.query(ServiceCategory).filter_by(name='Nut & Saddle').first()
if not cat:
    cat = ServiceCategory(name='Nut & Saddle', description='Nut & Saddle services')
    db.add(cat)
    db.commit()
    db.refresh(cat)
category_lookup['Nut & Saddle'] = cat.id

# Create category: Restringing
cat = db.query(ServiceCategory).filter_by(name='Restringing').first()
if not cat:
    cat = ServiceCategory(name='Restringing', description='Restringing services')
    db.add(cat)
    db.commit()
    db.refresh(cat)
category_lookup['Restringing'] = cat.id

# Create category: Setup
cat = db.query(ServiceCategory).filter_by(name='Setup').first()
if not cat:
    cat = ServiceCategory(name='Setup', description='Setup services')
    db.add(cat)
    db.commit()
    db.refresh(cat)
category_lookup['Setup'] = cat.id

# Service: Restring - Electric Guitar (Hard-Tail Bridge)
if not db.query(ServiceCatalog).filter_by(name="Restring - Electric Guitar (Hard-Tail Bridge)").first():
    db.add(ServiceCatalog(name="Restring - Electric Guitar (Hard-Tail Bridge)", description="Standard electric restring", default_cost=25, category_id=category_lookup['Restringing']))
    db.commit()

# Service: Restring - Electric (Non-Floyd Rose Tremolo)
if not db.query(ServiceCatalog).filter_by(name="Restring - Electric (Non-Floyd Rose Tremolo)").first():
    db.add(ServiceCatalog(name="Restring - Electric (Non-Floyd Rose Tremolo)", description="Electric restring with tremolo bridge", default_cost=30, category_id=category_lookup['Restringing']))
    db.commit()

# Service: Restring - Electric (Floyd Rose/Locking Nut)
if not db.query(ServiceCatalog).filter_by(name="Restring - Electric (Floyd Rose/Locking Nut)").first():
    db.add(ServiceCatalog(name="Restring - Electric (Floyd Rose/Locking Nut)", description="Advanced restring with locking nut", default_cost=40, category_id=category_lookup['Restringing']))
    db.commit()

# Service: Restring - 6-String Acoustic
if not db.query(ServiceCatalog).filter_by(name="Restring - 6-String Acoustic").first():
    db.add(ServiceCatalog(name="Restring - 6-String Acoustic", description="Standard acoustic restring", default_cost=25, category_id=category_lookup['Restringing']))
    db.commit()

# Service: Restring - 12-String Acoustic
if not db.query(ServiceCatalog).filter_by(name="Restring - 12-String Acoustic").first():
    db.add(ServiceCatalog(name="Restring - 12-String Acoustic", description="Double string acoustic restring", default_cost=35, category_id=category_lookup['Restringing']))
    db.commit()

# Service: Restring - Nylon String Classical
if not db.query(ServiceCatalog).filter_by(name="Restring - Nylon String Classical").first():
    db.add(ServiceCatalog(name="Restring - Nylon String Classical", description="Classical guitar restringing", default_cost=30, category_id=category_lookup['Restringing']))
    db.commit()

# Service: Set-up - Electric Guitar (Hard-Tail Bridge)
if not db.query(ServiceCatalog).filter_by(name="Set-up - Electric Guitar (Hard-Tail Bridge)").first():
    db.add(ServiceCatalog(name="Set-up - Electric Guitar (Hard-Tail Bridge)", description="Complete setup for fixed-bridge electric", default_cost=65, category_id=category_lookup['Setup']))
    db.commit()

# Service: Set-up - Electric (Non-Floyd Rose Tremolo)
if not db.query(ServiceCatalog).filter_by(name="Set-up - Electric (Non-Floyd Rose Tremolo)").first():
    db.add(ServiceCatalog(name="Set-up - Electric (Non-Floyd Rose Tremolo)", description="Setup for tremolo-equipped electric", default_cost=75, category_id=category_lookup['Setup']))
    db.commit()

# Service: Set-up - Electric (Floyd Rose/Locking Nut)
if not db.query(ServiceCatalog).filter_by(name="Set-up - Electric (Floyd Rose/Locking Nut)").first():
    db.add(ServiceCatalog(name="Set-up - Electric (Floyd Rose/Locking Nut)", description="Advanced setup for locking nut", default_cost=90, category_id=category_lookup['Setup']))
    db.commit()

# Service: Set-up - 6-String Acoustic
if not db.query(ServiceCatalog).filter_by(name="Set-up - 6-String Acoustic").first():
    db.add(ServiceCatalog(name="Set-up - 6-String Acoustic", description="Complete acoustic setup", default_cost=65, category_id=category_lookup['Setup']))
    db.commit()

# Service: Set-up - 12-String Acoustic
if not db.query(ServiceCatalog).filter_by(name="Set-up - 12-String Acoustic").first():
    db.add(ServiceCatalog(name="Set-up - 12-String Acoustic", description="Setup for 12-string acoustic", default_cost=75, category_id=category_lookup['Setup']))
    db.commit()

# Service: Set-up - Nylon String Classical
if not db.query(ServiceCatalog).filter_by(name="Set-up - Nylon String Classical").first():
    db.add(ServiceCatalog(name="Set-up - Nylon String Classical", description="Classical guitar setup", default_cost=70, category_id=category_lookup['Setup']))
    db.commit()

# Service: Fret Level & Crown
if not db.query(ServiceCatalog).filter_by(name="Fret Level & Crown").first():
    db.add(ServiceCatalog(name="Fret Level & Crown", description="Precision fret leveling and recrowning", default_cost=150, category_id=category_lookup['Fretwork']))
    db.commit()

# Service: Spot Level Job
if not db.query(ServiceCatalog).filter_by(name="Spot Level Job").first():
    db.add(ServiceCatalog(name="Spot Level Job", description="Partial fret leveling", default_cost=95, category_id=category_lookup['Fretwork']))
    db.commit()

# Service: Refret (unfinished/unbound board)
if not db.query(ServiceCatalog).filter_by(name="Refret (unfinished/unbound board)").first():
    db.add(ServiceCatalog(name="Refret (unfinished/unbound board)", description="Full refret - rosewood/maple board", default_cost=300, category_id=category_lookup['Fretwork']))
    db.commit()

# Service: Refret (finished/unbound board)
if not db.query(ServiceCatalog).filter_by(name="Refret (finished/unbound board)").first():
    db.add(ServiceCatalog(name="Refret (finished/unbound board)", description="Full refret - finished board", default_cost=325, category_id=category_lookup['Fretwork']))
    db.commit()

# Service: Refret (unfinished/bound board)
if not db.query(ServiceCatalog).filter_by(name="Refret (unfinished/bound board)").first():
    db.add(ServiceCatalog(name="Refret (unfinished/bound board)", description="Refret with binding", default_cost=350, category_id=category_lookup['Fretwork']))
    db.commit()

# Service: Refret (finished/bound board)
if not db.query(ServiceCatalog).filter_by(name="Refret (finished/bound board)").first():
    db.add(ServiceCatalog(name="Refret (finished/bound board)", description="Refret with finish + binding", default_cost=375, category_id=category_lookup['Fretwork']))
    db.commit()

# Service: Nut Replacement (pre-slotted)
if not db.query(ServiceCatalog).filter_by(name="Nut Replacement (pre-slotted)").first():
    db.add(ServiceCatalog(name="Nut Replacement (pre-slotted)", description="Plastic or bone nut install", default_cost=60, category_id=category_lookup['Nut & Saddle']))
    db.commit()

# Service: Nut Replacement (carved from blank)
if not db.query(ServiceCatalog).filter_by(name="Nut Replacement (carved from blank)").first():
    db.add(ServiceCatalog(name="Nut Replacement (carved from blank)", description="Custom fit nut from blank", default_cost=90, category_id=category_lookup['Nut & Saddle']))
    db.commit()

# Service: Nut Replacement (Brass)
if not db.query(ServiceCatalog).filter_by(name="Nut Replacement (Brass)").first():
    db.add(ServiceCatalog(name="Nut Replacement (Brass)", description="Brass nut install", default_cost=120, category_id=category_lookup['Nut & Saddle']))
    db.commit()

# Service: Acoustic Saddle
if not db.query(ServiceCatalog).filter_by(name="Acoustic Saddle").first():
    db.add(ServiceCatalog(name="Acoustic Saddle", description="Custom-fit acoustic saddle", default_cost=65, category_id=category_lookup['Nut & Saddle']))
    db.commit()

# Service: Pickup Replacement - 1
if not db.query(ServiceCatalog).filter_by(name="Pickup Replacement - 1").first():
    db.add(ServiceCatalog(name="Pickup Replacement - 1", description="Install 1 passive pickup", default_cost=55, category_id=category_lookup['Electronics']))
    db.commit()

# Service: Pickup Replacement - 2
if not db.query(ServiceCatalog).filter_by(name="Pickup Replacement - 2").first():
    db.add(ServiceCatalog(name="Pickup Replacement - 2", description="Install 2 pickups", default_cost=75, category_id=category_lookup['Electronics']))
    db.commit()

# Service: Pickup Replacement - 3
if not db.query(ServiceCatalog).filter_by(name="Pickup Replacement - 3").first():
    db.add(ServiceCatalog(name="Pickup Replacement - 3", description="Install 3 pickups", default_cost=95, category_id=category_lookup['Electronics']))
    db.commit()

# Service: Potentiometer Replacement - 1st Pot
if not db.query(ServiceCatalog).filter_by(name="Potentiometer Replacement - 1st Pot").first():
    db.add(ServiceCatalog(name="Potentiometer Replacement - 1st Pot", description="Replace 1 volume/tone pot", default_cost=45, category_id=category_lookup['Electronics']))
    db.commit()

# Service: Potentiometer Replacement - Additional Pot
if not db.query(ServiceCatalog).filter_by(name="Potentiometer Replacement - Additional Pot").first():
    db.add(ServiceCatalog(name="Potentiometer Replacement - Additional Pot", description="Each additional pot", default_cost=25, category_id=category_lookup['Electronics']))
    db.commit()

# Service: Toggle Switch Replacement
if not db.query(ServiceCatalog).filter_by(name="Toggle Switch Replacement").first():
    db.add(ServiceCatalog(name="Toggle Switch Replacement", description="Replace pickup selector switch", default_cost=45, category_id=category_lookup['Electronics Cavity Shielding']))
    db.commit()

db.close()
print('✅ Services and categories seeded.')