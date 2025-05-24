from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship, declarative_base
import datetime

Base = declarative_base()

# ------------------------
# Core Tables
# ------------------------

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(50))
    marketing_opt_in = Column(Boolean, default=False)
    referral_source = Column(String(100))

    guitars = relationship("Guitar", back_populates="customer")
    notes = relationship("Note", back_populates="customer")


class Guitar(Base):
    __tablename__ = "guitars"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    make_id = Column(Integer, ForeignKey("makes.id"))
    model_id = Column(Integer, ForeignKey("models.id"))
    serial_number = Column(String(100))
    type = Column(String(50))
    year = Column(Integer)
    color = Column(String(50))
    pickup_config = Column(String(50))
    estimated_value = Column(Float)
    string_count = Column(Integer)

    customer = relationship("Customer", back_populates="guitars")
    notes = relationship("Note", back_populates="guitar")
    repairs = relationship("RepairOrder", back_populates="guitar")


class Make(Base):
    __tablename__ = "makes"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    models = relationship("Model", back_populates="make")

class Model(Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    make_id = Column(Integer, ForeignKey("makes.id"))
    guitar_type = Column(String(50))  # "Acoustic" or "Electric"

    make = relationship("Make", back_populates="models")


class RepairOrder(Base):
    __tablename__ = "repair_orders"
    id = Column(Integer, primary_key=True)
    guitar_id = Column(Integer, ForeignKey("guitars.id"))
    status = Column(String(100))
    description = Column(Text)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)

    line_items = relationship("RepairLineItem", back_populates="repair_order")
    notes = relationship("Note", back_populates="repair_order")
    guitar = relationship("Guitar", back_populates="repairs")
    appointments = relationship("Appointment", back_populates="repair_order", cascade="all, delete-orphan")


class RepairLineItem(Base):
    __tablename__ = "repair_line_items"
    id = Column(Integer, primary_key=True)
    repair_id = Column(Integer, ForeignKey("repair_orders.id"))
    service_id = Column(Integer, ForeignKey("service_catalog.id"))
    name = Column(String(100))
    description = Column(Text)
    custom_cost = Column(Float)
    is_completed = Column(Boolean, default=False)

    repair_order = relationship("RepairOrder", back_populates="line_items")
    notes = relationship("Note", back_populates="repair_line_item")
    service = relationship("ServiceCatalog")
    work_logs = relationship("WorkLog", back_populates="repair_line_item")

class ServiceCatalog(Base):
    __tablename__ = "service_catalog"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(Text)
    default_cost = Column(Float)
    category_id = Column(Integer, ForeignKey("service_categories.id"), nullable=True)

    category = relationship("ServiceCategory", back_populates="services")


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    amount = Column(Float)
    date_paid = Column(DateTime)
    method = Column(String(50))
    status = Column(String(50))
    stripe_payment_id = Column(String(100))


class Note(Base):
    __tablename__ = "notes"
    id = Column(Integer, primary_key=True)
    note_content = Column(Text)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    guitar_id = Column(Integer, ForeignKey("guitars.id"), nullable=True)
    repair_order_id = Column(Integer, ForeignKey("repair_orders.id"), nullable=True)
    repair_line_item_id = Column(Integer, ForeignKey("repair_line_items.id"), nullable=True)
    date_added = Column(DateTime, default=datetime.datetime.utcnow)
    note_type = Column(String(50))

    customer = relationship("Customer", back_populates="notes")
    guitar = relationship("Guitar", back_populates="notes")
    repair_order = relationship("RepairOrder", back_populates="notes")
    repair_line_item = relationship("RepairLineItem", back_populates="notes")

class RepairIntake(Base):
    __tablename__ = "repair_intakes"
    id = Column(Integer, primary_key=True)
    repair_order_id = Column(Integer, ForeignKey("repair_orders.id"))
    string_gauge = Column(String(50))
    tuning = Column(String(50))
    case_provided = Column(Boolean, default=False)
    strings_provided = Column(Boolean, default=False)
    accept_stock_strings = Column(Boolean, nullable=True)
    custom_string_request = Column(Text, nullable=True)
    terms_accepted = Column(Boolean, default=False)
    form_signed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    concierge_requested = Column(Boolean, default=False)
    concierge_address = Column(Text, nullable=True)
    concierge_street = Column(String(200), nullable=True)
    concierge_address2 = Column(String(200), nullable=True)
    concierge_city = Column(String(100), nullable=True)
    concierge_zip = Column(String(20), nullable=True)


