## Requirements

- Install Docker
- Install Docker Compose
- Install Python 3
- Install pip

## Setup Instructions

### Step 1: Build the Application

1. Ensure you are in the `backend` folder of the project.
2. Build the Docker image with the following command:
   ```sh
   docker build -t app .
   ```

### Step 2: Deploy the Application with Docker Compose

1. Navigate to the `dev-env` folder where the `docker-compose.yml` file is located.
2. Start the services using Docker Compose:
   ```sh
   (cd dev-env && docker compose up -d)
   ```
3. The application will be available on the configured ports as specified in the `docker-compose.yml` file.

### Step 3: Mocking the Arduino

Refer to the Arduino documentation to learn how to mock the Arduino.

### Additional Information

- The `docker-compose.yml` file is located in the `dev-env` folder and is used to set up the necessary services.
- The `requirements.txt` file lists all the dependencies required for the application.