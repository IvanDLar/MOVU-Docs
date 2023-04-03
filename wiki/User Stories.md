# User Stories

Created: March 30, 2023 5:46 PM // 
Last time edited: April 3, 2023 13:30 PM
Tags: document

**LINK FORMATO**

[TC3004B.102 - Google Drive]()

## Table of contents

# **Systems**

## **Login**

<br>

**US01 - Account Sign Up**

As a user I want to register on the platform with data that is not very sensitive if I am not sure about buying or directly with Google to protect my integrity and use the services offered by the platform when registering

**Validation:**

- Create account screen that allows

1. Enter email
2. Enter password
3. Input personal data (address, zip code, etc.)
4. If everything is correct, the user is created, otherwise an error popup is shown on the screen

**Priority**: Very High

**Estimate**: 1 week

**US02 - Account Login**

As a customer I can log in with email and password or directly with google. To be able to do it in a much easier way, without the need to fill out an entire form.

**Validation:**

Button that connects with firebase auth and allows you to login directly with google:

1. Button with the Google logo, to let the user understand about this functionality.
2. A google pop-up will appear that will allow you to easily log in.
3. It will also be possible to login with username and password.

**Priority**: Very High

**Estimate**: 1 week

**US03 - Account Logout**

As a customer, salesperson, manager, super-admin, automotive group administrator I must be able to log out. So that nobody can use my username in case of losing my device.

**Validation:**

Button in the navigation bar, which when clicked deletes all user information saved as status in the web application.

1. When you click the button, your information will no longer be on the front. Which means you will lose access to payment and chat features.

**Priority**: Very High

**Estimate**: 1 week

## **Accounts**

**US04 - Reset Password**

As a user I want to have the option to change my account information or reset my password without losing my data to continue using my account and not have to create it and also maintain control of its security.

**Validation:**

There must be a section in the menu that leads to the stored user information, where you can request changes to your information, the user edits, and emails or messages are sent that need confirmation (by the requesting user) to save the changes in the DB

**Priority**: High

**Estimate**: 1 week

**US05 - Super admin register**

As Super-Admin I must be able to register other super users so that several people can control the platform and register groups.

**Validation:**

Screen to register other super administrators:

1. Section or form where they can create new super admins.
2. They will be created with random passwords.

**Priority**: High

**Estimate**: 1 week

**US06 - Automotive Group register**

As Super Admin I must be able to register the automotive groups so that they can begin operations within the application

**Validation:**

Screen to register automotive groups:

1. Section or form where they can create new automotive groups.
2. They will be created with random passwords.

**Priority**: High

**Estimate**: 1 week

**US07 - Agency register**

As Super Admin I must be able to register the automotive groups so that they can begin operations within the application

**Validation:**

Screen to register automotive groups:

1. Section or form where they can create new automotive groups.
2. They will be created with random passwords.

**Priority**: High

**Estimate**: 1 week


**US08 - Sellers register**

As a manager I want to be able to register sellers so they can make sales and contact customers within the application.

**Validation: **

Screen to register sellers:

1. Managers must have a form where they can register vendors from their agency.
2. The new seller must be created by the manager and with a random password.
3. All necessary fields must be entered to create the manager.

**Priority**: High

**Estimate**: 1 week


**US09 - Cancel account**

As a user, I want to be able to cancel the creation of my account so that I do not have an account on a platform that I will not use and that contains my data.

**Validation:**
When the user creates an account, he receives a confirmation email where he has the option to cancel the account creation in the same email, when canceling (with a hyperlink button) the request is canceled and the data is not stored.

1. Availability of cancel account button
2. Delete user account without storing any personal data in the database

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Could Have


**US10 - Access without registration**

As a user, I want to access the page without registering to see the catalog and decide whether to use the platform to buy a car.

**Validation:**
The user accesses the page and can perform actions that do not require user verification.

1. The different models available with their characteristics, cost to the public, and agency are shown.
2. When you click on the account button, the account creation or login interface appears.

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have


**US11 - User register/login**

As a user, I want to log in (in the account that I create) without a problem to be able to view my account information

