# Test Drive Module deliverys
## Table of Contents
- [Introduction](#introduction)
- [User Stories](#user-stories)
- [Validations](#validations)
- [Risk and Mitigations](#risk-and-mitigations)
- [Test Document](#test-document)
- [Test Drive Views](#test-drive-views)
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


## Risk and Mitigations
| Risk                 | Mitigations            |
|----------------------|------------------------|
| 4/5 team members have not made end points and the one that did was occupied with other groups.| We focused on the front end the first week while we started practicing with the end points.|
| We are a small group with many task that need to be done   | Dividing the task evenly for each team member, and did regular meeting to help each other.|


## Test Document
The test drive tests will start the 9th of June, unitl then we don't count with the test document.

## Test Drive Views
### Salesman Views
- Test Drive Table

![TD Employee Table](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/employee_testDriveList.png)

This will be the section where the salesman will be able to manage their active and inactive car testing appointments, they will be able to validate the information of each and every one of the appointments that were made as well as changing the status of this appointments.

Its important to highlight that the salesman will only be able to view the test drive appointments that they were assigned by the car dealership manager.

- Details of Test Drive

![Details of test drive](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/TDDetails.png)

This view shows the test drive details that salesman can see, these views are not available or accessible to other users. The name and model will be displayed for which the test drive was requested. On the other hand, there will be a document verification section, where salesman will be able to check the documents uploaded by the user, in this case it will be necessary to check that the driver's license has been uploaded correctly. Finally, the application can be accepted or rejected. This status can be checked in the previous page Test Drive Table

### Ecommerce Views
- Test Drive application forms

![User test drive forms](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/testDriveDoc.png)

The view is for our users to set all the required information we need for us to give them a test drive. First it is asked for a document, where the user has to upload a picture of their driver's license, after it, the user is able to set the date and time that fits best for both the tester and the dealership’s employee. At last, the user must see the name that was used to register their account (users must be logged in to access this view), and after it, they must fill in the direction of where they wish the test drive to be carried out and finally, send their request to the dealership for review.

- Test Drive Information 

![User test drive information](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/testDriveData.png)

The user can see their test drive information in this view. The tracker helps the user to see how their process is going. This tracker shows the same status that is on the salesman table, and it refreshes when the status changes. The tracker has 3 types of circles: "check", "onway" and "pending", and depending on the status is the type of circle the tracker has. Also the user can see the information of their test drive, like the car they solicitated, the date, hour and the address of the test drive.

- User Test Drive List

![User test drive list](https://github.com/IvanDLar/MOVU-Docs/blob/main/Modules/TD_TestDrive/img/testDriveList.png)

On the users menu they can click on "Pruebas de Manejo" so they can see the test drives they have solicitated, even the ones finished or canceled.

## Code
...
