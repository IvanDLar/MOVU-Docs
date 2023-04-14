# User Stories

Created: March 30, 2023 5:46 PM //
Last time edited: April 3, 2023 13:30 PM
Tags: document

**LINK FORMATO**

[TC3004B.102 - Google Drive]()

## Table of contents

# **Systems**

## NLP E-Search

## Auth Clients

## Front Page Results

## Home Page

## Test Drive

## Data Base

## Super Admin

## Project Reports

## In App Messaging

## Car Details

## Payments

## Car Retailers

---

---

## **US01 - Account Sign Up**

As a user I want to register on the platform with data that is not very sensitive. If I am not sure about buying or directly with Google to protect my integrity and use the services offered by the platform when registering

**Validation:**

- VA011 - The user can register into the platform by email or a google account.
  - AC - Auth Clients
- VA012 - The user must have a secure password with at least 8 characters.
  - AC - Auth Clients
- VA013 - The email and password must be in Firebase.
  - AC - Auth Clients
  - DB - Data Base
- VA014 - If at least one field is not valid, the user can not continue registering.
  - AC - Auth Clients

**Priority**: Very High

**Estimate**: 1 week

---

---

## **US02 - Account Login**

As a customer I can log in with email and password or directly with google. To be able to do it in a much easier way, without the need to fill out an entire form.

**Validation:**

- VA021 - Google sign up button leads you to Google Sign up
  - AC - Auth Clients
- VA022 - When entering an email or password that's not in Firebase, shows error and doesn't let the user log in.
  - AC - Auth Clients
  - DB - Data Base
- VA023 - When entering an email or password that's in Firebase,lets the user log in.
  - AC - Auth Clients
  - DB - Data Base

<!-- Button that connects with firebase auth and allows you to login directly with google:

1. Button with the Google logo, to let the user understand about this functionality.
2. A google pop-up will appear that will allow you to easily log in.
3. It will also be possible to login with username and password. -->

**Priority**: Very High

**Estimate**: 1 week

---

---

## **US03 - Account Logout**

As a customer, salesperson, manager, super-admin, automotive group administrator I must be able to log out. So that nobody can use my username in case of losing my device.

**Validation:**

- VA031 - When clicking the "Cerrar Sesión" button deletes all user information saved as status in the web application and the user information will no longer be on the front. Which means you will lose access to payment and chat features.
  - DB - Data Base
  - HP - Home Page

<!-- Button in the navigation bar, which when clicked deletes all user information saved as status in the web application.

1. When you click the button, your information will no longer be on the front. Which means you will lose access to payment and chat features. -->

**Priority**: Very High

**Estimate**: 1 week

---

---

## **US04 - Reset Password**

As a user I want to have the option to change my account information or reset my password without losing my data to continue using my account and not have to create it and also maintain control of its security.

**Validation:**

- VA041 - When selecting "Olvidé mi contraseña" in the log in page it redirects you to the Change password screen.
  - AC - Auth Clients
- VA042 - If the email inserted in the "Restablecer Contraseña" screen is stored in the Firebase, an email is send with a link to restore the password.
  - AC - Auth Clients
  - DB - Data Base
- VA043 - Entering the link that came in an email lets the user insert a new password.
  - AC - Auth Clients
- VA044 - The user must insert secure password with at least 8 characters.
  - AC - Auth Clients
- VA045 - The new password is stored in Firebase an the old password is erased.
  - AC - Auth Clients
  - DB - Data Base
- VA046 - When a registered user clicks the edit button, changes a field and saves the data, it is stored in Firebase and the old information is erased.
  - DB - Data Base
  - HP - Home Page

<!-- There must be a section in the menu that leads to the stored user information, where you can request changes to your information, the user edits, and emails or messages are sent that need confirmation (by the requesting user) to save the changes in the DB -->

**Priority**: High

**Estimate**: 1 week

---

---

## **US05 - Super admin register**

