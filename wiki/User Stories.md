# User Stories

Created: February 20, 2023 5:46 PM
Last edited time: March 7, 2023 6:28 PM
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
