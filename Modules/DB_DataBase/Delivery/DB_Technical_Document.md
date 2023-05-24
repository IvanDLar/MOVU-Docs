# Database Technical Document

***

## MOVU

### 23/05/2023

<font size = "2"> **Version:** 1.0.0 </font>

<font size = "2"> **Created on:** 23/05/2023 </font>

<font size = "2"> **Status:** <font color = "Red">Second Version </font>

### Signatures and Auditory

### Version History

| Version      | Date | Author | Change Description |
| ----------- | ----------- | ----------- | ----------- |
| 1 | 20/05/2023 | Octavio Fenalloza | Creation of First Draft |
|2|23/05/2023|Manuel Barrera López Portillo| Second Draft and Corrections|

### Approvers

| Name | Role | Aprover | Approval Date |
| ------ | ----| ----- | --------- |
|Manuel Barrera | Database developer | |
|Ivan | Project Manager ||

## 1 Introduction

### 1.1 Document Objective
This technical document describes the process of creating a PostgreSQL database for a car sales website. The database is intended to store information about cars, sales, customers, and other relevant data.

## 2 Requirements and Details

### 2.1 Database Requirements

The database must be able to store the following data:

- Car information, including make, model, year, mileage, color, VIN, and price
- Sales information, including sale ID, customer ID, car ID, sale date, and sale price
- Customer information, including name, address, phone number, and email address
- Maintenance and repair information, including service date, description of work, cost, and car ID
- Payment information, including payment ID, sale ID, payment date, payment amount, and payment method

### 2.2 Database Design

The database will be designed with the following tables:

- Cars: stores information about each car, including make, model, year, mileage, color, VIN, and price
- Sales: stores information about each sale, including sale ID, customer ID, car ID, sale date, and sale price
- Customers: stores information about each customer, including name, address, phone number, and email address
- Maintenance and Repairs: stores information about each maintenance and repair event, including service date, description of work, cost, and car ID
- Payments: stores information about each payment, including payment ID, sale ID, payment date, payment amount, and payment method

## 3 Scripting

The following scripts were used to create the database:

### 3.1 Script for Addresses

```
CREATE TABLE IF NOT EXISTS addresses(
id SERIAL PRIMARY KEY,
country VARCHAR(20) NOT NULL,
state VARCHAR(50) NOT NULL,
zip_code INT NOT NULL,
address_line1 VARCHAR(50) NOT NULL,export
address_line2 VARCHAR(50)
);
```

This script creates a table called "addresses" with columns for storing address information, including country, state, zip code, address line 1, and address line 2. It also defines an auto-incrementing ID column as the primary key.

### 3.2 Script for creating Customers

```
CREATE TABLE IF NOT EXISTS customers(
uid VARCHAR(50) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
phone VARCHAR(20),
stripe_customer_id VARCHAR(20),
address_id INT REFERENCES addresses(id),
user_status user_status NOT NULL DEFAULT 'active',
photo_url TEXT
);
```

Creates a table called "customers" to store customer information, including their unique identifier (UID), first name, last name, email, phone number, Stripe customer ID, address ID (referencing the "addresses" table), user status, and optionally, a photo URL.

### 3.3 Script for Super admins

```
CREATE TABLE IF NOT EXISTS super_admins(
uid VARCHAR(50) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
phone VARCHAR(20),
user_status user_status NOT NULL DEFAULT 'active'
);
```

This script creates a table called "super_admins" to store information about super admins. It includes columns for unique identifier (UID), first name, last name, email, phone number, and user status. Similar to the previous script, the user status column has a default value of "active".

### 3.4 Script for Automotive distributor

```
CREATE TABLE IF NOT EXISTS automotive_distributors(
id SERIAL PRIMARY KEY,
name varchar(50) NOT NULL,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
approved_at TIMESTAMP,
status status NOT NULL DEFAULT 'in-progress',
user_status user_status NOT NULL DEFAULT 'active',
logo_url TEXT
);
```

Creates a table called "automotive_distributors" to store information about automotive distributors, including an auto-incrementing ID, name, creation timestamp, approval timestamp, status, user status, and logo URL.

### 3.5 Script for Dealership

```
CREATE TABLE IF NOT EXISTS dealerships(
id SERIAL PRIMARY KEY,
dealership_name VARCHAR(100) NOT NULL,
automotive_distributor_id INT REFERENCES automotive_distributors(id) NOT NULL,
website_url TEXT,
logo_url TEXT,
created_at TIMESTAMP NOT NULL DEFAULT NOW(),
status status NOT NULL DEFAULT 'in-progress',
address_id INT REFERENCES addresses(id),
user_status user_status NOT NULL DEFAULT 'active'
);
```

