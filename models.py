from pydantic import BaseModel
from datetime import date
from typing import Optional

class Vehicle(BaseModel):
    vehicle_id: str
    driver_id: str

class Allocation(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: date
