# Precision Farming Management System

A REST API for agricultural monitoring, irrigation decision support, and resource management, developed using Python and FastAPI.

## Project Overview

The Precision Farming Management System (PFMS) is a lightweight backend application designed to simulate and manage agricultural field data.

The system provides REST APIs for:

- Managing agricultural fields
- Recording soil and environmental sensor readings
- Validating sensor data
- Generating irrigation recommendations
- Managing agricultural resource inventory
- Testing normal, boundary, invalid, and failure scenarios

The project was developed as a Software Engineering project with a focus on REST API development, data validation, automated testing, and software quality.

## Key Features

### Field Management

- Create agricultural fields
- Store field location and crop information
- Retrieve registered fields
- Handle requests for unavailable fields

### Sensor Monitoring

- Record soil moisture, temperature, and humidity
- Retrieve sensor readings
- Update existing readings
- Delete sensor readings
- Validate sensor input values
- Verify that sensor readings belong to valid fields

### Irrigation Decision Support

The system uses a simple rule-based model based on soil moisture:

| Soil Moisture | Recommendation |
|---|---|
| Below 30% | Irrigation required |
| 30%–60% | Monitor soil moisture |
| Above 60% | No irrigation required |

The rule-based implementation provides a simple baseline that can later be extended with crop-specific thresholds or machine-learning-based recommendations.

### Inventory Management

- Add agricultural resources
- Store fertilizer quantities and units
- Retrieve inventory information
- Validate inventory quantities and required fields

## Technology Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- pytest
- HTTPX

## Project Structure

```text
precision-farming-management-system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── irrigation.py
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── seed_data.py
├── phase3_test_report.txt
├── defect_log.txt
├── requirements.txt
├── .gitignore
├── README.md
└── PFMS_Project_Development.ipynb