This script creates a table called "dealerships" to store information about dealerships. It includes columns for an auto-incrementing ID, dealership name, automotive distributor ID (referencing the "automotive_distributors" table), website URL, logo URL, creation timestamp, status, address ID (referencing the "addresses" table), and user status. The status column has a default value of "in-progress", and the user status column has a default value of "active".

### 3.6 Script for Employees

```
CREATE TABLE IF NOT EXISTS employees(
uid VARCHAR(50) PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
phone VARCHAR(20),
role employee_role NOT NULL,
auto_distributor_id INT REFERENCES automotive_distributors(id) NOT NULL,
dealership_id INT REFERENCES dealerships(id) NOT NULL,
user_status user_status NOT NULL DEFAULT 'active',
photo_url TEXT
);
```

Creates a table called employees to store employee information.
It has columns for uid (unique identifier), first_name, last_name, email, phone, role (employee role), auto_distributor_id (referencing the id column in the automotive_distributors table), dealership_id (referencing the id column in the dealerships table), user_status (status of the user, with a default value of 'active'), and photo_url.

### 3.7 Script for Financing plans

```
CREATE TABLE IF NOT EXISTS financing_plans(
id SERIAL PRIMARY KEY,
dealership_id INT REFERENCES dealerships(id) NOT NULL,
hitch INT NOT NULL,
months INT NOT NULL,
interest FLOAT NOT NULL
);
```

Creates a table called "financing_plans" to store information about financing plans, including an auto-incrementing ID, dealership ID (referencing the "dealerships" table), hitch, months, and interest rate.

### 3.8 Scripts for Brands

```
CREATE TABLE IF NOT EXISTS brands(
id SERIAL PRIMARY KEY,
name varchar(50),
logo_url TEXT
);
```

This script creates a table called "brands" to store information about car brands. It includes columns for an auto-incrementing ID, brand name, and logo URL.

### 3.9 Scripts for Car Models

```
CREATE TABLE IF NOT EXISTS car_models(
id SERIAL PRIMARY KEY,
brand_id INT REFERENCES brands(id) NOT NULL,
model VARCHAR(20) NOT NULL,
year INT NOT NULL,
spec_sheet TEXT,
description JSON
);
```

This script creates a table called car_models to store car model information.
It has columns for id (auto-incrementing unique identifier), brand_id (referencing the id column in the brands table), model, year, spec_sheet, and description (stored as JSON data).

### 3.10 Script for Listing

```
CREATE TABLE IF NOT EXISTS listing(
  id SERIAL PRIMARY KEY,
  dealership_id INT REFERENCES dealerships(id) NOT NULL,
  car_model_id INT REFERENCES car_models(id) NOT NULL,
  car_variant_id INT, -- REFERENCES car_variant(id)
  status car_status NOT NULL,
  base_price FLOAT NOT NULL,
  test_drive BOOLEAN
);
```

This script creates a table called "listing" to store information about car listings. It includes columns for an auto-incrementing ID, dealership ID (referencing the "dealerships" table), car model ID (referencing the "car_models" table), car variant ID (to be implemented), status, base price, and test drive availability.

### 3.11 Script for Documents

```
CREATE TABLE IF NOT EXISTS documents(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  document_url VARCHAR(100) NOT NULL,
  status status NOT NULL DEFAULT 'in-progress',
  customer_id VARCHAR(50) REFERENCES customers(uid),
  dealership_id INT REFERENCES dealerships(id),
  automotive_distributor_id INT REFERENCES automotive_distributors(id)
);
```

This script creates a table called documents to store document information.
It has columns for id (auto-incrementing unique identifier), name, document_url, status (status of the document, with a default value of 'in-progress'), customer_id (referencing the uid column in the customers table), dealership_id (referencing the id column in the dealerships table), and automotive_distributor_id (referencing the id column in the automotive_distributors table).

### 3.13 Script for Order

```
CREATE TABLE IF NOT EXISTS orders(
  id SERIAL PRIMARY KEY,
  listing_id INT REFERENCES listing(id) NOT NULL,
  customer_id VARCHAR(50) REFERENCES customers(uid),
  status status NOT NULL DEFAULT 'in-progress',
  seller_id VARCHAR(50) REFERENCES employees(uid) NOT NULL,
  subtotal FLOAT NOT NULL,
  configuration JSON NOT NULL,
  financing_plan_id INT REFERENCES financing_plans(id) NOT NULL,
  due FLOAT NOT NULL
);
```

