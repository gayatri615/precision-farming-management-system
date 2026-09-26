
from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime

from .database import Base


class Field(Base):
    # Basic information about each field managed by the system.
    __tablename__ = "fields"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    crop_type = Column(String, nullable=False)


class SensorReading(Base):
    # Stores environmental readings received from field sensors.
    __tablename__ = "sensor_readings"

    id = Column(Integer, primary_key=True, index=True)
    field_id = Column(Integer, index=True, nullable=False)
    soil_moisture = Column(Float, nullable=False)
    temperature = Column(Float, nullable=False)
    humidity = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


class InventoryItem(Base):
    # Tracks fertilizers and other agricultural resources.
    __tablename__ = "inventory_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
