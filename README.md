# SutureService Installation Guide

Follow these steps to install and set up SutureService:

## Clone the Repository

1. **Clone the repository:**
    ```sh
    git clone https://github.com/DreamTeamSE/SutureService.git
    ```

## Frontend Setup

1. **Navigate to the frontend directory:**
    ```sh
    cd frontend
    ```

2. **Install dependencies:**
    ```sh
    npm install
    ```

3. **Start the development server:**
    ```sh
    npm run dev
    ```

You have successfully set up the frontend for SutureService! You can now open the web app with the local address provided in the terminal.

## Arduino Setup

1. **Navigate to the arduino directory:**
    ```sh
    cd arduino
    ```

2. **Set up virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Start the application:**
    ```sh
    python main.py
    ```

You have successfully set up the Arduino part of SutureService! You can now run the application with the command provided above.

## Backend Setup

**Important:** Ensure that the Arduino mocks are running before setting up the backend. This is necessary for the backend to function correctly.

1. **Navigate to the backend directory:**
    ```sh
    cd backend
    ```

2. **Build the Docker image:**
    ```sh
    docker build -t app .
    ```

3. **Deploy the application with Docker Compose:**
    ```sh
    (cd dev-env && docker compose up -d)
    ```

4. **View API documentation:**
    Navigate to the Swagger API Documentation at:
    [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

The application will be available on the configured ports as specified in the `docker-compose.yml` file. You have successfully set up the backend for SutureService!