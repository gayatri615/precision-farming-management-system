# Precision Farming Management System

A REST API for agricultural monitoring, irrigation decision support, and resource management, developed using Python and FastAPI.

## Project Overview

The **Precision Farming Management System (PFMS)** is a RESTful API designed to support agricultural monitoring and resource management.

The system provides functionality for:

- Agricultural field management
- Sensor data collection and validation
- Soil moisture monitoring
- Irrigation decision support
- Fertilizer inventory management
- Automated API testing
- Boundary and negative testing
- Defect identification and documentation

The project was developed as part of a **Software Engineering testing assignment**, with emphasis on REST API development, software testing, validation, test automation, and software quality.

---

## Technologies Used

- **Python**
- **FastAPI**
- **SQLAlchemy**
- **SQLite**
- **Pydantic**
- **Pytest**
- **HTTPX**
- **Jupyter Notebook / Google Colab**

---

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
├── defect_log.txt
├── phase3_test_report.txt
├── requirements.txt
├── README.md
├── __init__.py
└── PFMS_Project_Development.ipynb
```

---

## Main Features

### 1. Field Management

The system supports creation and retrieval of agricultural field information.

Each field contains:

- Field ID
- Field name
- Location
- Crop type

### 2. Sensor Monitoring

The API stores simulated agricultural sensor readings including:

- Soil moisture
- Temperature
- Humidity
- Field ID
- Timestamp

Input validation is applied to ensure that sensor values remain within defined acceptable ranges.

### 3. Irrigation Recommendation

The system generates a rule-based irrigation recommendation using soil moisture values.

| Soil Moisture | Recommendation |
|---|---|
| Below 30% | Irrigation required |
| 30% – 60% | Monitor soil moisture |
| Above 60% | No irrigation required |

The recommendation can be generated directly from a soil moisture value or using an existing sensor reading.

### 4. Fertilizer Inventory

The system provides APIs for managing fertilizer inventory.

Each inventory item contains:

- Item name
- Category
- Quantity
- Unit

Validation is applied to prevent invalid quantities and incomplete inventory records.

### 5. Sample Data

The `seed_data.py` script inserts simulated sample data into the SQLite database for development and testing.

The sample data includes:

- Agricultural fields
- Sensor readings
- Fertilizer inventory

---

## API Endpoints

### General

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/` | Check API status |

### Fields

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/fields` | Create a field |
| `GET` | `/fields` | Retrieve all fields |
| `GET` | `/fields/{field_id}` | Retrieve a field by ID |

### Sensor Readings

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/sensor-readings` | Create a sensor reading |
| `GET` | `/sensor-readings` | Retrieve all sensor readings |
| `GET` | `/sensor-readings/{reading_id}` | Retrieve a reading by ID |
| `PUT` | `/sensor-readings/{reading_id}` | Update a sensor reading |
| `DELETE` | `/sensor-readings/{reading_id}` | Delete a sensor reading |
| `GET` | `/sensor-readings/{reading_id}/irrigation-recommendation` | Generate irrigation recommendation from a sensor reading |

### Irrigation

| Method | Endpoint | Purpose |
|---|---|---|
| `GET` | `/irrigation-recommendation/{soil_moisture}` | Generate irrigation recommendation from soil moisture |

### Inventory

| Method | Endpoint | Purpose |
|---|---|---|
| `POST` | `/inventory` | Add a fertilizer inventory item |
| `GET` | `/inventory` | Retrieve inventory items |

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/gayatri615/precision-farming-management-system.git
cd precision-farming-management-system
```

### 2. Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI development server from the repository root:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## Loading Sample Data

After starting the project setup, sample agricultural data can be inserted using:

```bash
python seed_data.py
```

The script creates sample records for fields, sensor readings, and fertilizer inventory.

---

## API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

Open:

```text
http://127.0.0.1:8000/docs
```

### ReDoc

The alternative API documentation is available at:

```text
http://127.0.0.1:8000/redoc
```

The Swagger interface can be used to send requests to the API and examine the responses.

---

## Testing

The project uses **pytest** for automated API testing.

Run the complete test suite from the repository root:

```bash
pytest -v
```

The Phase 3 test suite contains **34 automated test cases** covering:

- API availability
- Field creation and retrieval
- Missing field data
- Sensor reading creation
- Sensor reading retrieval
- Sensor reading updates
- Sensor reading deletion
- Invalid field references
- Invalid sensor IDs
- Soil moisture boundary values
- Invalid soil moisture values
- Humidity boundary values
- Invalid data types
- Irrigation recommendations
- Irrigation boundary conditions
- Invalid irrigation input
- Sensor-based irrigation recommendations
- Missing sensor readings
- Inventory creation
- Inventory retrieval
- Invalid inventory quantities
- Missing inventory fields

### Test Result

The Phase 3 automated test suite completed successfully:

```text
34 passed in 0.99s
```

The detailed test results are recorded in:

```text
phase3_test_report.txt
```

---

## Software Testing Approach

The project applies multiple software testing techniques.

### Functional Testing

Functional tests verify that each API endpoint performs its intended operation.

### Boundary Value Analysis

Boundary values are tested for input fields such as:

- Soil moisture: `0` and `100`
- Values below `0`
- Values above `100`
- Humidity: `0` and `100`

### Negative Testing

Invalid requests and failure scenarios are tested, including:

- Non-existent IDs
- Invalid field references
- Invalid numeric values
- Missing required fields
- Invalid data types

### Integration Testing

Sensor readings and irrigation recommendation functionality are tested together to verify the interaction between different parts of the application.

### Automated Testing

Pytest is used to automate the test suite and provide repeatable test execution.

---

## Defect Tracking

A defect log is maintained in:

```text
defect_log.txt
```

The defect log records issues identified during the testing process and their status.

During the Phase 3 testing cycle, no confirmed application defect remained unresolved after testing.

---

## Development Phases

### Phase 1 – Basic REST API

- FastAPI application setup
- SQLite database configuration
- Sensor reading model
- CRUD operations
- Basic API testing

### Phase 2 – System Expansion

- Field management
- Irrigation recommendation module
- Fertilizer inventory
- Additional validation
- Expanded API functionality

### Phase 3 – Software Testing

- Comprehensive pytest suite
- Boundary value testing
- Negative testing
- Failure scenario testing
- Test result documentation
- Defect tracking

### Phase 4 – Documentation and Packaging

- Requirements file
- README documentation
- API documentation
- Test reports
- GitHub project organization

---

## Development Notebook

The complete development and testing process is documented in:

```text
PFMS_Project_Development.ipynb
```

The notebook contains the implementation and testing steps carried out during development, including:

- Project setup
- Database configuration
- API implementation
- Manual API testing
- Automated pytest testing
- Boundary testing
- Negative testing
- Test result generation

---

## Software Engineering Practices Demonstrated

This project demonstrates the application of several Software Engineering concepts:

- Requirement-based test design
- Functional testing
- Boundary Value Analysis
- Negative testing
- Integration testing
- Automated testing
- Test documentation
- Defect tracking
- API validation
- Modular software design
- Version control using Git and GitHub
- Incremental development through project phases

---

## Future Improvements

Possible extensions to the system include:

- Authentication and authorization
- Role-based access control
- Weather API integration
- Real-time IoT sensor integration
- Migration from SQLite to PostgreSQL
- Web-based monitoring dashboard
- Advanced irrigation prediction using machine learning
- Docker-based deployment
- Cloud deployment

---

## Author

Developed as a Software Engineering project demonstrating REST API development, software testing, validation, automation, and software quality practices.
