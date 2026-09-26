
from sqlalchemy.orm import Session

from . import models, schemas


# -------------------- Fields --------------------

def create_field(db: Session, field: schemas.FieldCreate):
    db_field = models.Field(**field.model_dump())

    db.add(db_field)
    db.commit()
    db.refresh(db_field)

    return db_field


def get_fields(db: Session):
    return db.query(models.Field).all()


def get_field(db: Session, field_id: int):
    return db.query(models.Field).filter(
        models.Field.id == field_id
    ).first()


# -------------------- Sensor readings --------------------

def create_sensor_reading(db: Session, reading: schemas.SensorReadingCreate):
    db_reading = models.SensorReading(**reading.model_dump())

    db.add(db_reading)
    db.commit()
    db.refresh(db_reading)

    return db_reading


def get_sensor_readings(db: Session):
    return db.query(models.SensorReading).all()


def get_sensor_reading(db: Session, reading_id: int):
    return db.query(models.SensorReading).filter(
        models.SensorReading.id == reading_id
    ).first()


def update_sensor_reading(
    db: Session,
    reading_id: int,
    reading: schemas.SensorReadingCreate
):
    db_reading = get_sensor_reading(db, reading_id)

    if db_reading is None:
        return None

    for key, value in reading.model_dump().items():
        setattr(db_reading, key, value)

    db.commit()
    db.refresh(db_reading)

    return db_reading


def delete_sensor_reading(db: Session, reading_id: int):
    db_reading = get_sensor_reading(db, reading_id)

    if db_reading is None:
        return None

    db.delete(db_reading)
    db.commit()

    return db_reading


# -------------------- Inventory --------------------

def create_inventory_item(
    db: Session,
    item: schemas.InventoryItemCreate
):
    db_item = models.InventoryItem(**item.model_dump())

    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


def get_inventory_items(db: Session):
    return db.query(models.InventoryItem).all()
