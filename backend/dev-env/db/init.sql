-- Create Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for the users table
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- Create Metrics table
CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255),
    velocity_list DOUBLE PRECISION[],
    acceleration_list DOUBLE PRECISION[],
    top_velocity DOUBLE PRECISION,
    top_acceleration DOUBLE PRECISION,
    average_velocity DOUBLE PRECISION,
    average_acceleration DOUBLE PRECISION,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
