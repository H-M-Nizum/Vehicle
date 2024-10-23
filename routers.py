from fastapi import APIRouter, HTTPException
from models import Allocation, Vehicle
from schemas import VehicleSchema, ResponseModel, AllocationSchema, UpdateAllocationSchema
from db import vehicle_conn, allocation_conn 
from typing import List, Optional
from datetime import date, datetime
from bson import ObjectId

router = APIRouter()

@router.get('/')
async def home():
    return {'message' : "Welcome to Softwd Ltd vehicle allocation system for employees"}
#===================================================================================
# Create Vehicle With Driver
@router.post("/vehicles/create/", response_model=VehicleSchema)
async def create_vehicle(vehicle: VehicleSchema):
    vehicle_doc = vehicle.dict()
    # Check for existing vehicle
    existing_vehicle =  vehicle_conn.vehicle.find_one({
        "vehicle_id": vehicle.vehicle_id,
        "driver_id": vehicle.driver_id
    })
    if existing_vehicle:
        raise HTTPException(status_code=400, detail="Vehicle ID already exists.")
    # Create a new Vehicle with Driver
    result = vehicle_conn.vehicle.insert_one(vehicle_doc)
    return VehicleSchema(id=str(result.inserted_id), **vehicle_doc)

# Get All Vehicles
@router.get('/vehicles/', response_model=List[VehicleSchema])
async def find_all_vehicles():
    vehicles_cursor = vehicle_conn.vehicle.find()
    vehicles = [VehicleSchema(**vehicle) for vehicle in vehicles_cursor]
    return vehicles

# Get a Specific Vehicles
@router.get('/vehicles/{vehicle_id}', response_model=VehicleSchema)
async def get_vehicle(vehicle_id: str):
    vehicle = vehicle_conn.vehicle.find_one({"vehicle_id": vehicle_id})
    if vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found.")
    return VehicleSchema(**vehicle)

# Update a Specific Vehicles
@router.put('/vehicles/{vehicle_id}', response_model=VehicleSchema)
async def update_vehicle(vehicle_id: str, vehicle: VehicleSchema):
    vehicle_doc = vehicle.dict()
    # Check if the vehicle exists
    existing_vehicle = vehicle_conn.vehicle.find_one({"vehicle_id": vehicle_id})
    if not existing_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found.")
    # Update the vehicle in the database
    vehicle_conn.vehicle.update_one({"vehicle_id": vehicle_id}, {"$set": vehicle_doc})

    # Return the updated vehicle
    return VehicleSchema(**{**existing_vehicle, **vehicle_doc})

# Delete a specific Vehicles
@router.delete('/vehicles/{vehicle_id}', response_model=dict)
async def delete_vehicle(vehicle_id: str):
    # Check if the vehicle exists
    existing_vehicle = vehicle_conn.vehicle.find_one({"vehicle_id": vehicle_id})
    if not existing_vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found.")
    # Delete the vehicle from the database
    vehicle_conn.vehicle.delete_one({"vehicle_id": vehicle_id})

    # Return a success message
    return {"message": "Vehicle deleted successfully."}

#===================================================================================
# Create Allocation for a employee
@router.post("/allocations/", response_model=AllocationSchema)
async def allocate_vehicle(allocation: Allocation):
    allocation_doc = allocation.dict()
    
    # Convert allocation_date to datetime.datetime
    allocation_doc['allocation_date'] = datetime.combine(allocation.allocation_date, datetime.min.time())

    # Check for existing vehicle allocation
    existing_allocation = allocation_conn.allocation.find_one({
        "vehicle_id": allocation.vehicle_id,
        "allocation_date": allocation_doc['allocation_date']
    })
    
    # Check for existing employee allocation for vehicle
    employee_allocation = allocation_conn.allocation.find_one({
        "employee_id": allocation.employee_id,
        "allocation_date": allocation_doc['allocation_date']
    })
    
    # Check if the vehicle exists
    existing_vehicle = vehicle_conn.vehicle.find_one({
        "vehicle_id": allocation.vehicle_id
    })
    
    if existing_allocation:
        raise HTTPException(status_code=400, detail="Vehicle already allocated for this day.")
    
    if employee_allocation:
        raise HTTPException(status_code=401, detail="Employee already allocated vehicle for this day.")
    
    if not existing_vehicle:  # Fixed the logic to check if vehicle does not exist
        raise HTTPException(status_code=402, detail="This vehicle does not exist.")
       # Compare the allocation_date with the current datetime
    if allocation_doc['allocation_date'] <= datetime.now():
        raise HTTPException(status_code=403, detail="Allocation has already passed. You can't Create it.")
    
    # Insert the new allocation
    result = allocation_conn.allocation.insert_one(allocation_doc)
    # Create and return the AllocationSchema with the new id
    return AllocationSchema(id=str(result.inserted_id), **allocation_doc)  # Use original allocation for other fields

