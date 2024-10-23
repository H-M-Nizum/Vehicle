from typing import Optional
from pydantic import BaseModel, Field
from datetime import date

class VehicleSchema(BaseModel):
    vehicle_id: str = Field(...)
    driver_id: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "vehicle_id": "V123",
                "driver_id": "D456",
            }
        }

class UpdateVehicleModel(BaseModel):
    vehicle_id: Optional[str]
    driver_id: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "vehicle_id": "V123",
                "driver_id": "D789",
            }
        }

class AllocationSchema(BaseModel):
    id: str = Field(..., description="The unique identifier for the allocation.")
    employee_id: str = Field(...)
    vehicle_id: str = Field(...)
    allocation_date: date = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "id": "671889f9254f20bc1dacbe31",
                "employee_id": "E123",
                "vehicle_id": "V123",
                "allocation_date": "2024-10-22",
            }
        }

class UpdateAllocationSchema(BaseModel):
    employee_id: Optional[str]
    vehicle_id: Optional[str]
    allocation_date: Optional[date]

    class Config:
        schema_extra = {
            "example": {
                "employee_id": "E123",
                "vehicle_id": "V124",
                "allocation_date": "2024-10-23",
            }
        }

def ResponseModel(data, message, code):
    return {
        "data": [data],
        "code": code,
        "msg": message,
    }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
