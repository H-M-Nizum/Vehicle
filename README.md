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



## Getting Started
  #### Prerequisites
    - Python: 3.7 or higher
    - MongoDB: Local or cloud instance
    - pip: Python package installer
  #### Installation
  **1. Clone the repository:**  
  
    
      git clone https://github.com/yourusername/vehicle-allocation-system.git
      cd vehicle-allocation-system

      
  **2. Create a virtual environment (optional):**
  
     
      python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  
      
  **3. Install required packages:**
  
      
      pip install -r requirements.txt
      
      
  **4. Configure your MongoDB connection in db.py or set environment variables accordingly.(optional for check task)**

### Running the Application
  To run the application locally:
  ```
  uvicorn main:app --reload
  ```
### Test the Application
  To run the test script locally
  ```
  pytest test_routes.py
  ```
* Access the API at ```http://127.0.0.1:8000```
* Access the swagger documentation at ```http://127.0.0.1:8000/docs```

## Deployment
  #### Vercel
  - Push your code to a GitHub repository.
  - Sign in to Vercel and create a new project.
  - Connect your GitHub repository to Vercel.
  - Set any required environment variables in the Vercel dashboard.
  - Deploy your project.
## Maintenance
  - Monitor logs and performance metrics regularly.
  - Update dependencies to maintain security and performance.
  - Consider implementing automated tests to ensure reliability.


## Acknowledgments
  - FastAPI: ```https://fastapi.tiangolo.com/```
  - MongoDB: ```https://www.mongodb.com/```