As Super-Admin I must be able to register other super users so that several people can control the platform and register groups.

**Validation:**

- VA051 - The super admin can register into the platform by email or a google account.
  - SA - Super Admin
- VA052 - The super admin must have a secure password with at least 8 characters.
  - SA - Super Admin
- VA053 - The email and password must be stored in firebase.
  - SA - Super Admin
- VA054 - If at least one field is not valid, the user can not continue registering.
  - SA - Super Admin

<!-- Screen to register other super administrators:

1. Section or form where they can create new super admins.
2. They will be created with random passwords. -->

**Priority**: High

**Estimate**: 1 week

---

---

## **US06 - Automotive Group register**

As Super Admin I must be able to accept an application of an automotive groups so that they can begin operations within the application.

**Validation:**

- VA061 - Table with all the applications of the automotive groups.
  - SA - Super Admin
- VA062 - Super Admin can change the status of application from "En revisión" to "Activa" or "Inactiva".
  - SA - Super Admin
- VA063 - Super Admin can check the information (submission documents) the automotive group send to validate.
  - SA - Super Admin

<!-- Screen to register automotive groups:

1. Section or form where they can create new automotive groups.
2. They will be created with random passwords. -->

**Priority**: High

**Estimate**: 1 week

---

---

## **US07 - Agency register**

As an automotive group I must be able to apply so I can begin operations within the application.

**Validation:**

- VA071 - Sign in page for Agency.
  - CR - Car Retails
- VA072 - The user can register into the platform by email or a google account.
  - CR - Car Retails
- VA073 - The user must have a secure password with at least 8 characters.
  - CR - Car Retails
- VA074 - The email and password must be stored in firebase.
  - CR - Car Retails
- VA075 - If at least one field is not valid, the user can not continue registering.
  - CR - Car Retails
- VA076 - The admin lands on the application page where they can submit their documents and wait for the super admin to validate.
  - CR - Car Retails
  - SA - Super Admin
- VA077 - If the super admin changes the status, the agency can see the comments made and the status of the application.
  - CR - Car Retails
  - SA - Super Admin
- VA078 - When the status of application is accepted the agency can access the whole page.
  - CR - Car Retails
  <!-- Screen to register automotive groups:

1. Section or form where they can create new automotive groups.
2. They will be created with random passwords. -->

**Priority**: High

**Estimate**: 1 week

---

---

## **US08 - Sellers register**

As a manager I want to be able to register sellers so they can make sales and contact customers within the application.

**Validation:**

- VA081 - Form where managers can register seller from their agency.
  - CR - Car Retails
- VA082 - Seller can log in with the password and email given by the agency.
  - CR - Car Retails

**Priority**: High

**Estimate**: 1 week

---

---

## **US09 - Cancel account**

As a user, I want to be able to cancel the creation of my account so that I do not have an account on a platform that I will not use and that contains my data.

**Validation:**

- VA091 - Cancel button deletes user account without storing any personal data in Firebase.
  - HP - Home Page
  <!-- When the user creates an account, he receives a confirmation email where he has the option to cancel the account creation in the same email, when canceling (with a hyperlink button) the request is canceled and the data is not stored.

1. Availability of cancel account button
2. Delete user account without storing any personal data in the database -->

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Could Have

---

---

## **US10 - Access without registration**

As a user, I want to access the page without registering to see the catalog and decide whether to use the platform to buy a car.

**Validation:**

- VA11 - User can move thru the page without registering.
  - AC - Auth Clients
- VA12 - When the user clicks a component that needs registering, redirects to register page.
  - AC - Auth Clients
  <!--
  The user accesses the page and can perform actions that do not require user verification.

1. The different models available with their characteristics, cost to the public, and agency are shown.
2. When you click on the account button, the account creation or login interface appears. -->

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US11 - Register payment info in agency**

As a customer I must be able to register a payment method. To be able to make transactions in the application and buy the vehicles.

