# Quiz Application

## Setup

1. Create a virtual environment:
    ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    python backend/utils/setup_db.py
    ```

## Running the Application

1. Start the Flask application:
    ```bash
    python backend/api/main.py
    ```

2. Access the API documentation at:
    ```
    http://0.0.0.0:8000/apidocs/
    ```

## API Endpoints

- `GET /quiz`: Fetches the quiz questions and options.
- `POST /quiz/submit`: Submits the quiz answers and returns the score along with the correctness of each answer.
- `POST /quiz/restart`: Restarts the quiz.
