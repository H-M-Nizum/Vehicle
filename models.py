from pydantic import BaseModel
from datetime import date


class Vehicle(BaseModel):
    vehicle_id: str
    driver_id: str

class Allocation(BaseModel):
    employee_id: str
    vehicle_id: str
    allocation_date: date
