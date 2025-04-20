# Luthios 🎸

**Luthios** is a mobile-first, full-featured repair shop backend designed for guitar luthiers.  
It handles everything from intake to inspection, invoicing to payments — and it's fully extensible.

---

## 🔧 Built With

- **FastAPI** – Python API framework
- **SQLAlchemy** – ORM for database modeling
- **SQLite** – Lightweight dev database
- **GitHub** – Version control
- **(Coming Soon)** – Stripe, PWA frontend, and mobile optimization

---

## 📦 Features

- Customer + Guitar tracking
- Repair orders and line items
- Intake forms and inspection metrics
- Notes system for jobs and instruments
- Work logs / technician time tracking
- Estimates, Invoices, and Payments
- Service catalog and templates
- Fully relational backend
- Ready for deployment

---

## 🚀 Local Dev Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # (coming soon)
python init_db.py
uvicorn main:app --reload
