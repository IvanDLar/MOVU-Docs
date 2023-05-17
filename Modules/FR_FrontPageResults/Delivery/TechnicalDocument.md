# FR - Front Page Results

## Date: 15 may 2023

## Version

* v0.1 - Joshua Amaya

## Document Structure

1. Introduction
2. Localhost explanation
3. Installation instructions
4. API description
    * Endpoint details
    * Sample requests and responses
    * Response Formats

## Introduction

The objective of this technical document is to describe the Front Page Results Section, emphasizing in how Localhost works and how to run it, besides and API description of this module.

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