# Get All Allocations
@router.get('/allocations/', response_model=List[AllocationSchema])
async def find_all_allocations():
    allocations_cursor = allocation_conn.allocation.find()
    allocations = []
    
    for allocation in allocations_cursor:
        allocation['id'] = str(allocation['_id'])  # Add the id field
        allocations.append(AllocationSchema(**allocation))
    
    return allocations


# Get a specific Allocation using by id
@router.get('/allocations/{id}', response_model=AllocationSchema)
async def get_allocations(id: str):
    # Convert the string ID to ObjectId
    try:
        object_id = ObjectId(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    # Find the allocation by ObjectId
    allocation = allocation_conn.allocation.find_one({"_id": object_id})
    if allocation is None:
        raise HTTPException(status_code=404, detail="Allocation not found.")
    
    # Add the 'id' field to the allocation document for the response
    allocation['id'] = str(allocation['_id'])  
    return AllocationSchema(**allocation)

# Update a specific Allocations
@router.put('/allocations/{id}', response_model=AllocationSchema)
async def update_allocation(id: str, allocation: UpdateAllocationSchema):
    allocation_doc = allocation.dict(exclude_unset=True)  # Exclude fields not set by the user
    # Convert allocation_date to datetime if provided
    if 'allocation_date' in allocation_doc:
        allocation_doc['allocation_date'] = datetime.combine(allocation_doc['allocation_date'], datetime.min.time())

    try:
        object_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    # Check if the allocation exists
    existing_allocation = allocation_conn.allocation.find_one({"_id": object_id})
    if not existing_allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")
    # Compare the allocation_date with the current datetime
    if existing_allocation['allocation_date'] <= datetime.now():
        raise HTTPException(status_code=401, detail="Allocation has already passed. You can't modify it.")
    
    # Update the allocation in the database
    allocation_conn.allocation.update_one({"_id": object_id}, {"$set": allocation_doc})

    # Merge the existing allocation with the updated fields
    updated_allocation = {**existing_allocation, **allocation_doc}
    updated_allocation['id'] = str(updated_allocation['_id'])  

    # Return the updated allocation
    return AllocationSchema(**updated_allocation)

# Delete a Specific Allocations
@router.delete('/allocations/{id}', response_model=dict)
async def delete_allocation(id: str):
    try:
        object_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid ID format.")

    # Check if the allocation exists
    existing_allocation = allocation_conn.allocation.find_one({"_id": object_id})
    if not existing_allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")
    # Compare the allocation_date with the current datetime
    if existing_allocation['allocation_date'] <= datetime.now():
        raise HTTPException(status_code=401, detail="Allocation has already passed. You can't Delete it.")
    
    # Delete the allocation from the database
    allocation_conn.allocation.delete_one({"_id": object_id})
    return {"message": "Allocation deleted successfully."}



@router.get('/allocations_filters/', response_model=List[AllocationSchema])
async def filters_allocations(
    from_date: Optional[date] = None,
    to_date: Optional[date] = None,
    vehicle_id: Optional[str] = None,
    employee_id: Optional[str] = None
):
    query = {}
    
    # Add filters to the query
    if from_date:
        query['allocation_date'] = {"$gte": datetime.combine(from_date, datetime.min.time())}
    if to_date:
        query.setdefault('allocation_date', {})["$lte"] = datetime.combine(to_date, datetime.min.time())
    if vehicle_id:
        query['vehicle_id'] = vehicle_id
    if employee_id:
        query['employee_id'] = employee_id

    # Fetch data from the database
    allocations_cursor = allocation_conn.allocation.find(query)
    allocations = []
    for allocation in allocations_cursor:
        allocation['id'] = str(allocation['_id'])  
        allocations.append(AllocationSchema(**allocation))

    return allocations