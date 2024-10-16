# Alibaba Database Simulation with SQL

## Project Overview
This project simulates the core database of Alibaba, a major online travel platform in Iran. It focuses on modeling the key functionalities of the website such as booking tickets for flights, trains, buses, and hotels. Using SQL, I implemented the database schema to manage the relationships between users, services, transactions, and other related data.

## Database Design
The database is structured around several key entities that represent the core features of Alibaba's operations. These entities are connected through relational tables, with foreign keys ensuring the integrity of data.

### Entities
- **Users:** Represents the customers registered on the platform, with details such as name, email, contact information, and transaction history.
- **Bookings:** Captures all booking details, including the type of service (flight, bus, train, or hotel), booking dates, and user information.
- **Services:** Contains the available services such as flight schedules, bus routes, train schedules, and hotel availability.
- **Payments:** Manages the payment information for each booking, including payment method, status, and transaction details.
- **Reviews:** Stores user feedback and ratings for services booked through the platform.

### Relationships
- **User-Booking:** One-to-many relationship, where one user can make multiple bookings.
- **Booking-Service:** One-to-one relationship linking each booking to the specific service being used.
- **Booking-Payment:** One-to-one relationship between bookings and payments.
- **User-Review:** One-to-many relationship where users can leave multiple reviews.

## Key Features
- **Data Integrity:** All relationships are enforced through foreign keys to maintain data consistency.
- **Booking Management:** Handles user bookings for various services offered on the Alibaba platform.
- **Transaction Handling:** Manages payments and ensures the correct status for each transaction.
- **Service Availability:** Provides real-time availability of services, ensuring bookings cannot be made for unavailable services.

## SQL Implementation
The SQL scripts provided in this repository cover:
- Creating the database schema with all necessary tables and relationships.
- Populating the database with sample data to simulate real-world use cases.
- Queries to handle common operations such as creating new bookings, processing payments, and retrieving service availability.