**Validation:**

When selecting to pay in a car, I will have the option to choose between multiple payment methods through a simple click. This together with stripe will allow users to select their payment methods and do everything within the platform.

- V111 Be able to select from a variety of payment methods.
  - Py - Payments
- V112 Submit personal information in order to make the payment.
  - PY - Payments
- V113 A stripe component will be rendered to make the payment
  - PY - Payments
- V114 If successful, modify database. If an error occurs, show it to the user.
  - PY - Payments
  - DB - DataBase

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US12 - Register payment info**

As a car retailer I must enter data to which the funds of any purchase will arrive. So that the funds reach the desired account.

**Validation:**

- V121 Agency submits bank account details.
    - CR - Car Retailers
- V122 Save encrypted data in the database.
    - CR - Car Retailers
    - DB - Data Base

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US13 - Payment opportunities for clients**

As a user/buyer, I want to see the payment options and terms and conditions that each agency offers me to be able to make choices and finance according to my economic possibilities.

**Validation:**

- VA131 User can see the available finanicng options offered by the agency.
  - CD - Car Details
  - PY - Payments
- VA132 The options are dynamic (depending) on the down payment.
  - CD - Car Details
  - PY - Payments

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must have

---

---

## **US14 - Payments for custom order**

As a buyer, I want to have the option of customizing elements of my vehicle (as long as the model/agency allows it).

**Validation:**
- VA141 Display list of all available customizations.
- VA142 If a customization is not currently available gray out the button holding the option.
- VA143 A customized button is displayed on available vehicles.
- VA144 The user can view the customizable vehicles and customize them.

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Should Have

---

---

## **US15 - Download quotes or view**

As a user, I want to download vehicle quotes in PDF or have a space within my profile to view and analyze them and make the right decisions when buying a vehicle.

**Validation:**

- VA151 Display the "download" button near the displayed price of the car.
  -
- VA152 The quote is downloaded in the client's browser
  -

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Could have

---

---

## **US16 - Setting up financing plans**

As an agency, I want to be able to set up my financing and insurance plans (including rates and plans) to manage agency costs and monitor necessary changes according to the market.

**Validation:**
When a manager uploads a car, he will need to fill out a cost section where he can add fixed options that his agency has available, such as the different insurance plans, and financing options so that platform users can view them in their quotes.

1. VA161 A customizable forms that the manager can modify and add different financing options, insurance plans etc...
  - CR - Car Retailers
2. VA162 A submit button that will upload to the cars page the financing  and insurance options.
  - CR - Car Retailers

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US17 - Sales price display**

As a user, I want to see the price of sale to the public without having to register.

**Validation:**
When viewing vehicles in the catalog or in an overview on the main page (as featured or promoted models), the retail prices are displayed.

- VA171 Display of prices without prior registration or registration.
  - FR - Front Page Results
  - PY - Payments

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US18 - Vehicles quotation**

As a user, I want to quote a vehicle model and see what factors can increase the final cost of a model ().

**Validation:**
When selecting a specific vehicle, approximate expenses can be selected in the calculator (at the bottom of the page) to show an approximation of the final price, such as insurance, down payment and customization... 

- VA182 Show approximations depending on the chosen vehicle
  - CD - Car Details

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Could Have

---

---

## **US19 - Account movement notifications**

As a user/consumer, I want to receive notifications of operations (via email and/or sms) carried out on my account to be sure of my actions and that my account is not used by third parties.

**Verification**

- VA191 When a change operation is made within the account send notification
  - IM - In App Messaging
  
- VA192 When requesting a driving test send notification
  - IM - In App Messaging

- VA193 When requesting a quote send notification
  - IM - In App Messaging

- VA194 When trying to purchase a vehicle send a notification.
  - IM - In App Messaging

- VA195 Request a test drive and have a notice sent by email
  - IM - In App Messaging

