-- Create a table to store users
CREATE TABLE Users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    hash VARCHAR(100) NOT NULL,
    salt VARCHAR(50) NOT NULL
);
