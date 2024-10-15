CREATE DATABASE IF NOT EXISTS AliBaba;

USE AliBaba;

DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS person;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS passenger;
DROP TABLE IF EXISTS bank_info;
DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS train_trip;
DROP TABLE IF EXISTS flight;
DROP TABLE IF EXISTS bus_trip;
DROP TABLE IF EXISTS cabin;
DROP TABLE IF EXISTS coach_train_ticket;
DROP TABLE IF EXISTS compartment_train_trip;	
DROP TABLE IF EXISTS coach_train_trip;			
DROP TABLE IF EXISTS hotel_comments;
DROP TABLE IF EXISTS discount;
DROP TABLE IF EXISTS protector;
DROP TABLE IF EXISTS airplane;
DROP TABLE IF EXISTS bus;
DROP TABLE IF EXISTS compartment_train;
DROP TABLE IF EXISTS coach_train;
DROP TABLE IF EXISTS hotel_reservation;
DROP TABLE IF EXISTS hotel_room;
DROP TABLE IF EXISTS hotel;
DROP TABLE IF EXISTS bus_ticket;
DROP TABLE IF EXISTS domestic_flight_ticket;
DROP TABLE IF EXISTS international_flight_ticket;
DROP TABLE IF EXISTS compartment_train_ticket;



CREATE TABLE address (
    address_id INT PRIMARY KEY,
    country VARCHAR(50),
    city VARCHAR(50),
    main_street VARCHAR(100),
    secondary_street VARCHAR(100),
    alley VARCHAR(50),
    postal_code VARCHAR(20),
    unit VARCHAR(20)
);


CREATE TABLE person (
    person_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    national_code VARCHAR(20),
    birth_date DATE,
    gender VARCHAR(10),
    address_id INT,
    FOREIGN KEY (address_id) REFERENCES address(address_id)
); 


CREATE TABLE users (
    user_id INT PRIMARY KEY,
    person_id INT,
    credit INT,
    user_password VARCHAR(100),
    username VARCHAR(50),
    score INT,
    email VARCHAR(100),
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);


CREATE TABLE passenger (
    passenger_id INTEGER PRIMARY KEY,
    person_id INT,
    user_id INT,
    FOREIGN KEY (person_id) REFERENCES person(person_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE bank_info (
    bank_info_id INT PRIMARY KEY,
    shaba_number VARCHAR(30),
    account_number VARCHAR(30),
    card_number VARCHAR(16),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE transactions (
    transaction_id INT PRIMARY KEY,
    transaction_date DATE,
    amount INT,
    transaction_type VARCHAR(20),
    transaction_time TIME,
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE trip (
    trip_id INT PRIMARY KEY,
    transportation_type VARCHAR(50),
    transportation_company VARCHAR(100),
    capacity INT,
    origin VARCHAR(100),
    destination VARCHAR(100),
    departure_date DATE,
    departure_time TIME,
    arrival_time TIME,
    amenity VARCHAR(255)
);


/*train*/

CREATE TABLE train_trip (
   train_trip_number varchar(15),
   trip_id int,                   
   stopping_stations varchar(200),
   image varchar(100),
   adult_price int,
   child_price int,
   PRIMARY KEY (train_trip_number),
   FOREIGN KEY (trip_id) REFERENCES trip(trip_id)
);


CREATE TABLE compartment_train(
    compartment_train_number INTEGER PRIMARY KEY,
    train_model TEXT NOT NULL,
    number_of_wagons INTEGER NOT NULL,
    number_of_train_compartments INTEGER NOT NULL,
    number_of_beds_in_each_compartment INTEGER NOT NULL
);


CREATE TABLE compartment_train_trip (
    compartment_train_trip_id int,
    train_trip_number varchar(15),/*foreign key*/
    compartment_train_number int, /*foreign key*/
    PRIMARY KEY (compartment_train_trip_id),
    FOREIGN KEY (train_trip_number) REFERENCES train_trip(train_trip_number),
    FOREIGN KEY (compartment_train_number) REFERENCES compartment_train(compartment_train_number)
);


CREATE TABLE compartment_train_ticket (
    compartment_ticket_number varchar(15),
    passenger_id int,
    ticket_number int,
    wagon_number int,
    seat_number int,
    compartment_number int,
    compartment_train_trip_id int,     /*foreign key*/
    PRIMARY KEY (compartment_ticket_number),
    FOREIGN KEY (compartment_train_trip_id) REFERENCES compartment_train_trip(compartment_train_trip_id),
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id)
);


CREATE TABLE coach_train (
    coach_train_number INTEGER PRIMARY KEY,
    train_model TEXT NOT NULL,
    number_of_wagons INTEGER NOT NULL,
    number_of_seats_in_each_carriage INTEGER NOT NULL,
    number_of_all_seats INTEGER NOT NULL
);


CREATE TABLE coach_train_trip (
    coach_train_trip_id int,
    train_trip_number varchar(15),
    coach_train_number int,        
    PRIMARY KEY (coach_train_trip_id),
    FOREIGN KEY (train_trip_number) REFERENCES train_trip(train_trip_number),
    FOREIGN KEY (coach_train_number) REFERENCES coach_train(coach_train_number)
);


CREATE TABLE coach_train_ticket (
    coach_ticket_number varchar(15),
    passenger_id int,            
    ticket_number int,
    wagon_number int,
    seat int,
    coach_train_trip_id int,     
    PRIMARY KEY (coach_ticket_number),
    FOREIGN KEY (coach_train_trip_id) REFERENCES coach_train_trip(coach_train_trip_id),
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id)
);


/*airplane*/

CREATE TABLE airplane (
    airplane_id INTEGER PRIMARY KEY,
    airplane_model varchar(50),
    number_of_airplane_seats INTEGER
);


CREATE TABLE flight_trip (
    flight_number varchar(15),
    trip_id int,                    /*foreign key*/
    terminal varchar(50),
    airport varchar(50),
    flight_duration time,
    airplane_id int,            /*foreign key*/
    PRIMARY KEY (flight_number),
    FOREIGN KEY (trip_id) REFERENCES trip(trip_id),
    FOREIGN KEY (airplane_id) REFERENCES airplane(airplane_id)
);


CREATE TABLE cabin (
   class_id int,
   class_type varchar(10),
   flight_number varchar(15),    /*foreign key*/
   baggage_allowance int,
   adult_price int,
   child_price int,
   PRIMARY KEY (class_id),
   FOREIGN KEY (flight_number) REFERENCES flight_trip(flight_number)
);


CREATE TABLE international_flight_ticket (
    international_flight_ticket_id INTEGER PRIMARY KEY,
    passenger_id INTEGER,                        
    ticket_series INTEGER,
    passport_num  INTEGER,
    passport_expiration_date DATE,
    ad_birthdate DATE,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES cabin(class_id),
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id)
);


CREATE TABLE domestic_flight_ticket (
    domestic_flight_ticket_id INTEGER PRIMARY KEY,
    passenger_id INTEGER,                        
    ticket_series INTEGER,
    class_id INTEGER,
    FOREIGN KEY (class_id) REFERENCES cabin(class_id),
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id)
);


