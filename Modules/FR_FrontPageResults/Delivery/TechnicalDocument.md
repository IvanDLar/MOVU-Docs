# FR - Front Page Results

## Date: 12 june 2023

## Version

* v1.1 - Joshua Amaya

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

### 1. Install Git

If you haven't already, download and install Git from the official website for your operating system (https://git-scm.com/).

### 2. Clone the repository

Open a terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the repository:

   ```
   git clone <repository_url>
   ```

   Replace `<repository_url>` with the URL of the GitHub repository.

   ```
   git clone https://github.com/IvanDLar/MOVU-FrontEnd.git
   ```

### 3. Install Node.js

Next.js requires Node.js to be installed on your machine. You can download it from the official website

   ```
   (https://nodejs.org/)
   ```

   and follow the installation instructions.

### 4. Navigate to the project directory

Use the `cd` command to change into the project directory that was created when you cloned the repository. For example:

   ```
   cd MOVU-FrontEnd
   ```

### 5. Install project dependencies

The project tyically has dependencies listed in a `package.json` file. To install these dependencies, run the following command:

   ```
   npm install
   ```

   This will download and install all the necessary packages required by the project.

### 6. **.env file**

It is necessary to have the most recent version of the .env file inside the project in order to access it with the appropriate credentials. In case of not obtaining it, a personal .env file can be created following the structure provided in

   ```
    .env.example
   ```

### 7. Start the development server

Once the dependencies are installed, you can start the Next.js development server using the following command:

   ```
   npm run dev
   ```

   This command will start the development server and provide you with a local URL where you can view the project in your web browser. Typically, it will be `http://localhost:3000`.

### 8. Open the project in a web browser

Launch your preferred web browser and navigate to the local development URL provided by the previous step (`http://localhost:3000` by default). You should now see the Next.js project running locally.

## API Description

MOVU application exposes an API that enables users to perform various actions, such as searching for vehicles, adding vehicles to the inventory, and processing sales. The API is structured as follows:

* **Endpoints**: The API provides several endpoints to interact with different functionalities of the application. These endpoints include:

    * '/compareCars': This view shows a list of the cars you wish to compare, and you can delete or buy them (by making the required choice) if desired
    * '/employee/profile': This tab displays the employee's information, showing name, email, address and dealership, as well as the possibility to edit the basic information.
    * '/employee/usuarios': This tab displays the employee's information, showing name, email, telephone, address; the individual's interests can be added as well as uploading official documents that can be used to make purchases within the application.
    * '/home': This view is the landing page, which is initially displayed when the application is opened.
    * '/search': View where all cars resulting from a specific search are displayed as a table, also showing manual filters such as region, price, and car variants.
    * '/wishList': Window where the favorite cars selected by the user are displayed, either to compare different models and buy them later or to save offers and favorite brands.