class GuitarPhoto(Base):
    __tablename__ = "guitar_photos"
    id = Column(Integer, primary_key=True)
    guitar_id = Column(Integer, ForeignKey("guitars.id"), nullable=True)
    repair_order_id = Column(Integer, ForeignKey("repair_orders.id"), nullable=True)
    photo_url = Column(String(200))
    caption = Column(String(100))

class InspectionSession(Base):
    __tablename__ = "inspection_sessions"
    id = Column(Integer, primary_key=True)
    guitar_id = Column(Integer, ForeignKey("guitars.id"))
    repair_order_id = Column(Integer, ForeignKey("repair_orders.id"), nullable=True)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    technician = Column(String(100))  # Optional: future user link

    metrics = relationship("InspectionMetric", back_populates="session")

class MetricDefinition(Base):
    __tablename__ = "metric_definitions"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    units = Column(String(50))
    category_id = Column(Integer, ForeignKey("service_categories.id"))
    category = relationship("ServiceCategory", back_populates="metrics")
    per_string = Column(Boolean, default=False)
    is_required = Column(Boolean, default=False)
    sort_order = Column(Integer)
    description = Column(Text)


class InspectionMetric(Base):
    __tablename__ = "inspection_metrics"
    id = Column(Integer, primary_key=True)
    inspection_session_id = Column(Integer, ForeignKey("inspection_sessions.id"))
    metric_definition_id = Column(Integer, ForeignKey("metric_definitions.id"))
    value = Column(String(100))  # Can hold mm, %, etc.
    string_number = Column(Integer, nullable=True)
    repair_line_item_id = Column(Integer, ForeignKey("repair_line_items.id"), nullable=True)

    session = relationship("InspectionSession", back_populates="metrics")
    definition = relationship("MetricDefinition")


class ServiceCategory(Base):
    __tablename__ = "service_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(Text)
    metrics = relationship("MetricDefinition", back_populates="category")
    services = relationship("ServiceCatalog", back_populates="category")

class Estimate(Base):
    __tablename__ = "estimates"
    id = Column(Integer, primary_key=True)
    repair_order_id = Column(Integer, ForeignKey("repair_orders.id"))
    status = Column(String(50), default="Draft")
    subtotal = Column(Float)
    tax = Column(Float)
    tax_mode = Column(String(20))  # Flat or %
    total = Column(Float)
    stripe_estimate_id = Column(String(100))
    stripe_url = Column(String(200))
    converted_invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=True)

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    repair_order_id = Column(Integer, ForeignKey("repair_orders.id"))
    status = Column(String(50))
    subtotal = Column(Float)
    tax = Column(Float)
    tax_mode = Column(String(20))  # Flat or %
    total = Column(Float)
    stripe_invoice_id = Column(String(100))
    stripe_url = Column(String(200))
    from_estimate_id = Column(Integer, ForeignKey("estimates.id"), nullable=True)

class WorkLog(Base):
    __tablename__ = "work_logs"
    id = Column(Integer, primary_key=True)
    repair_line_item_id = Column(Integer, ForeignKey("repair_line_items.id"))
    start_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    duration_minutes = Column(Float, nullable=True)
    manual_entry = Column(Boolean, default=False)
    note = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    repair_line_item = relationship("RepairLineItem", back_populates="work_logs")

class InventoryItem(Base):
    __tablename__ = "inventory_items"
    id = Column(Integer, primary_key=True)
    sku = Column(String(100), unique=True)
    item_type = Column(String(50))  # e.g. "strings", "pickup"
    guitar_type = Column(String(20), nullable=True)  # "electric", "acoustic", "nylon", etc.
    brand = Column(String(100))
    model = Column(String(100), nullable=True)
    gauge = Column(String(50), nullable=True)
    description = Column(Text, nullable=True)
    vendor = Column(String(100), nullable=True)
    reorder_link = Column(String(300), nullable=True)  # optional purchase URL
    in_stock_qty = Column(Integer, default=0)
    restock_threshold = Column(Integer, default=0)
    unit_cost = Column(Float, nullable=True)
    retail_price = Column(Float, nullable=True)
    location = Column(String(100), nullable=True)
    barcode = Column(String(100), nullable=True)  # for scanning/labels
    qr_code_path = Column(String(200), nullable=True)  # if generating & storing locally
    last_restocked = Column(DateTime, nullable=True)
    active = Column(Boolean, default=True)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    repair_order_id = Column(Integer, ForeignKey("repair_orders.id"), nullable=False)
    appointment_type = Column(String(50))  # pickup, dropoff, in-shop
    scheduled_time = Column(DateTime, nullable=False)
    location = Column(String(200), nullable=True)
    notes = Column(Text, nullable=True)
    status = Column(String(50), default="scheduled")

    repair_order = relationship("RepairOrder", back_populates="appointments")