/*bus*/

CREATE TABLE bus(
    bus_id INTEGER PRIMARY KEY,
    bus_model VARCHAR(50),
    number_of_bus_seats INTEGER,
    bus_license_plate_number VARCHAR(20) 
);

CREATE TABLE bus_trip (
    bus_trip_number varchar(15),
    trip_id int,                    /*foreign key*/
    terminal varchar(50),
    price int,
    bus_id int,                /*foreign key*/
    PRIMARY KEY (bus_trip_number),
    FOREIGN KEY (trip_id) REFERENCES trip(trip_id),
    FOREIGN KEY (bus_id) REFERENCES bus(bus_id)
);

CREATE TABLE bus_ticket (
    bus_ticket_num VARCHAR(20) PRIMARY KEY,              
    passenger_id INTEGER,                        
    ticket_series INTEGER,
    seat INTEGER,
    bus_trip_number varchar(15),
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id),
    FOREIGN KEY (bus_trip_number) REFERENCES bus_trip(bus_trip_number)
);


/*hotel*/

CREATE TABLE hotel (
    hotel_id INTEGER PRIMARY KEY,
    hotel_name TEXT,
    hotel_stars INTEGER,
    telephone VARCHAR(20),
    address_id INTEGER, 
    arrival_time TIME,   
    departure_time TIME,
    hotel_facilities TEXT,
    hotel_image TEXT,
    capcity INTEGER,
    FOREIGN KEY (address_id) REFERENCES address(address_id)
);


CREATE TABLE hotel_room (
    room_id INTEGER PRIMARY KEY,
    price INTEGER,
    beds_num INTEGER,
    room_type TEXT,
    hotel_id INTEGER,     
    FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
);


CREATE TABLE hotel_reservation (
    reserv_id INTEGER PRIMARY KEY,
    passenger_id INTEGER,
    arrival_time TIME,   
    departure_time TIME,
    room_id INTEGER,
    reserv_date DATE,
    hotel_id INTEGER,          
    FOREIGN KEY (passenger_id) REFERENCES passenger(passenger_id),
    FOREIGN KEY (room_id) REFERENCES hotel_room( room_id),
    FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
);


CREATE TABLE hotel_comment (
    comment_id INTEGER PRIMARY KEY,
    user_id INTEGER ,
    comment_registration_time TIME ,
    comment_registration_date DATE ,
    score INTEGER ,
    hotel_id INTEGER ,
    comment_text TEXT,
    FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


CREATE TABLE protector (
    protector_id INTEGER PRIMARY KEY,
    person_id INTEGER ,
    email TEXT ,
    FOREIGN KEY (person_id) REFERENCES person(person_id)
);


CREATE TABLE discount (
    discount_id INTEGER PRIMARY KEY,
    amount_of_discount INTEGER NOT NULL,
    expiration_date DATE NOT NULL,
    minimum_purchase_amount INTEGER NOT NULL,
    type_of_trip TEXT NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);