- VA196 Confirm a vehicle purchase and have confirmation sent to the email
  - IM - In App Messaging

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US20 - Multi factor Authentication**

**As a** person with an agency account in the webpage **I want** to have double authentication **to be able** to have more security at preventing anyone else to access all my information.

**Verification**

- V201 Whenever someone with an account tries to log in, the system will ask for an authenticator code.
  - AC - Auth Clients
- V202 In case the information given is wrong, the system will not allow the user to access the account.
  - AC - Auth Clients
- V203 - The user can retry the login process as many times as he wants.
  - AC - Auth Clients

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US21 - Roles/Permissions Configurations**

**As a** super adim **I want** to limit the various actions the other accounts are able to do or modify (admin, manager, vendor, user) **to be able** to avoid any unwanted alteration both in the database, website visuals, users car purchase progress, etc.

**Verification**

- V211 Whenever a specific account tries to use actions exclusively allowed for other roles, that account will not be able to perform that actions.
  - AC - Auth Clients
- V212 When a user is denied access to a specific action, the system will display an unathenticated message in the appropiate page.
  - AC - Auth Clients

**Priority:** Very High

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US22 - Encryption REST**

**As a** super adim **I want** ensure that all the data stored inside our databases are correctly Encrypted as well as only able to be viewed by sepecific roles/user **to be able** to protect the privacy and all sensitive information that are required from clients during their car purchase process.

**Verification**

- V221 Whenever the systems recieves any information that is required to be stored in our Database, it has to be encrpyted so if by any chance an intruder manages to access the DB they will not be able to comprehend the information.

**Priority:** Very High

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US23 - Encryption in transit**

**As a** super admin **I want** to ensure that while the users is sending all the documents and sensitive infarmation will be correctly encrypted (https) **to be able** to gurarantee that no intruder who could intercept the messages could understand its meanings.

**Verification**

- V231 During the data transfer from the users to Movu Webpage, all information has to be sented by security protocols (HTTPS)

**Priority:** Very High

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US24 - Secure Payments**

**As a** super admin **I want** to ensure that all transactions made from the users are correctly secured and encrypted **to be able** to ensure that all payments will always succed.

**Verification**

- V241 The user will be able to perform a transaction with the certantty that the money will be correctly sent to the destintation without any probability of lost.

**Priority:** Very High

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US25 - Data Privacy**

**As a** **I want** **to be able**

**Verification**

**Priority:** Very High

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US25 - Web Security**

**As a\*\***I want\*\* **to be able**

**Verification**

- **Priority:** Very High

  **Estimate:** 1 week

  **Classification:** Must Have

---

---

## **US26 - Data Visualization SAD**

**As** a super admin **I want** to visualize the statistics of every car dealership that are in the application **to be able** to detect trends and patterns that would allow for future improvements, as well as detecting any suspicious activity.

**Validation:**

- V261 In the Super Admin Dashboard, there will be a section which contains some data Summaries from all the car dealerships.

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US27 - Users Re-engagement**

**As a** super admin **I want** to send notification to users that have not viisted the site after a long time **To be able** to recover theri interest in buying a car from the platform.

**Validation:**

- V271 After 2 weeks from inactivity, the system will send them a emial inviting them to check the new deals and cars at MOVU.

**Priority**: Low

**Estimate**: 1 week

**Classification:** Could Have

---

---

## **US28 - Commissions**

**As a** super admin **I want** charge a comision for every car registered by an agency **To be able** to make earnings that will allow me to profit from this app, as well as maintaining it.

**Validation:**

- V281 For every cas uploaded to the system, be from catalog upload or indiviudal, a percentage of a the car price should be given to NDS as part of comission.

**Priority**: Very High

**Estimate**: 2 weeks

**Classification:** Must Have

---

---

## **US29 - Data Visualization AD**

**As a** administrator (automotive agency) **I want** to obtain certain data summary from all my registered agencies **To be able** analyze their overall performance (cars sold, most purchased cars per agency).

