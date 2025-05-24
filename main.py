from fastapi import FastAPI, Request, Depends, Form, File, UploadFile
from app.api import customers, guitars, makes, models, repair_intakes, repair_line_items, photos, inspections, metric_definitions, inspection_metrics, service_categories, service_catalog, estimates, invoices, payments, work_logs, notes,appointments
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from app import models
from app.models import Make, Model, InventoryItem
from app.database import SessionLocal, get_db
from sqlalchemy.orm import Session
from collections import defaultdict
from typing import List
import os
from fastapi.encoders import jsonable_encoder


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(customers.router)
app.include_router(guitars.router)
app.include_router(makes.router)
app.include_router(repair_intakes.router)
app.include_router(repair_line_items.router)
app.include_router(photos.router)
app.include_router(inspections.router)
app.include_router(metric_definitions.router)
app.include_router(inspection_metrics.router)
app.include_router(service_categories.router)
app.include_router(service_catalog.router)
app.include_router(estimates.router)
app.include_router(invoices.router)
app.include_router(payments.router)
app.include_router(work_logs.router)
app.include_router(notes.router)
app.include_router(appointments.router)

@app.get("/")
def read_root():
    return {"message": "🎸 Welcome to luthiOS API"}

@app.get("/intake", response_class=HTMLResponse)
async def intake_form(request: Request, db: Session = Depends(get_db)):
    makes = db.query(Make).all()
    models = db.query(Model).all()
    stock_gauges = db.query(InventoryItem.gauge, InventoryItem.guitar_type).filter(
        InventoryItem.item_type == "strings",
        InventoryItem.in_stock_qty > 0,
        InventoryItem.active == True
    ).distinct().all()

    gauge_by_type = defaultdict(list)
    for gauge, gtype in stock_gauges:
        if gtype:
            gauge_by_type[gtype.lower()].append(gauge)

    context = {
        "request": request,
        "makes": makes,
        "models": models,
        "models_json": jsonable_encoder([
            {"name": m.name, "type": m.guitar_type or ""}
            for m in models
        ]),
        "in_stock_gauges": gauge_by_type
    }
    return templates.TemplateResponse("intake.html", context)

@app.post("/submit-intake")
async def submit_intake(
    request: Request,
    db: Session = Depends(get_db),
    # Customer
    first_name: str = Form(...),
    last_name: str = Form(...),
    email: str = Form(None),
    phone: str = Form(None),
    referral_source: str = Form(None),
    marketing_opt_in: bool = Form(False),

    # Guitar
    type: str = Form(...),
    make_select: str = Form(None),
    make_custom: str = Form(None),
    model_select: str = Form(None),
    model_custom: str = Form(None),
    year: int = Form(None),
    serial_number: str = Form(None),
    estimated_value: float = Form(None),

    # Repair Intake
    string_gauge_select: str = Form(None),
    string_gauge_custom: str = Form(None),
    tuning: str = Form(None),
    case_provided: bool = Form(False),
    strings_provided: bool = Form(False),
    accept_stock_strings: str = Form(None),
    custom_string_request: str = Form(None),

    # Services
    services: List[str] = Form(None),

    # Repair Description
    repair_description: str = Form(None),

    # Photos
    photos: List[UploadFile] = File(None),

    # Concierge
    concierge_requested: bool = Form(False),
    concierge_street: str = Form(None),
    concierge_address2: str = Form(None),
    concierge_city: str = Form(None),
    concierge_zip: str = Form(None),
):
    # 👇 Good spot: handle custom selections
    make = make_custom.strip() if make_select == "other" else make_select
    model = model_custom.strip() if model_select == "other" else model_select
    string_gauge = string_gauge_custom.strip() if string_gauge_select == "other" else string_gauge_select

    # 🔥 Your normal logic continues here (STEP 1, STEP 2, etc.)

    # STEP 1: Find or create Customer
    existing_customer = db.query(models.Customer).filter_by(
        first_name=first_name.strip(),
        last_name=last_name.strip(),
        phone=phone.strip() if phone else None
    ).first()

    if existing_customer:
        customer = existing_customer
    else:
        customer = models.Customer(
            first_name=first_name.strip(),
            last_name=last_name.strip(),
            email=email.strip() if email else None,
            phone=phone.strip() if phone else None,
            marketing_opt_in=marketing_opt_in,
            referral_source=referral_source
        )
        db.add(customer)
        db.commit()
        db.refresh(customer)
    # STEP 2: Create Guitar
    make = make_custom.strip() if make_select == "other" else make_select
    model = model_custom.strip() if model_select == "other" else model_select

    string_gauge = string_gauge_custom.strip() if string_gauge_select == "other" else string_gauge_select

    guitar = models.Guitar(
        customer_id=customer.id,
        make=make,
        model=model,
        type=type,
        serial_number=serial_number.strip() if serial_number else None,
        year=year,
        estimated_value=estimated_value,
        string_gauge=string_gauge,
        tuning=tuning.strip() if tuning else None
    )

    db.add(guitar)
    db.commit()
    db.refresh(guitar)
    # STEP 3: Create Repair Order
    repair_order = models.RepairOrder(
        guitar_id=guitar.id,
        status="Intake Received",
        description=repair_description.strip() if repair_description else None
    )

    db.add(repair_order)
    db.commit()
    db.refresh(repair_order)
    # STEP 4: Create Repair Intake
    intake = models.RepairIntake(
        repair_order_id=repair_order.id,
        string_gauge=string_gauge,
        tuning=tuning.strip() if tuning else None,
        case_provided=case_provided,
        strings_provided=strings_provided,
        accept_stock_strings=True if accept_stock_strings == "yes" else False,
        custom_string_request=custom_string_request.strip() if custom_string_request else None,
        concierge_requested=concierge_requested,
        concierge_street=concierge_street.strip() if concierge_street else None,
        concierge_address2=concierge_address2.strip() if concierge_address2 else None,
        concierge_city=concierge_city.strip() if concierge_city else None,
        concierge_zip=concierge_zip.strip() if concierge_zip else None
    )

    db.add(intake)
    db.commit()
    db.refresh(intake)
    # STEP 5: Create Repair Line Items
    if services:
        for service_name in services:
            # Try to match the service from ServiceCatalog
            service = db.query(models.ServiceCatalog).filter_by(name=service_name).first()

            if service:
                line_item = models.RepairLineItem(
                    repair_id=repair_order.id,
                    service_id=service.id,
                    name=service.name,
                    description=service.description,
                    cost=service.default_cost
                )
                db.add(line_item)
        db.commit()
    # STEP 6: Handle uploaded Photos
    if photos:
        for photo in photos:
            if photo.filename:
                contents = await photo.read()

                # Save the uploaded photo to disk (static/uploads/)
                upload_dir = "static/uploads"
                os.makedirs(upload_dir, exist_ok=True)

                filename = f"{repair_order.id}_{photo.filename}"
                filepath = os.path.join(upload_dir, filename)

                with open(filepath, "wb") as f:
                    f.write(contents)

                # Save the photo record in database
                photo_record = models.GuitarPhoto(
                    guitar_id=guitar.id,
                    photo_url=f"/{filepath}",
                    caption=None
                )
                db.add(photo_record)
        db.commit()

    return {"message": "🎸 Intake submission received!"}
