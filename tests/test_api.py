
from fastapi.testclient import TestClient
from PFMS.app.main import app

client = TestClient(app)


# Basic API checks
def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


# Field management tests
def test_create_field():
    response = client.post(
        "/fields",
        json={
            "name": "Phase 3 Test Field",
            "location": "Chennai",
            "crop_type": "Tomato"
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Phase 3 Test Field"


def test_get_fields():
    response = client.get("/fields")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_field():
    response = client.get("/fields/999999")
    assert response.status_code == 404


def test_create_field_with_missing_data():
    response = client.post(
        "/fields",
        json={
            "name": "Incomplete Field"
        }
    )
    assert response.status_code == 422


# Sensor reading tests
def test_create_sensor_reading():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": 45,
            "temperature": 30,
            "humidity": 65
        }
    )
    assert response.status_code == 200
    assert response.json()["soil_moisture"] == 45


def test_sensor_reading_invalid_field():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 999999,
            "soil_moisture": 45,
            "temperature": 30,
            "humidity": 65
        }
    )
    assert response.status_code == 404


def test_get_sensor_readings():
    response = client.get("/sensor-readings")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_nonexistent_sensor_reading():
    response = client.get("/sensor-readings/999999")
    assert response.status_code == 404


def test_update_sensor_reading():
    response = client.put(
        "/sensor-readings/1",
        json={
            "field_id": 1,
            "soil_moisture": 52,
            "temperature": 29,
            "humidity": 70
        }
    )
    assert response.status_code == 200
    assert response.json()["soil_moisture"] == 52


def test_update_nonexistent_sensor_reading():
    response = client.put(
        "/sensor-readings/999999",
        json={
            "field_id": 1,
            "soil_moisture": 52,
            "temperature": 29,
            "humidity": 70
        }
    )
    assert response.status_code == 404


def test_delete_nonexistent_sensor_reading():
    response = client.delete("/sensor-readings/999999")
    assert response.status_code == 404


# Soil moisture boundary and validation tests
def test_soil_moisture_lower_boundary():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": 0,
            "temperature": 30,
            "humidity": 60
        }
    )
    assert response.status_code == 200


def test_soil_moisture_upper_boundary():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": 100,
            "temperature": 30,
            "humidity": 60
        }
    )
    assert response.status_code == 200


def test_soil_moisture_above_upper_boundary():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": 100.1,
            "temperature": 30,
            "humidity": 60
        }
    )
    assert response.status_code == 422


def test_soil_moisture_below_lower_boundary():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": -0.1,
            "temperature": 30,
            "humidity": 60
        }
    )
    assert response.status_code == 422


def test_humidity_above_upper_boundary():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": 50,
            "temperature": 30,
            "humidity": 100.1
        }
    )
    assert response.status_code == 422


def test_humidity_below_lower_boundary():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": 50,
            "temperature": 30,
            "humidity": -0.1
        }
    )
    assert response.status_code == 422


def test_invalid_sensor_data_type():
    response = client.post(
        "/sensor-readings",
        json={
            "field_id": 1,
            "soil_moisture": "not-a-number",
            "temperature": 30,
            "humidity": 60
        }
    )
    assert response.status_code == 422


# Irrigation decision tests
def test_irrigation_required():
    response = client.get("/irrigation-recommendation/25")
    assert response.status_code == 200
    assert response.json()["irrigation_required"] is True


def test_irrigation_monitoring():
    response = client.get("/irrigation-recommendation/45")
    assert response.status_code == 200
    assert response.json()["irrigation_required"] is False
    assert response.json()["recommendation"] == "Monitor soil moisture"


def test_irrigation_not_required():
    response = client.get("/irrigation-recommendation/75")
    assert response.status_code == 200
    assert response.json()["irrigation_required"] is False
    assert response.json()["recommendation"] == "No irrigation required"


def test_irrigation_lower_boundary():
    response = client.get("/irrigation-recommendation/0")
    assert response.status_code == 200
    assert response.json()["irrigation_required"] is True


def test_irrigation_upper_boundary():
    response = client.get("/irrigation-recommendation/100")
    assert response.status_code == 200
    assert response.json()["irrigation_required"] is False


def test_invalid_irrigation_value():
    response = client.get("/irrigation-recommendation/101")
    assert response.status_code == 400


def test_negative_irrigation_value():
    response = client.get("/irrigation-recommendation/-1")
    assert response.status_code == 400


def test_sensor_to_irrigation_recommendation():
    response = client.get("/sensor-readings/1/irrigation-recommendation")
    assert response.status_code == 200
    assert "recommendation" in response.json()


def test_sensor_irrigation_missing_reading():
    response = client.get(
        "/sensor-readings/999999/irrigation-recommendation"
    )
    assert response.status_code == 404


# Inventory tests
def test_create_inventory_item():
    response = client.post(
        "/inventory",
        json={
            "name": "Phase 3 Test Fertilizer",
            "category": "Fertilizer",
            "quantity": 25,
            "unit": "kg"
        }
    )
    assert response.status_code == 201
    assert response.json()["quantity"] == 25


def test_get_inventory():
    response = client.get("/inventory")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_invalid_inventory_quantity():
    response = client.post(
        "/inventory",
        json={
            "name": "Invalid Fertilizer",
            "category": "Fertilizer",
            "quantity": -5,
            "unit": "kg"
        }
    )
    assert response.status_code == 422


def test_inventory_missing_name():
    response = client.post(
        "/inventory",
        json={
            "category": "Fertilizer",
            "quantity": 10,
            "unit": "kg"
        }
    )
    assert response.status_code == 422


# Test invalid HTTP input for an endpoint that expects a number
def test_invalid_field_id_format():
    response = client.get("/fields/not-a-number")
    assert response.status_code == 422


def test_invalid_sensor_id_format():
    response = client.get("/sensor-readings/not-a-number")
    assert response.status_code == 422