**Validation:**

- V291 In the Admin Dashboard, the user will be able to visualize a data summary of all the agencies owned (number of sales per agency, most sold cars, etc)

**Priority**: Medium

**Estimate**: 2 weeks

**Classification:** Must Have

---

---

## **US30 - Authorization in Procedures**

**As** a manager **I want** to approve certain steps during the car purchase process **to be able** to have a better control on the various sales

**Validation:**

- In some specific steps during the car purchase process, in order to continue with the next steps it will be required that the manager approves the completion of the current one.
- If there is no approval from admin, the car purchase will not be able to continue

**Priority**: High

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US31 - Vendors Administration**

**As** a manager I want to administrate my vendors from the agency (CRUD) to be able to have an easy experience managing their accounts.

**Validation:**

Manger will be able to perform all CRUD actions (Create, Read, Update and Delete) on the the vendors that are inside their assigned agencies.
Once the manager performs this modifications, the DB of vendors should be updated.

**Priority:** High

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US32 - Data Visualization MG**

**As** a manager I want to visualize the most important data from my agency To be able to better understand how my vendors are performing, as well as the most viewed and sold cars.

**Validation:**

In the dashboard page, the manager will be able to view data summary of the vendors sells and current car purchase processes.
Additional, the data summary will include a summary of the most bought cars as well as the most viewed by users.

**Priority:** Medium

**Estimate:** 2 weeks

**Classification:** Must Have

---

---

## **US33- Agency Catalog**

As a manager I want manage the agency car catalog (CRUD) To be able have a better control on the vehicles offered to the customers.

**Validation:**

The manager will be able to upload the agency car catalog by either a csv with standard data, as well as adding them one by one.
Once the catalog has been added successfully, the manager can either edit current vehicles in the catalog or delete them.

**Priority:** High

**Estimate:** 3 weeks

**Classification:** Must Have

---

---

## **US34 - Data Visualization Vendor**

As a vendor I want to easily visualize my customers data summary To be able to easily observe patterns on my clients.

**Validation:**
In the vendor dashboard they will be able to observe a summary of different data from their clients, such as most bough car, customers current car purchase process, etc.

---

---

**Priority:** Low

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US35 - Sells status**

**As** a seller I want to know how many sales I have made and the status of each one (amount paid). To know the status of my clients.

**Validation:**

Sellers will be able to see all their sales on a dedicated screen and the status of those sales.

1. Cards for all sales associated with the vendor
2. All cards will have information about the sale and the current status of it.

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

---

---

## **US36 - Current Status on active Car Purchase**

**As** a vendor I want to be able to know the status of all my current active car purchases to be able to keep track on their current progresses, as well as knowing what approvals or requirements are missing on every one of them.

**Validation:**

In the Dasboard, the vendor will be able to view a section where all the current car purchased assigned to him is display.
When selecting a specific car purchase, the vendor will get all the information of that process, as well as its current status.

**Priority:** High

**Estimate:** 2 weeks

**Classification:** Must Have

---

---

## **US37 - Payment status**

As a customer I want to be able to know the status of my order and payment, if the car is being prepared, on the way, etc. To keep track of my purchase and security.

**Validation: **

After paying for the car, as a customer I will be able to see the status of my order on a screen. An approximate of when you will arrive at your house will be given.

1. Card with order information.
2. Information on the status of the order will be included.

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US38 - Modify personal information**

As a user want to modify my personal account information to be able to update any outdated information or create a new password.

**Validation: **

- The users will have a profile page section, where they are able to modify specific information of their profile (username, password, email, address)

- Once the user has made this updates, it should be reflected both in its profile section.

**Priority**: Medium

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US39 - Website access**

**As a** user **I want** to use the web page through my computer and my phone **to be able** to have different options to access.

**Validation:**

- Through a web browser the user must be able to access the website

**Priority**: Medium

**Estimate**: 2 week

**Classification:** Must Have

