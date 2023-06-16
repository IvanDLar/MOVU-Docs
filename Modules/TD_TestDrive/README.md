# Test Drive Module deliverys
- Andrea Yela González   A01025250
- Emilio Sibaja Villarreal   A01025139
- Ariadne Álvarez Reyes   A01652080
- Salvador Salgado Normandia   A01422874
- Ivan Díaz Lara   A01365801	
## Table of Contents
- [Introduction](#introduction)
- [User Stories](#user-stories)
- [Validations](#validations)
- [Test Document](#test-document)
- [Test Drive Views](#test-drive-views)
- [User Manual](#user-manual)
- [Code](#code)

## Introduction
At Movu, we prioritize the client’s experience during the purchase of a new car, knowing that the best way to know which car to buy is to test it yourself. We developed all the needed features so  the user can request a test drive by selecting their preferred car and filling out a simple form. In this document we present the most relevant information of the “TestDrive” module.

## User Stories
- [US55 - Easy Test Drive Application](https://github.com/IvanDLar/MOVU-Docs/milestone/19)
- [US56 - Test Drive Requirements](https://github.com/IvanDLar/MOVU-Docs/milestone/20)
- [US57 - Skip Drive](https://github.com/IvanDLar/MOVU-Docs/milestone/21)
- [US58 - Test Drive Documents](https://github.com/IvanDLar/MOVU-Docs/milestone/22)

## Validations
- [VA571 - Making sure the Test Drive is not a requirement to purchase the vehicle](https://github.com/IvanDLar/MOVU-Docs/issues/94)
- [VA581 - When requesting a test drive the user should have an input to upload multiple files](https://github.com/IvanDLar/MOVU-Docs/issues/96)
- [VA551 - In any car appearance in any ecommerce page (user view), an easy to access test drive request button will be shown.](https://github.com/IvanDLar/MOVU-Docs/issues/65)
- [VA582 - Have as a mandatory requirement the submission of all necessary documents](https://github.com/IvanDLar/MOVU-Docs/issues/98)
- [VA553 - Once TD button is activated and the forms to request the TD are complete its dashboard will update with the test drive details.](https://github.com/IvanDLar/MOVU-Docs/issues/67)
- [VA552 - Once the user answers a form with specific information as well add sending its valid driver license, he will have to wait for the agencies approval](https://github.com/IvanDLar/MOVU-Docs/issues/66)
- [VA561 - Salesman Dashboard will be a section to manage the test drives. Here the salesman can view the applications as well as approving or denying the test](https://github.com/IvanDLar/MOVU-Docs/issues/86)

## Test Document
- [Test Document in excel](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/Delivery/PruebasRecorridoTestDrive.xlsx%20-%20Tours.pdf)

## Test Drive Views

- [Test Drive Views Video](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/Delivery/TestDriveViews.mp4)

### Salesman Views
- Test Drive Table

This will be the section where the salesman will be able to manage their active and inactive car testing appointments, they will be able to validate the information of each and every one of the appointments that were made as well as changing the status of this appointments. It's important to highlight that the salesman will only be able to view the test drive appointments that they were assigned by the car dealership manager. (Image 1.1)

- Details of Test Drive
This view shows the test drive details that salesman can see, these views are not available or accessible to other users. The name and model will be displayed for which the test drive was requested. On the other hand, there will be a document verification section, where salesman will be able to check the documents uploaded by the user, in this case it will be necessary to check that the driver's license has been uploaded correctly. Finally, the application can be accepted or rejected. This status can be checked in the previous page Test Drive Table. (Image 1.2)

### Ecommerce Views
- Test Drive application forms

The view is for our users to set all the required information we need for us to give them a test drive. First it is asked for a document, where the user has to upload a picture of their driver's license, after it, the user is able to set the date and time that fits best for both the tester and the dealership’s employee. At last, the user must see the name that was used to register their account (users must be logged in to access this view), and after it, they must fill in the direction of where they wish the test drive to be carried out and finally, send their request to the dealership for review. (Image 2.1)

- Test Drive Information 

The user can see their test drive information in this view. The tracker helps the user to see how their process is going. This tracker shows the same status that is on the salesman table, and it refreshes when the status changes. The tracker has 3 types of circles: "check", "onway" and "pending", and depending on the status is the type of circle the tracker has. Also the user can see the information of their test drive, like the car they solicitated, the date, hour and the address of the test drive. (Image 2.2)

- User Test Drive List

On the users menu they can click on "Pruebas de Manejo" so they can see the test drives they have solicitated, even the ones finished or canceled. (Image 2.3)

### Images
![TD Employee Table](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/employee_testDriveList.png)

<div align="center"> 1.1 </div>

![Details of test drive](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/testDriveDetails.png)

<div align="center"> 1.2 </div>

![User test drive forms](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/testDriveDoc.png)

<div align="center"> 2.1 </div>

![User test drive information](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/testDriveData.png)

<div align="center"> 2.2 </div>

![User test drive list](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/testDriveList.png)

<div align="center"> 2.3 </div>

## User Manual

- [User Manual pdf](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/Delivery/TD_Manual.pdf)

## Code
...
