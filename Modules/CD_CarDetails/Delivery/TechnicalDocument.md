# CD - Car Details

## Date: 12 june 2023

## Version

* v0.1 - Joshua Amaya

## Document Structure

1. Introduction
2. User Stories
3. API Description
    * Endpoint Details
4. Views

## Introduction



## User Stories

|   ID      |   User Story                      |   Validations |   Description |
|-----------|-------------------                |---------------|---------------|
|   US13    |   Payments opportunities for clients  |   US131       |   User can see the available financing options offered by the car dealership  |
|           |                                   |   US132       |   The financing options are dynamic (depending) on the down payment   |
|   US14    |   Payments for custom order       |   US141       |   Display list of all available customizations    |
|           |                                   |   US142       |   If a customization is not currently available gray out the button holding the option    |
|           |                                   |   US143       |   A customized button is displayed on available vehicles    |
|   US15    |   Download quotes or view         |   US151       |   Display the "download" button near the displayed price of the car    |
|           |                                   |   US152       |   The quote is downloaded in the client's browser    |
|   US18    |   Dynamic Pricing                 |   US181       |   Reflect changes on the final price when selecting extras, such as car customizations and financing/insurance options    |
|   US41    |   Displaying the available financing plans submitted by the car retailer  |   US411       |   A list of different insurance options with the price of each of the options will be displayed in the car details page    |
|           |                                   |   US421       |   A list of different financing options with the price of each of the options will be displayed in the car details page    |
|   US45    |   Car Visualization               |   US452       |   If the user selects a specific car, they will be redirected to another section with all the description of the car    |
|   US46    |   Car characteristics comparison  |   US461       |   While inspecting the vehicles, the user will be able to click a button that redirects them to a comparative section    |
|           |                                   |   US463       |   Once the cars are selected, the key car characteristics will be placed side by side for better analysis    |
|   US47    |   Indoor and outdoor display      |   US471       |   When the user selects a vehicle, they can go through the images provided by the car dealerships, to explore its structure both inside and outside in detail    |
|           |                                   |   US472       |   Inside the car details, the users will be able to view the vehicle 360º    |
|   US49    |   Car shopping Wishlist           |   US492       |   When accessing the wishlist, all the cars previously select need to appear in this section    |

## API Description

MOVU application exposes an API that enables users to perform various actions, such as searching for vehicles, adding vehicles to the inventory, and processing sales. The API is structured as follows:

* **Endpoints**: The API provides several endpoints to interact with different functionalities of the application. These endpoints include:

    * '/purchaseList': On this page the customer can follow up on purchases he/she has previously made. The view shows the image of the purchased vehicle, the vehicle model, a description of the arrival date as well as the status of the order. Inside the box, a button is displayed that redirects to the details of the purchase.
    * '/purchaseDetails': In this view the customer can visualize the status of his purchase, from the creation of the order to the arrival of the vehicle. Likewise, the image of the vehicle, the make and model as well as its corresponding logo are displayed. Divided into two boxes, the details of the transaction as well as the total cost of the purchase are displayed. The details include the name of the seller, the date of arrival and request, the status of the car, the dealer in charge of the sale and the shipping address. At the end, there are two buttons, the first one to view the documents generated from the transaction and another button to request help from an employee in case there is any problem with the order.
    * '/carDetails': The page displays detailed information about the vehicle to be sold, showing its model, make and logo as well as its base price. On the other hand, a description provided by the agency and the details of the vehicle are displayed. The image of the car is shown in 360° for the user's convenience as well as a gallery section so that the client can get to know the car in more detail. If required, all the details about the variants that the product has, such as the type of body, transmission or gasoline, are displayed. Among the buttons is the one to buy or to schedule a test drive if the user decides to try the car before buying it.
    * '/carDetailsDelearship': In this view, dealers can register a new vehicle that will be displayed within the application. In order for the vehicle to appear correctly in the system, the requested fields must be filled in, such as model name, type of traction, year, brake system, number of doors, among other variants. Likewise, a base price is assigned and the pertinent forms are filled out in order to register the vehicle.
 
## Views
![Captura de Pantalla 2023-06-07 a la(s) 18 47 19](https://github.com/IvanDLar/MOVU-Docs/assets/78172208/9aedb1bb-8d1f-4062-a93f-b6df7669dd3d)

![Captura de Pantalla 2023-06-07 a la(s) 18 47 35](https://github.com/IvanDLar/MOVU-Docs/assets/78172208/00d0999e-4681-419e-901f-52f47b77372c)

![image](https://github.com/IvanDLar/MOVU-Docs/assets/110345846/5dd76a51-8828-4d9b-b64b-bbb0d2ad9b36)

![image](https://github.com/IvanDLar/MOVU-Docs/assets/73249378/707cf479-7cb0-458a-83f4-0c28f67bf1f4)