---

---

## **US40 - Website access**

**As a** **I want** **to be able**.

**Validation:**

- **Priority**: Medium

  **Estimate**: 2 week

  **Classification:** Must Have

---

---

## **US40 - NL Search**

**As a** user **I want** to search for cars without the need of filters or advanced details **to be able** to have a easy expierience in seraching my car.

**Validation:**

- VA401 - The landing page will have a search bar where the users will be able to write a simple car description which will then reutrn a list of vehicles that match that critiera. (Front Page Results)
- VA402 - The application must have a NL model that allows to interpret the input of user and send the correct request to the DB. (NLP E-Search)
- VA403 - The DB must be able to filter with the given information and return the list of cars that match the critiera. (Front Page Results)
- VA404 - The resulting "tokens" determined by the NL model will need to have at least 80% of accuracy on what the user intended so the result are coherent as posible but also provide a bit more of variety.(NLP E-Search)

- **Priority**: Very High

  **Estimate**: 2 week

  **Classification:** Must Have

---

---

## **US41 - Forms Search**

**As a** user **I want** guidance during my car search **To be able** to avoid the filters that can result confusing for user that lack car knowledge.

**Validation:**

- VA411 - In the Landing Page, the app will have a section "Search Guide" that once clicked it will ask the user various questions regarding the car being looked. (Front Page Results)
- VA412 - The answers of the user will be sent to the DB through an API (Front Page Results)
- VA000 - The DB should return the list of cars that allign to the filter back to the Webpage (Front Page Results)
- VA413 - The cars with that filter should be displayed to the user. (Front Page Results)

**Priority**: Low

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US42 - Filter Search**

**As a** user **I want** to utilize traditional filters **To be able** to select a car with the specific requirements that I want (model, price range, color, number of seats, etc)

**Validation:**

- VA421 - In the car display page, the users should be able to select specific filters which allow a more detailed result. (Front Page Results)
- VA422 - Once the specific fitlers are selected, the Webpage will send those parameters to the DB (Front Page Results)
- VA423 - The DB will obtain the cars that allign with the filters and then return them to the Webpage (Front Page Results)
- VA424 - The cars that with that filter should be displayed to the user. (Front Page Results)

**Priority**: Very High

**Estimate**: 1 week

**Classification:** Must Have

---

---

## **US43 - No login Search**

**As a** user **I want** to use the search feature even if I am not registered. **To be able** to see the cars I’m interested immediately.

**Validation:**

- VA431 - The user can use the NL search function without having an account ()
- VA432 - The user can use the formulaire search function without having an account ()
- VA433 - The user can use the basic filter search function of the app ()

- **Priority**: Very High

  **Estimate**: 1 week

  **Classification:** Must Have

---

---

## **US44 - NL Search Always Available**

**As a** user **I want** to always have access to the search bar car search. **To be able** to search cars whenever I want.

**Validation:**

- VA441 - The search bar is visible even when the user scrolls down the page (Home Page)
- VA442 - Whenever the user interacts to the search bar, they must allways obtain the car results. (Front Page Results)

- **Priority**: Low

  **Estimate**: 1 week

  **Classification:** Could Have

---

---

## **US45 - Car Visualization**

**As a** customer **I want** to see general information about the vehicle through cards **to be able** to get a brief overview of the vehicle without having to see each one in detail.

**Validation:**

- VA451 - For every car that is displayed, it must have general information before clicking the car for more details: (Front Page Results)

1. Images
2. Initial price
3. Basic characteristics (doors, capacity, color, etc).

- VA45 - If the user selects a specific car, they will be redirected to another section with all the description of the car (Car Details)

- **Priority**: Low

  **Estimate**: 1 week

  **Classification**:Should Have

---

---

## **US46 - Car characteristics comparison**

**As a** customer **I want**to compare the features of the cars I'm interested in **to be able to** buy the car that best suits my needs.

**Validation:**

