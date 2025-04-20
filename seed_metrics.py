from app.database import SessionLocal
from app.models import MetricDefinition

db = SessionLocal()

# Metric: Action height at 12th fret
if not db.query(MetricDefinition).filter_by(name="Action height at 12th fret").first():
    db.add(MetricDefinition(
        name="Action height at 12th fret",
        units="mm",
        category="Setup",
        per_string=True,
        is_required=True,
        sort_order=1,
        description="Measured from bottom of string to top of 12th fret"
    ))
    db.commit()

# Metric: Action height at 1st fret
if not db.query(MetricDefinition).filter_by(name="Action height at 1st fret").first():
    db.add(MetricDefinition(
        name="Action height at 1st fret",
        units="mm",
        category="Setup",
        per_string=True,
        is_required=False,
        sort_order=2,
        description="Measured from bottom of string to top of 1st fret"
    ))
    db.commit()

# Metric: Neck relief
if not db.query(MetricDefinition).filter_by(name="Neck relief").first():
    db.add(MetricDefinition(
        name="Neck relief",
        units="mm",
        category="Setup",
        per_string=False,
        is_required=False,
        sort_order=3,
        description="Measured at 7th/8th fret with capo and finger on last fret"
    ))
    db.commit()

# Metric: Nut slot height
if not db.query(MetricDefinition).filter_by(name="Nut slot height").first():
    db.add(MetricDefinition(
        name="Nut slot height",
        units="mm",
        category="Setup",
        per_string=True,
        is_required=False,
        sort_order=4,
        description="Measured at 1st fret while string is unfretted"
    ))
    db.commit()

# Metric: String spacing at bridge
if not db.query(MetricDefinition).filter_by(name="String spacing at bridge").first():
    db.add(MetricDefinition(
        name="String spacing at bridge",
        units="mm",
        category="Setup",
        per_string=False,
        is_required=False,
        sort_order=5,
        description="Total spacing between outermost strings at bridge"
    ))
    db.commit()

# Metric: String spacing at nut
if not db.query(MetricDefinition).filter_by(name="String spacing at nut").first():
    db.add(MetricDefinition(
        name="String spacing at nut",
        units="mm",
        category="Setup",
        per_string=False,
        is_required=False,
        sort_order=6,
        description="Total spacing between outermost strings at nut"
    ))
    db.commit()

# Metric: Bridge saddle height
if not db.query(MetricDefinition).filter_by(name="Bridge saddle height").first():
    db.add(MetricDefinition(
        name="Bridge saddle height",
        units="mm",
        category="Setup",
        per_string=True,
        is_required=False,
        sort_order=7,
        description="Saddle height from bridge base to string contact point"
    ))
    db.commit()

# Metric: String gauge
if not db.query(MetricDefinition).filter_by(name="String gauge").first():
    db.add(MetricDefinition(
        name="String gauge",
        units="gauge",
        category="Setup",
        per_string=False,
        is_required=False,
        sort_order=8,
        description="String set used for setup"
    ))
    db.commit()

# Metric: Tap tone frequency
if not db.query(MetricDefinition).filter_by(name="Tap tone frequency").first():
    db.add(MetricDefinition(
        name="Tap tone frequency",
        units="Hz",
        category="Acoustic",
        per_string=False,
        is_required=False,
        sort_order=1,
        description="Tap top and measure peak frequency with mic"
    ))
    db.commit()

# Metric: Body resonance frequency
if not db.query(MetricDefinition).filter_by(name="Body resonance frequency").first():
    db.add(MetricDefinition(
        name="Body resonance frequency",
        units="Hz",
        category="Acoustic",
        per_string=False,
        is_required=False,
        sort_order=2,
        description="Main resonance peak of the body"
    ))
    db.commit()

# Metric: Top deflection under tension
if not db.query(MetricDefinition).filter_by(name="Top deflection under tension").first():
    db.add(MetricDefinition(
        name="Top deflection under tension",
        units="mm",
        category="Acoustic",
        per_string=False,
        is_required=False,
        sort_order=3,
        description="Measured dip/arch of top when strings are tuned"
    ))
    db.commit()

# Metric: Sustain time
if not db.query(MetricDefinition).filter_by(name="Sustain time").first():
    db.add(MetricDefinition(
        name="Sustain time",
        units="seconds",
        category="Acoustic",
        per_string=True,
        is_required=False,
        sort_order=4,
        description="Time a fretted note rings before falling below threshold"
    ))
    db.commit()

