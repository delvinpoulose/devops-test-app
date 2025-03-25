-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hostlogs;

-- Use the database
USE hostlogs;

-- Create the request_log table
CREATE TABLE IF NOT EXISTS request_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(45),
    hostname VARCHAR(255),
    timestamp DATETIME
);

