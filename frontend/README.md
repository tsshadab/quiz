# Frontend Application

This repository contains the codebase for the frontend of our application.

## Technologies Used
- HTML
- CSS
- JavaScript
- Docker

## Installation
1. Clone this repository.
2. Navigate to the frontend directory.
3. Install dependencies using `pip install -r requirements.txt`.

## Usage
- To run the application locally:
    ```lua
    uvicorn main:app --host 0.0.0.0 --port 8080
    ```
- To run the application using Docker:
    ```arduino
    docker build -t frontend-image .
    docker run -d -p 8080:8080 frontend-image
    ```

## Accessing the Application
The application can be accessed at [http://localhost:8080](http://localhost:8080).
