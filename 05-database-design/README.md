# Lesson 4: Database Design

**Date:** 13th March 2026

## Overview

Every app needs to store data. How you structure that data determines if your app is fast and scalable or slow and buggy.

## Agenda

1. **Relational Model (SQL)**
   - **Tables**: Like Excel sheets (Users, Products).
   - **Columns**: Attributes (Name, Age, Email).
   - **Rows**: Individual records.

2. **Keys & Relationships**
   - **Primary Key (PK)**: Unique ID for a row (e.g., `user_id`).
   - **Foreign Key (FK)**: A link to another table (e.g., `order.user_id` points to `users.id`).
   - **Types**: One-to-One, One-to-Many, Many-to-Many.

3. **Normalization**
   - The art of not repeating yourself.
   - Example: Don't store the user's address in every order they make. Store it in the User table and link to it.

4. **Basic SQL**
   - `SELECT * FROM Users WHERE age > 18;`
   - `INSERT INTO Users (name) VALUES ('Alice');`
   - `JOIN`: Combining tables.

## Class Activity

We will whiteboard the database schema for a simple Application