- VA461 - While inspecting the vehicles, the user will be able to click a button that redirects them to a comparative section. (Car Details)
- VA462 - The webage will give the user the list of all available cars, in which they can select two cars to compare. (Front Page Results)
- VA464 - Once the cars are selected, the key car characteristicas will be placed side by side for better analysis. (Car Details)

- **Priority**: Low

  **Estimate**: 1 week

  **Classification**: Could Have

---

---

## **US47 - Indoor and outoor display**

**As a** user, **I want** to see the interior and exterior photographs in detail **to be able to** have a better visualization of the vehicle

**Validation:**

- VA471 - When the user selects a vehicle, they can go through the images provided by the agencies, to explore its structure both inside and outside in detail. (Car Details)
- VA472 - Inside the car details, the users will be able to view the vehicle 360º (Cars Details)

- **Priority:** Medium

  **Estimate:** 1 week

  **Classification:** Should Have

---

**US49 - Car shopping Wishlist**

**As a** user **I want** an online shopping cart **to be able** to have custom list of cars I might buy and save them for later.

**Validation**:

VA491 - When looking for a car there is going to be a "add to cart" button next to each car (both in card and description mode) where the user can add cars to a shopping cart page.(Home page)
VA492 - When accesing the shopping cart, all the cars previosly select need to appear in this section. (Home page)

- **Priority**: High

  **Estimate**: 2 week

  **Classification:** Must Have

---

---

## **US50 - Chat with Vendor**

**As** a user **I want** to have an easy communication between the agency vendors **to be able** to ask all my questions and follow ups on my current car purchase status.

**Validation:**

- VA501 - Once the user select a specific car for details, they will be able to click a chat button that will contact a vendor that matches the car agency that belongs the car.

- **Priority**: High

  **Estimate**: 3 weeks

  **Classification:** Must Have

---

---

## **US51 - Chat with Chatbot**

**As a** user **I want** to be able to begin a conversation with a chat bot **to be able** to obtain quick information and status of my current car purchase progress, as well as support to sign up for a test drive.

**Validation:**

- VA511 - At all times, the user can quickly begin a conversation with our chatbot, which will give the user the various questions that it can respond to.

- **Priority**: Medium

  **Estimate**: 3 weeks

  **Classification:** Should Have

---

---

## **US52 - Email Notifications**

**As a** user **I want**to receive email notification when any progress in my car purchase has been done **To be able** to quickly access the webpage for more details.

**Validation:**

- VA521 - Whenever a update on the users car purchase progress is done, they should be able to receive an email detailing the current status.

- **Priority**: Medium

  **Estimate**: 1 week

  **Classification:** Must Have

---

---

## **US53 - Chats Managements**

**As a** vendor **I want** to have an easy interface for administrating all my chat with clients **To be able** to better keep track on every conversation.

**Validation:**

- VA531 - In the Vendor Dashboard, the vendor will be able to visualize all it conversations with clients.
- VA532 - Once a conversation has ended, the vendor will be able to delete it from the dashboard and store it in archives.

- **Priority**: Medium

  **Estimate**: 2 weeks

  **Classification:** Should Have

---

---

## **US54 - Chats Recordings**

**As a** super **I want** to store every conversation generated in app **To be able** to rate customer experience and the vendors treatment towards clients.

**Validation:**

- VA541 - Once either a chat conversation or vendor chat has been conluded, it will be stored for both customer support review as well as any misuse of the tool.

- **Priority**: High

  **Estimate**: 1 week

  **Classification:** Must Have

---

---

## **US55 - Easy Test Drive Application**

**As a** user **I want** an easy and smooth process while scheduling a test drive **to be able to** quickly test the car before deciding to purchase it.

**Validation:**

- VA551 - In the user Dashboard, the user will be able to select an option to request a Test Drive
- VA552 - Once the user answers a form with specific information as well add sending its valid drive license, he will have to wait form the agency approval
- VA553 - Once its done, its dashboard will update with the test drive details.

