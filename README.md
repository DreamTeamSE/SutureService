# SutureService Installation Guide

Follow these steps to install and set up SutureService:

## Clone the Repository

1. **Clone the repository:**
    Use the following command to clone the SutureService repository:
    ```sh
    git clone https://github.com/DreamTeamSE/SutureService.git
    ```

## Frontend Setup

1. **Navigate to the frontend directory:**
    ```sh
    cd frontend
    ```

2. **Install the dependencies:**
    ```sh
    npm install
    ```

3. **Start the development server:**
    ```sh
    npm run dev
    ```

You have successfully set up the frontend for SutureService!

You can now open the web app with the local address provided in the terminal!

## Arduino Setup

1. **Set Up Virtual Environment:**
    To set up the virtual environment, use the following commands:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

2. **Install Dependencies:**
    To install the required dependencies, use the command:
    ```sh
    pip install -r requirements.txt
    ```

3. **Start the Application:**
    To start the application, use the command:
    ```sh
    python main.py
    ```

You have successfully set up the Arduino part of SutureService!

You can now run the application with the command provided above!

## Backend Setup

**Important:** Ensure that the Arduino mocks are running before setting up the backend. This is necessary for the backend to function correctly.

1. **Navigate to the backend directory:**
    Ensure you are in the `backend` folder of the project.

2. **Build the Docker image:**
    Use the following command to build the Docker image:
    ```sh
    docker build -t app .
    ```

3. **Deploy the Application with Docker Compose:**
    Navigate to the `dev-env` folder where the `docker-compose.yml` file is located and start the services:
    ```sh
    (cd dev-env && docker compose up -d)
    ```

4. **View API Documentation:**
   To learn how to use the API, navigate to the Swagger API Documentation at:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

The application will be available on the configured ports as specified in the `docker-compose.yml` file.

You have successfully set up the backend for SutureService!