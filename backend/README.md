# Backend Application

This repository contains the codebase for the backend of our application.

## Technologies Used
- Python
- FastAPI
- Gunicorn
- Uvicorn
- Docker

## Installation
1. Clone this repository.
2. Navigate to the backend directory.
3. Install dependencies using `pip install -r requirements.txt`.

## Usage
- To run the application locally:
    ```lua
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```
- To run the application using Docker:
    ```arduino
    docker build -t backend-image .
    docker run -d -p 8000:8000 backend-image
    ```

## API Documentation
The API documentation can be found at [http://localhost:8000/docs](http://localhost:8000/docs).