- **Priority:** High

  **Estimate:** 2 weeks

  **Classification:** Must Have

---

---

## **US56 - Test Drive Requirements**

**As a** vendor **I want** to manage all the various test drive applications the users request **to be able to** have a better control of all the test drives required, as well as verifying the users information before accepting the test.

**Validation:**

- VA561 - In the vendor Dashboard, it will be a section specified to manage the test drives. Here the vendor can view the applications as well as approving or denying the test.

- **Priority:** High

  **Estimate:** 2 weeks

  **Classification:** Must Have

---

---

## **US57 - Skip Drive**

As a customer I can decide not to take a test drive. To jump directly to the purchase and streamline the process.

**Validation:**

- VA571 - The user should be able to continue with the car purchase process without schedulling any test drive.

- **Priority**: Medium

  **Estimate**: 1 week

  **Classification:** Must Have

---

---

## **US58 - Test Drive Docuemnts**

**As a** vendor **I want** users to upload all the required documents to take the driving test (INE, driver's license, etc.) **to be able to** ensuere that the person is allowed to drive.

**Validation:**

- VA581 - When requesting a vehicle test drive, the user will have to enter data required by the agency to achieve registration

1. Input to upload multiple files.
2. Include all files specified by that agency in the input.

- **Priority**: Medium

  **Estimate**: 1 week

  **Classification:** Must Have

---

---

## **US59 - Filter of Cars applicable for Test Drive**

**As a** user, **I want** to see a filter or section within the profile of an agency where the vehicles that are available for a test drive are available **to be able** to easily choose one.

**Validation:**
When a vehicle is uploaded to the platform, there is a box, "available for a test drive", when selected it is added to your inventory for test drive requests, customers can see which vehicle they can request at the selected agency (management view)

1.  When selecting an agency (by search or from a vehicle), a section is displayed where all the vehicles available for a test drive are listed.

- **Priority:** Medium

  **Estimate:** 1 week

  **Classification:** Should have

---

---

## **US60 - User Documentation Definitions**

**As a** admin **I want** to define which documentation is required in order for a user to buy a car from my agencies **to be able** to standarize all the procedures in all of my agencies and ensure that the users are applicable for the purchase.

**Validation:**

- In admin dasboard there will be an option to define which documents are required for every step during the car purchas process.
- **Priority:** High

  **Estimate:** 2 weeks

  **Classification:** Must have

---

---

## **US61 - Vendor Documentation Approvals**

**As a** VENDOR **I want** to approve or deny the various docuemnts that the user will be uploading during the car purchase procceudre **to be able** valdiate the corresponding docuemnts before advancing to any future steps.

---

---

## **US62 - Automotive Groups Documentation Application Approvals**

**As a** super admin **I want** to have the ability to view the various automotive group applications and either approve or reject them from the application it the documentation is not valid.

**Validation:**

- In the super admin Dashboard, the super admin will have a section in which they can validate or reject new Automotive Groups Applications.

- **Priority:** High

  **Estimate:** 2 weeks

  **Classification:** Must have

## **US63 - Displaying the available financing plans inputed by the car retailer**

As a user/buyer I want to be able to see which financing and insurance plans are available to me. 

**Validation:**

1. VA631 A list of different insurance options with the price of each of the options will be displayed in the car details page. 
  - CD - Car Details
2. VA632 A list of different financing options with the price of each of the options will be displayed in the car details page. 
  - CD - Car Details

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Must Have

---
---

## **US64 - Dynamic Pricing**

As a user/buyer, I want to be able to see the effects on the price when adding car customizations and/or choosing differents financing and/or insuarance options.

**Validation:**
- VA641 Reflect changes on the final price when selecting extras, such as car customizations and financing/insurance options. 
  - CD - Car Details

**Priority:** Medium

**Estimate:** 1 week

**Classification:** Should Have

---
---