# Metric: Pickup output
if not db.query(MetricDefinition).filter_by(name="Pickup output").first():
    db.add(MetricDefinition(
        name="Pickup output",
        units="mV",
        category="Electronics",
        per_string=True,
        is_required=False,
        sort_order=1,
        description="Measured with strings plucked and multimeter on output jack"
    ))
    db.commit()

# Metric: Pot resistance
if not db.query(MetricDefinition).filter_by(name="Pot resistance").first():
    db.add(MetricDefinition(
        name="Pot resistance",
        units="kΩ",
        category="Electronics",
        per_string=False,
        is_required=False,
        sort_order=2,
        description="Resistance of volume/tone pots"
    ))
    db.commit()

# Metric: Capacitor value
if not db.query(MetricDefinition).filter_by(name="Capacitor value").first():
    db.add(MetricDefinition(
        name="Capacitor value",
        units="µF",
        category="Electronics",
        per_string=False,
        is_required=False,
        sort_order=3,
        description="Measured or labeled value of tone capacitor"
    ))
    db.commit()

# Metric: Output jack resistance
if not db.query(MetricDefinition).filter_by(name="Output jack resistance").first():
    db.add(MetricDefinition(
        name="Output jack resistance",
        units="Ω",
        category="Electronics",
        per_string=False,
        is_required=False,
        sort_order=4,
        description="Check for continuity or unwanted resistance at jack"
    ))
    db.commit()

# Metric: Battery voltage
if not db.query(MetricDefinition).filter_by(name="Battery voltage").first():
    db.add(MetricDefinition(
        name="Battery voltage",
        units="V",
        category="Electronics",
        per_string=False,
        is_required=False,
        sort_order=5,
        description="For active pickups or onboard preamp"
    ))
    db.commit()

# Metric: Neck angle
if not db.query(MetricDefinition).filter_by(name="Neck angle").first():
    db.add(MetricDefinition(
        name="Neck angle",
        units="degrees",
        category="Structural",
        per_string=False,
        is_required=False,
        sort_order=1,
        description="Set neck geometry vs body"
    ))
    db.commit()

# Metric: Fret wear level
if not db.query(MetricDefinition).filter_by(name="Fret wear level").first():
    db.add(MetricDefinition(
        name="Fret wear level",
        units="%",
        category="Fretwork",
        per_string=True,
        is_required=False,
        sort_order=1,
        description="Percent worn compared to new fret height"
    ))
    db.commit()

# Metric: Crack length
if not db.query(MetricDefinition).filter_by(name="Crack length").first():
    db.add(MetricDefinition(
        name="Crack length",
        units="mm",
        category="Structural",
        per_string=False,
        is_required=False,
        sort_order=2,
        description="Measured crack length"
    ))
    db.commit()

# Metric: Humidity
if not db.query(MetricDefinition).filter_by(name="Humidity").first():
    db.add(MetricDefinition(
        name="Humidity",
        units="% RH",
        category="Inspection Environment",
        per_string=False,
        is_required=False,
        sort_order=1,
        description="Room humidity during inspection"
    ))
    db.commit()

# Metric: Temperature
if not db.query(MetricDefinition).filter_by(name="Temperature").first():
    db.add(MetricDefinition(
        name="Temperature",
        units="°F",
        category="Inspection Environment",
        per_string=False,
        is_required=False,
        sort_order=2,
        description="Room temperature during inspection"
    ))
    db.commit()

# Metric: Customer satisfaction rating
if not db.query(MetricDefinition).filter_by(name="Customer satisfaction rating").first():
    db.add(MetricDefinition(
        name="Customer satisfaction rating",
        units="1–5 scale",
        category="Customer Service",
        per_string=False,
        is_required=False,
        sort_order=1,
        description="From post-service survey"
    ))
    db.commit()

# Metric: Time since last string change
if not db.query(MetricDefinition).filter_by(name="Time since last string change").first():
    db.add(MetricDefinition(
        name="Time since last string change",
        units="days",
        category="Setup",
        per_string=True,
        is_required=False,
        sort_order=9,
        description="Self-reported or based on string wear"
    ))
    db.commit()

db.close()
print('✅ Metric definitions seeded.')