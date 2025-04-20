from fastapi import FastAPI
from app.api import customers, guitars, makes, models, repair_intakes, repair_line_items, photos, inspections, metric_definitions, inspection_metrics, service_categories, service_catalog, estimates, invoices, payments, work_logs, notes

app = FastAPI()

app.include_router(customers.router)
app.include_router(guitars.router)
app.include_router(makes.router)
app.include_router(models.router)
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

@app.get("/")
def read_root():
    return {"message": "🎸 Welcome to luthiOS API"}
