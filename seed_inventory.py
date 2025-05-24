from app.database import SessionLocal
from app.models import InventoryItem

db = SessionLocal()

# Item: DAD-E-0942
if not db.query(InventoryItem).filter_by(sku="DAD-E-0942").first():
    db.add(InventoryItem(
        sku="DAD-E-0942",
        item_type="strings",
        brand="D'Addario",
        gauge="9-42",
        guitar_type="electric",
        description="""D'Addario Nickel Wound Electric Guitar Strings, Super Light, 9-42""",
        vendor="Sweetwater",
        in_stock_qty=10,
        restock_threshold=3,
        location="Drawer 1",
        active=True
    ))
    db.commit()

# Item: DAD-E-1046
if not db.query(InventoryItem).filter_by(sku="DAD-E-1046").first():
    db.add(InventoryItem(
        sku="DAD-E-1046",
        item_type="strings",
        brand="D'Addario",
        gauge="10-46",
        guitar_type="electric",
        description="""D'Addario Nickel Wound Electric Guitar Strings, Regular Light, 10-46""",
        vendor="Sweetwater",
        in_stock_qty=8,
        restock_threshold=3,
        location="Drawer 1",
        active=True
    ))
    db.commit()

# Item: DAD-A-1254
if not db.query(InventoryItem).filter_by(sku="DAD-A-1254").first():
    db.add(InventoryItem(
        sku="DAD-A-1254",
        item_type="strings",
        brand="D'Addario",
        gauge="12-54",
        guitar_type="acoustic",
        description="""D'Addario Phosphor Bronze Acoustic Guitar Strings, Light, 12-54""",
        vendor="Sweetwater",
        in_stock_qty=6,
        restock_threshold=2,
        location="Drawer 2",
        active=True
    ))
    db.commit()

db.close()
print("✅ Inventory items seeded.")