-- 1. Create Users Table
CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE NOT NULL
);

-- 2. Create Drivers Table
-- TODO: Add columns for id, name, car_model, rating
CREATE TABLE Drivers (
    id SERIAL PRIMARY KEY,
    -- ...
);

-- 3. Create Rides Table
-- TODO: Add columns and Foreign Keys to Users and Drivers
CREATE TABLE Rides (
    id SERIAL PRIMARY KEY,
    -- user_id INT REFERENCES ...
    -- ...
);


-- QUERIES ------------------------------------------

-- Query 1: Find all rides taken by user with id = 1
-- SELECT ...

-- Query 2: Find all drivers with a rating > 4.5
-- SELECT ...

-- Query 3: (Bonus) Find the total money spent by user with id = 1
-- Hint: Use SUM(price)