**Validation:**
Sign in option displayed when attempting some user-restricted actions

1. when accessing menu > login, in any of the 2 cases; access with your user credentials and can view the saved information.

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

## **Payments**

**US35 - Register payment info in agency**

As a customer I must be able to register a payment method. To be able to make transactions in the application and buy the vehicles.

**Validation:**

When selecting to pay in a car, I will have the option to choose between multiple payment methods through a simple click. This together with stripe will allow users to select their payment methods and do everything within the platform.

1. By selecting payment method I will be able to enter my personal information.
2. A stripe component will be rendered to make the payment
3. If successful, modify database. If an error occurs, show it to the user.

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have


**US34 - Register payment info**

As an agency I must enter data to which the funds of any purchase will arrive. So that the funds reach the desired account.

**Validation:**

When the agency is accepted by the super-admin, they will be forced to add their bank account information. So that the payments are from the client to the agency, with the only intermediary the API that we use (example: Stripe)

1. Agency enters bank account details
2. Save encrypted data in the database

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have


**US35 - Payment changes**

As a user, I want to be able to see the interior and exterior photographs in detail to have a better visualization of the vehicle

**Validation:**

When the user selects a vehicle, they can go through the images provided by the agencies, to explore its structure both inside and outside in detail.

1. Agency provides images of the vehicle inside-out
2. The images are shown to the client on the application

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have


**US36 - Payment opportunities for clients**

As a user/buyer, I want to see the payment options and terms that each agency offers me to be able to make choices and finance according to my economic possibilities.

**Validation:**

When a quote is made, the available options given by the agency (static) are seen. When a formal purchase is made, the options may vary depending on the down payment.

User can see the available options of the agency
The options are shown depending on the down payment

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must have


**US37 - Payments for custom order**

As a buyer, I want to have the option of customizing elements of my vehicle (as long as the model/agency allows it) and see how the price varies to make my choice according to my budget

**Validation:**
When selecting a vehicle, the option to customize or choose an agency that has the same customizable model is shown, it can be through a quote or at the time of a purchase request.

A customized button is displayed on available vehicles
The user can view the customizable vehicles and customize them.

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Should Have


**US39 - Download quotes or view**

As a user, I want to download my quotes in PDF or have a space within my profile to view and analyze them and make the right decisions when buying a vehicle.

**Validation:**
When the user makes a vehicle quote, a "save/download" button appears, depending on the type of button the operation process changes, a PDF will be downloaded or saved in the profile (give preference to the first option)

The "save" button is displayed
The quote is saved in the client's account
The "download" button is displayed
The quote is downloaded in the client's browser

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Could have


**US40 - Setting up financing plans**

As an agency, I want to be able to set up my financing and insurance plans (including rates and plans) to manage agency costs and monitor necessary changes according to the market.

**Validation:**
When a manager uploads a car, he will need to fill out a cost section where he can add fixed options that he drives so that platform users can view them in their quotes.

1. A customized button is displayed on available vehicles
2. The user can view the customizable vehicles and customize them.

**Priority:** Medium

**Estimate:** 1 week

**Classification: ** Must Have


**US41 - Sales price display**

As a user, I want to see the price of sale to the public without having to register

**Validation:**
When viewing vehicles in the catalog or in an overview on the main page (as featured or promoted models), the retail prices are displayed.

1. Display of prices without prior registration
2. Display of prices with registration

**Priority:** Medium

**Estimate:** 1 week

**Classification: **  Must Have


**US42 - Vehicles quotation**

As a user, I want to quote a vehicle model and see what factors can increase the final cost of a model

**Validation:**
When selecting a specific vehicle, approximate expenses can be selected in the calculator (at the bottom of the page) to show an approximation of the final price, such as insurance, and down payment...

1. Price calculator that changes depending on the option chosen
2. Show approximations depending on the chosen vehicle

**Priority:** Medium

**Estimate:** 1 week

**Classification: ** Could Have



## **Security**

## **Super Admin (NDS)**

## **Admin (Automotive Group)**

## **Vendor**

## **User**

## **Search**

## **Cars**

## **Comunication**

## **Test Drive**

## **Documentation**
