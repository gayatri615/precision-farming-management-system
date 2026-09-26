
from PFMS.app.database import SessionLocal, Base, engine
from PFMS.app import models


Base.metadata.create_all(bind=engine)

db = SessionLocal()

try:
    fields = [
        {
            "name": "North Field",
            "location": "Chennai",
            "crop_type": "Tomato"
        },
        {
            "name": "East Field",
            "location": "Coimbatore",
            "crop_type": "Chilli"
        },
        {
            "name": "Greenhouse Field",
            "location": "Bengaluru",
            "crop_type": "Cucumber"
        }
    ]

    field_objects = []

    for field_data in fields:
        existing = db.query(models.Field).filter(
            models.Field.name == field_data["name"]
        ).first()

        if existing:
            field_objects.append(existing)
        else:
            field = models.Field(**field_data)
            db.add(field)
            db.flush()
            field_objects.append(field)

    # These values simulate what sensors might report from
    # fields with different environmental conditions.
    if db.query(models.SensorReading).count() < 5:
        readings = [
            {
                "field_id": field_objects[0].id,
                "soil_moisture": 24.5,
                "temperature": 31.2,
                "humidity": 64.0
            },
            {
                "field_id": field_objects[0].id,
                "soil_moisture": 47.0,
                "temperature": 29.8,
                "humidity": 69.0
            },
            {
                "field_id": field_objects[1].id,
                "soil_moisture": 28.0,
                "temperature": 30.5,
                "humidity": 61.0
            },
            {
                "field_id": field_objects[1].id,
                "soil_moisture": 72.0,
                "temperature": 28.4,
                "humidity": 74.0
            },
            {
                "field_id": field_objects[2].id,
                "soil_moisture": 55.0,
                "temperature": 27.9,
                "humidity": 78.0
            }
        ]

        for reading_data in readings:
            db.add(models.SensorReading(**reading_data))

    inventory = [
        {
            "name": "NPK 10-26-26",
            "category": "Fertilizer",
            "quantity": 50.0,
            "unit": "kg"
        },
        {
            "name": "Urea",
            "category": "Nitrogen Fertilizer",
            "quantity": 30.0,
            "unit": "kg"
        },
        {
            "name": "Potassium Sulphate",
            "category": "Potassium Fertilizer",
            "quantity": 20.0,
            "unit": "kg"
        }
    ]

    if db.query(models.InventoryItem).count() == 0:
        for item_data in inventory:
            db.add(models.InventoryItem(**item_data))

    db.commit()

    print("Sample PFMS data added successfully.")

finally:
    db.close()
