# FR - Front Page Results

## Date: 17 may 2023

## Version

* v0.2 - Joshua Amaya

## Document Structure

1. Introduction
2. User Stories
3. Localhost Explanation
4. Installation Instructions
5. API Description
    * Endpoint Details
    * Sample requests and responses
    * Response Formats

## Introduction

The objective of this technical document is to describe the Front Page Results Section, emphasizing in how Localhost works and how to run it, besides and API description of this module.

## User Stories

|   ID      |   User Story                      |   Validations |   Description |
|-----------|-------------------                |---------------|---------------|
|   US09    |   Delete account                  |   VA091       |   Display message that informs the user how to delete their account   |
|   US31    |   Vendors Administration          |   US311       |   Create an employee account  |
|           |                                   |   US312       |   Update employee account |
|           |                                   |   US313       |   Get employee accounts from an automotive group|
|           |                                   |   US314       |   Delete employee account |
|   US38    |   Modify personal information     |   US381       |   When a registered user clicks the edit button, changes a field and saves data, it is stored in Firebase and the old information is erased   |
|   US39    |   Website access                  |   US391       |   user can enter the web page in any device with internet connection  |
|   US40    |   NL Search                       |   US401       |   The landing page will have a search bar where the users will be able to write a simple car description which will then return a list of vehicles that match that criteria   |
|           |                                   |   US403       |   Filter with the given information and return the list of cars that match the criteria   |
|   US42    |   Filter search                   |   US421       |   In the car display page, the users should be able to select specific filters which allow a more detailed result |
|           |                                   |   US422       |   Once the specific filters are selected, the webpage will sned those parameters to the DB    |
|           |                                   |   US423       |   The DB will obtain the cars that align with the filters and then return them to the webpage.    |
|           |                                   |   US424       |   Display the result of the DB filter |
|   US43    |   No login Search                 |   US431       |   The user can use the NL search function without having an account   |
|           |                                   |   US432       |   The user can use the form search function without having an account |
|   US44    |   NL Search always available      |   US442       |   Whenever the user interacts to the search bar, they must always obtain the car  |
|   US45    |   Car visualization               |   US415       |   For every car that is displayed, it must have general information before clicking the car for more details  |
|   US46    |   Car characteristics comparison  |   US462       |   The webpage will give the user the list of all available cars, in which they can select two cars to compare |
|   US49    |   Car shopping wishlist           |   US492       |   When accessing the wishlist, all the cars previously select need to appear in this section  |
|   US55    |   Easy test drive application     |   US551       |   In any car appearance in any ecommerce page (user view), an easy to access test drive request button will be shown  |
|   US63    |                                   |   US631       |   Display user profile page that shows the previously defined personal information    |
|           |                                   |   US632       |   Edit user profile page  |
|   US64    |                                   |   US641       |   Display employee profile page that shows the previously defined personal information|
|           |                                   |   US642       |   Edit employee profile page  |

## Localhost Explanation 

Localhost refers to the local development environment on a computer where the application is being built and tested. It allows developers to simulate the app's functionality without the need for a live server or an internet connection. By using localhost, developers can perform various tasks, such as testing API endpoints, debugging code, and verifying system behavior.

## Installation Instructions

### **Install Node.js in the computer**
    
Node.js can be downloaded from 
    
    https://nodejs.org/en/download 

### **Install yarn**

Yarn must be installed form the command line as follows

```
npm install --global yarn
```

### **.env file**

It is necessary to have the most recent version of the .env file inside the project in order to access it with the appropriate credentials. In case of not obtaining it, a personal .env file can be created following the structure provided in 

    .env.example

### **Run application**

To run the proyect, type in command line

```
yarn dev
```

### **Open app in browser**

The application will start running in port 3000. Open the browser in the following link:

```
http://localhost:3000/
```

## API Description

MOVU application exposes an API that enables users to perform various actions, such as searching for vehicles, adding vehicles to the inventory, and processing sales. The API is structured as follows:

* **Endpoints**: The API provides several endpoints to interact with different functionalities of the application. These endpoints include:

    * '/compsignup'
    * '/forgot'
    * '/home'
    * '/index'
    * '/login'
    * '/purchaseList'
    * '/signup'
    * '/wishList'
