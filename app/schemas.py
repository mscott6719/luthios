from pydantic import BaseModel
import datetime

class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone: str
    marketing_opt_in: bool = False

class GuitarCreate(BaseModel):
    customer_id: int
    make_id: int = None
    model_id: int = None
    serial_number: str = None
    type: str = None
    year: int = None
    color: str = None
    pickup_config: str = None
    estimated_value: float = None
    string_count: int = None

class MakeCreate(BaseModel):
    name: str

class ModelCreate(BaseModel):
    name: str
    make_id: int

class RepairIntakeCreate(BaseModel):
    repair_order_id: int
    string_gauge: str = None
    tuning: str = None
    case_provided: bool = False
    strings_provided: bool = False
    terms_accepted: bool = False
    form_signed: bool = False
    concierge_requested: bool = False
    concierge_type: str = None
    concierge_address: str = None
    concierge_status: str = "Pending"

class RepairLineItemCreate(BaseModel):
    repair_id: int
    service_id: int
    name: str = None         # Optional override name
    description: str = None  # Optional override description
    custom_cost: float = None
    is_completed: bool = False

class PhotoCreate(BaseModel):
    guitar_id: int = None
    repair_order_id: int = None
    photo_url: str
    caption: str = None

class InspectionSessionCreate(BaseModel):
    guitar_id: int
    repair_order_id: int = None
    technician: str = None


class MetricDefinitionCreate(BaseModel):
    name: str
    units: str
    category: str
    per_string: bool = False
    is_required: bool = False
    sort_order: int = 0
    description: str = None


class InspectionMetricCreate(BaseModel):
    inspection_session_id: int
    metric_definition_id: int
    value: str
    string_number: int = None
    repair_line_item_id: int = None

class ServiceCategoryCreate(BaseModel):
    name: str
    description: str = None

class ServiceCatalogCreate(BaseModel):
    name: str
    description: str = None
    default_cost: float = 0.0
    category_id: int = None

class EstimateCreate(BaseModel):
    repair_order_id: int
    status: str = "Draft"
    subtotal: float
    tax: float
    tax_mode: str
    total: float
    stripe_estimate_id: str = None
    stripe_url: str = None
    converted_invoice_id: int = None

class InvoiceCreate(BaseModel):
    repair_order_id: int
    status: str
    subtotal: float
    tax: float
    tax_mode: str
    total: float
    stripe_invoice_id: str = None
    stripe_url: str = None
    from_estimate_id: int = None

class PaymentCreate(BaseModel):
    invoice_id: int
    amount: float
    date_paid: datetime.datetime
    method: str
    status: str
    stripe_payment_id: str = None

class WorkLogCreate(BaseModel):
    repair_line_item_id: int
    start_time: datetime.datetime = None
    end_time: datetime.datetime = None
    duration_minutes: float = None
    manual_entry: bool = False
    note: str = None

class NoteCreate(BaseModel):
    note_content: str
    customer_id: int = None
    guitar_id: int = None
    repair_order_id: int = None
    repair_line_item_id: int = None
    note_type: str = None
