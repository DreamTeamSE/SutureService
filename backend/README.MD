## Requirements

- Install Docker

## Setup Instructions

### Step 1: Build the Application

1. Ensure you are in the `dev-env` folder.
2. Run the following command in the terminal to build the application:
   ```sh
   docker build -t app .
   ```

### Step 2: Start the Servers

1. Navigate to the `dev-env` folder.
2. Run the following commands to start the servers:
   ```sh
   docker-compose down
   docker-compose up -d
   ```

### Step 3: Mocking the Arduino

Refer to the Arduino documentation to learn how to mock the Arduino.