
from pydantic import BaseModel, Field
from datetime import datetime


class FieldCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    location: str = Field(..., min_length=2, max_length=150)
    crop_type: str = Field(..., min_length=2, max_length=100)


class FieldResponse(BaseModel):
    id: int
    name: str
    location: str
    crop_type: str

    class Config:
        from_attributes = True


class SensorReadingCreate(BaseModel):
    # Sensor values are restricted to realistic ranges.
    field_id: int = Field(..., gt=0)
    soil_moisture: float = Field(..., ge=0, le=100)
    temperature: float = Field(..., ge=-50, le=80)
    humidity: float = Field(..., ge=0, le=100)


class SensorReadingResponse(BaseModel):
    id: int
    field_id: int
    soil_moisture: float
    temperature: float
    humidity: float
    timestamp: datetime

    class Config:
        from_attributes = True


class InventoryItemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    category: str = Field(..., min_length=2, max_length=50)
    quantity: float = Field(..., ge=0)
    unit: str = Field(..., min_length=1, max_length=20)


class InventoryItemResponse(BaseModel):
    id: int
    name: str
    category: str
    quantity: float
    unit: str

    class Config:
        from_attributes = True
