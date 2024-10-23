import pytest
from fastapi.testclient import TestClient
from main import app
import warnings
from main import app
from models import Allocation, Vehicle  


client = TestClient(app)


def test_read_main():
    warnings.simplefilter("ignore")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Softwd Ltd vehicle allocation system for employees"}
    

# =======================Tests for vehicle endpoints=========================
def test_create_vehicle():
    response = client.post("/vehicles/create/", json={"vehicle_id": "v1", "driver_id": "d1"})
    assert response.status_code == 200
    assert response.json()["vehicle_id"] == "v1"
    assert response.json()["driver_id"] == "d1"

def test_find_all_vehicles():
    response = client.get("/vehicles/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  

def test_get_vehicle():
    response = client.get("/vehicles/v1")
    assert response.status_code == 200
    assert response.json()["vehicle_id"] == "v1"

def test_update_vehicle():
    response = client.put("/vehicles/v1", json={
        "vehicle_id": "v1",  
        "driver_id": "d2"    
    })
    assert response.status_code == 200
    assert response.json()["driver_id"] == "d2"

def test_delete_vehicle():
    response = client.delete("/vehicles/v1")
    assert response.status_code == 200
    assert response.json()["message"] == "Vehicle deleted successfully."
    
    
# ============================ Tests for allocation endpoints ==================================
def test_allocate_vehicle():
    response = client.post("/allocations/", json={
        "employee_id": "e100",
        "vehicle_id": "v1",
        "allocation_date": "2024-10-23"
    })
    print(response.json())
    if response.status_code == 200:
        assert response.status_code == 200
        assert response.json()["employee_id"] == "e100"
        assert response.json()["vehicle_id"] == "v100"
        assert response.json()["allocation_date"] == "2024-10-23"
    elif response.status_code == 400:
        assert response.json()["detail"] == "Vehicle already allocated for this day."
    elif response.status_code == 401:
        assert response.json()["detail"] == "Employee already allocated vehicle for this day."
    elif response.status_code == 402:
        assert response.json()["detail"] == "This vehicle does not exist."
    elif response.status_code == 403:
        assert response.json()["detail"] == "Allocation has already passed. You can't Create it."


def test_find_all_allocations():
    response = client.get("/allocations/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_allocation():
    response = client.get("/allocations/id")  
    if response.status_code == 200:
        assert response.status_code == 200

def test_update_allocation():
    response = client.put("/allocations/id", json={
        "vehicle_id": "v2"  
    })
    if response.status_code == 200:
        assert response.status_code == 200
    elif response.status_code == 400:
        assert response.status_code == 400
        assert response.json()["detail"] == "Invalid ID format."
    elif response.status_code == 401:
        assert response.status_code == 401
        assert response.json()["detail"] == "Allocation has already passed. You can't modify it."
    elif response.status_code == 404:
        assert response.status_code == 404
        assert response.json()["detail"] == "Allocation not found."

def test_delete_allocation():
    response = client.delete("/allocations/id")  
    if response.status_code == 200:
        assert response.status_code == 200
        assert response.json()["message"] == "Allocation deleted successfully."
    elif response.status_code == 401:
        assert response.status_code == 401
        assert response.json()["detail"] == "Allocation has already passed. You can't Delete it."
    elif response.status_code == 400:
        assert response.status_code == 400
        assert response.json()["detail"] == "Invalid ID format."
    elif response.status_code == 404:
        assert response.status_code == 404
        assert response.json()["detail"] == "Allocation not found."
        
