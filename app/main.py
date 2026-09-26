
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import models, schemas, crud
from .irrigation import get_irrigation_recommendation


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Precision Farming Management System",
    description="REST API for Agricultural Monitoring and Resource Management",
    version="1.0.0"
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {
        "message": "Precision Farming Management System API is running"
    }


# ============================================================
# Field management
# ============================================================

@app.post(
    "/fields",
    response_model=schemas.FieldResponse,
    status_code=201
)
def create_field(
    field: schemas.FieldCreate,
    db: Session = Depends(get_db)
):
    return crud.create_field(db, field)


@app.get(
    "/fields",
    response_model=list[schemas.FieldResponse]
)
def get_fields(db: Session = Depends(get_db)):
    return crud.get_fields(db)


@app.get(
    "/fields/{field_id}",
    response_model=schemas.FieldResponse
)
def get_field(
    field_id: int,
    db: Session = Depends(get_db)
):
    field = crud.get_field(db, field_id)

    if field is None:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    return field


# ============================================================
# Sensor readings
# ============================================================

@app.post(
    "/sensor-readings",
    response_model=schemas.SensorReadingResponse
)
def create_sensor_reading(
    reading: schemas.SensorReadingCreate,
    db: Session = Depends(get_db)
):
    # A reading should always belong to a registered field.
    if crud.get_field(db, reading.field_id) is None:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    return crud.create_sensor_reading(db, reading)


@app.get(
    "/sensor-readings",
    response_model=list[schemas.SensorReadingResponse]
)
def get_sensor_readings(db: Session = Depends(get_db)):
    return crud.get_sensor_readings(db)


@app.get(
    "/sensor-readings/{reading_id}",
    response_model=schemas.SensorReadingResponse
)
def get_sensor_reading(
    reading_id: int,
    db: Session = Depends(get_db)
):
    reading = crud.get_sensor_reading(db, reading_id)

    if reading is None:
        raise HTTPException(
            status_code=404,
            detail="Sensor reading not found"
        )

    return reading


@app.put(
    "/sensor-readings/{reading_id}",
    response_model=schemas.SensorReadingResponse
)
def update_sensor_reading(
    reading_id: int,
    reading: schemas.SensorReadingCreate,
    db: Session = Depends(get_db)
):
    if crud.get_field(db, reading.field_id) is None:
        raise HTTPException(
            status_code=404,
            detail="Field not found"
        )

    updated_reading = crud.update_sensor_reading(
        db,
        reading_id,
        reading
    )

    if updated_reading is None:
        raise HTTPException(
            status_code=404,
            detail="Sensor reading not found"
        )

    return updated_reading


@app.delete("/sensor-readings/{reading_id}")
def delete_sensor_reading(
    reading_id: int,
    db: Session = Depends(get_db)
):
    deleted_reading = crud.delete_sensor_reading(
        db,
        reading_id
    )

    if deleted_reading is None:
        raise HTTPException(
            status_code=404,
            detail="Sensor reading not found"
        )

    return {
        "message": "Sensor reading deleted successfully",
        "id": reading_id
    }


# ============================================================
# Irrigation recommendations
# ============================================================

@app.get("/irrigation-recommendation/{soil_moisture}")
def irrigation_recommendation(soil_moisture: float):
    if soil_moisture < 0 or soil_moisture > 100:
        raise HTTPException(
            status_code=400,
            detail="Soil moisture must be between 0 and 100"
        )

    return get_irrigation_recommendation(soil_moisture)


@app.get(
    "/sensor-readings/{reading_id}/irrigation-recommendation"
)
def sensor_irrigation_recommendation(
    reading_id: int,
    db: Session = Depends(get_db)
):
    # This endpoint connects an actual stored reading to
    # the irrigation decision instead of requiring the
    # client to provide the moisture value separately.
    reading = crud.get_sensor_reading(db, reading_id)

    if reading is None:
        raise HTTPException(
            status_code=404,
            detail="Sensor reading not found"
        )

    recommendation = get_irrigation_recommendation(
        reading.soil_moisture
    )

    return {
        "reading_id": reading.id,
        "field_id": reading.field_id,
        **recommendation
    }


# ============================================================
# Fertilizer and resource inventory
# ============================================================

@app.post(
    "/inventory",
    response_model=schemas.InventoryItemResponse,
    status_code=201
)
def create_inventory_item(
    item: schemas.InventoryItemCreate,
    db: Session = Depends(get_db)
):
    return crud.create_inventory_item(db, item)


@app.get(
    "/inventory",
    response_model=list[schemas.InventoryItemResponse]
)
def get_inventory_items(db: Session = Depends(get_db)):
    return crud.get_inventory_items(db)
