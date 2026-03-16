# Homework 4: Design a Ride-Sharing App

**Objective**: Design a relational database schema for a simplified version of Uber/Lyft.

## Instructions
1. Open `schema_starter.sql`.
2. We need to store data for:
   - **Users** (riders)
   - **Drivers**
   - **Rides** (links a User and a Driver)
3. **Tasks**:
   - Complete the `CREATE TABLE` statements for `Drivers` and `Rides`.
   - Think about relationships: A Ride has ONE User and ONE Driver.
   - Write the SQL queries requested at the bottom of the file.
4. You can test your SQL in [DB Fiddle](https://www.db-fiddle.com/) (select PostgreSQL).

## Schema Requirements
- **Users**: id, name, email.
- **Drivers**: id, name, car_model, rating.
- **Rides**: id, user_id, driver_id, start_location, end_location, price, status (e.g., 'completed').




