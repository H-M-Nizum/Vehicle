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
      "make": "string",
      "model": "string",
      "year": "integer"
  }