This script creates a table called orders to store order information.
It has columns for id (auto-incrementing unique identifier), listing_id (referencing the id column in the listing table), customer_id (referencing the uid column in the customers table), status (status of the order, with a default value of 'in-progress'), seller_id (referencing the uid column in the employees table), subtotal, configuration (stored as JSON data), financing_plan_id (referencing the id column in the financing_plans table), and due.

## 4 Testing and Validation

### 4.1 Testing methodology

The database was tested by inserting sample data and verifying that it was stored correctly. The database was also tested by performing various queries to ensure that the data could be retrieved and processed correctly.

## 5 Deployment and Maintenance

### 5.1 Deployment
To deploy the database, the scripts were executed on a PostgreSQL server. The server was configured to allow remote access and backups were scheduled regularly to ensure data integrity. Maintenance of the database includes regularly optimizing and tuning the database for performance, and ensuring that backups are properly secured and stored. It is also important to regularly update the database software to ensure that security patches and bug fixes are applied.

## 6 Security Measures

### 6.1 Methodology

To ensure the security of the database, the following measures were implemented:

- Unique logins and passwords are required for all users who access the database.
- Passwords are required to be complex and changed regularly.
- All communication with the database is encrypted using SSL.
- Access to sensitive information is limited to authorized personnel only.
- The database is regularly backed up and stored in a secure off-site location.
- The database is regularly audited to ensure that there are no security vulnerabilities or unauthorized access.

## 7 Procedures and Usage

### 7.1 Database Data Upload

#### 7.1.2 CSV Method

The authorized user (Auto Angency Employee) must upload the information to update the listings data
through a csv file with the following order:

- name: the name of brand of the Autogroup.

- logoUrl: Official logo of the brand.

- model: Model of the Car.

- body_type: example of car variant: "Sedan"

- year: Year of car model production.

- specSheet: detailed sheet.

- fullName: Full car name:"Ford Territory 2023"

- variantName: Car variant related to color.

- isNew: determined if car has not been previously used.

- usedKm: number of kilometers driven.

- writtenDescription: Extra details related to the car.

- tags: search related tags

- fullDescription: Complete descriptions that need to be known by the costumer.

- fuelType: Diesel, premium or lean.

- horsePower: Amount of power measured in Horsepower.

- passengers: Maximum number of allowed passangers in car.

- traction: All wheel, front wheel, rear wheel drive.

- transmission: Manual or Automatic

- spin: included or not

- oilConsume: Oil type consumed.

- liter: Fuel capacity.

- numberDoors: number of doors in the car.

- rimMaterial: Aluminum, steel, custom.

- rim: Size of the rim.

- airConditioning: included or not

- abs: included or not

- rearAirbags: included or not

- frontAirbags: included or not

- colors: available color.

- basePrice: price in MXN.

- testDrive: available or not.

### 7.2 Listings

#### 7.2.1 Endpoints

- getAutoComplete: Aid the user by completing their string with system sugestion.
- getListings/search: Elastic Search returns the listngs by relevancy.
- getListingsById: Gives front end the information to proyect the DB information.

#### 7.2.2 Expected Results

It is expected that when the user inputs information on the search bar to see the following steps:

- The User starts typing and the Auto Complete brings out possible string.

- The user inputs their selection in the search bar.

- The system using Elastic Search returns the results ordered by relevance.

- The system proyects in the listing page the results.

### 7.3 User Registry

#### 7.3.1 Endpoints

- createUser (firebase): connects to firebase to upload the personal information of the new user.
- updateUser (firebase): connects to firebase to update the information of an existing user.

#### 7.3.2 Expexted Results

It is expected that when the user inputs information on the user creation view to see the following steps:

- The user inputs the correct information to the system.

- The system connects to Firebase DB to upload the information.

- If the request is an user creation and the information is valid, the user is created and its ID returned.

- If the request is an update and the information is valid, the user is updated.

### 7.4 Wishlists

#### 7.4.1 Endpoints

- getUserWishlist: Retrieve the user's related id.
- deleteCarFromWishlist: Deletes a value inside a user's Wishlist array.

#### 7.4.2 Expected Results

It is expected that when the user's wishlist to exist, to follow the hereunder flow:

- If the user creates adds a wishlist bring the carId to the wishlist. It remains there until deleted.

- If the user deletes an element of the wishlist, the carid is unrelated.

## 8 Diagrams

### 8.1 Database Architecture

![ArchitectureDB](arquitecturaDB.PNG)

The arquitecture of the DB can be described by the following flow:

```Script SQL -> Translation to JavaScript (ORM) -> Query in Lambda Function -> Return Info in JSON -> Information returns to Frontend```

### 8.2 Database Diagram

![DBD](DBDiagram.png)

This is the DB structure and how information is related to each other.