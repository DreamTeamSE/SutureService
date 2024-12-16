-- Create Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for the users table
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- Create Metrics table
CREATE TABLE metrics (
    email VARCHAR(255) NOT NULL,              
    velocity_list TEXT NOT NULL,            
    acceleration_list TEXT NOT NULL,          
    top_velocity FLOAT NOT NULL,              
    top_acceleration FLOAT NOT NULL,          
    average_velocity FLOAT NOT NULL,          
    average_acceleration FLOAT NOT NULL,      
    insertion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (email),
    FOREIGN KEY (email) REFERENCES users(email) ON DELETE CASCADE
);
