# Vehicle Allocation System

## Overview
The Vehicle Allocation System is a web API designed to manage vehicle allocations for employees in a company. Built using FastAPI and MongoDB, this system allows for seamless handling of vehicle information and their allocations, ensuring efficient resource management.

## Features
- **Vehicle Management**: Create, read, update, and delete vehicle records.
- **Allocation Management**: Allocate vehicles to employees, read, update, and delete and manage allocation records.
- **Filters**: Retrieve allocations based on various criteria such as dates and IDs.
- **Error Handling**: Comprehensive error responses for various API operations.

## API Endpoints

### Home
- **GET /**  
  Returns a welcome message.

### Vehicle Management
- **POST /vehicles/create/**  
  Create a new vehicle with a driver.  
  **Request Body**:
  ```json
  {
      "vehicle_id": "string",
      "driver_id": "string",
  }
- **GET /vehicles/**  
  Retrieve all vehicles.
- **GET /vehicles/{vehicle_id}**  
  Retrieve a specific vehicle by its ID.
- **PUT /vehicles/{vehicle_id}**  
  Update a specific vehicle.
  **Request Body**:
  ```json
  {
      "vehicle_id": "string",
      "driver_id": "string",
  }
- **DELETE /vehicles/{vehicle_id}**  
  Delete a specific vehicle by its ID.
  
### Allocation Management
- **POST /allocations/**  
  Create a new allocation with a employee.  
  **Request Body**:
  ```json
  {
    "vehicle_id": "string",
    "employee_id": "string",
    "allocation_date": "YYYY-MM-DD"
  }
- **GET /allocations/**  
  Retrieve all allocation .
- **GET /allocations/{id}**  
  Retrieve a specific allocation  by its ID.
- **PUT /allocations/{id}**  
  Update a specific allocation .
  **Request Body**:
  ```json
  {
      "vehicle_id": "string",
      "employee_id": "string",
      "allocation_date": "YYYY-MM-DD"
  }
- **DELETE /allocations/{id}**  
  Delete a specific allocation  by its ID.
  
