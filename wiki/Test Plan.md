# Test Plan

Created: March 6, 2023 5:25 PM
Last edited time: March 15, 2023 7:23 PM
Tags: document# Document Information

# Table of Contents

- [Test Plan](#test-plan)
- [Table of Contents](#table-of-contents)
  - [Team](#team)
- [Revision and Sign Off Sheet](#revision-and-sign-off-sheet)
  - [Document History](#document-history)
  - [Approvers Lists](#approvers-lists)
    - [Reference Documents](#reference-documents)
- [1. Introduction](#1-introduction)
  - [1.1 Purpose](#11-purpose)
  - [1.2 Project Overview](#12-project-overview)
  - [1.3 Audience](#13-audience)
- [2. Test strategy](#2-test-strategy)
  - [2.1 Test Description](#21-test-description)
    - [2.2.1 Dynamic tests:](#221-dynamic-tests)
    - [2.2.2 Static tests:](#222-static-tests)
  - [2.2 Test Objectives](#22-test-objectives)
  - [2.3 Test Assumptions](#23-test-assumptions)
    - [2.3.1 Key assumptions](#231-key-assumptions)
    - [2.3.2 General](#232-general)
  - [2.4 Test Objects](#24-test-objects)
  - [2.5 Scope](#25-scope)
    - [2.5.1 User authentication](#251-user-authentication)
    - [2.5.2 Role management](#252-role-management)
    - [2.5.3 Search feature](#253-search-feature)
    - [2.5.4 Consumer Dashboard](#254-consumer-dashboard)
    - [2.5.5 Admin Dashboard](#255-admin-dashboard)
    - [2.5.6 Car and dealership upload](#256-car-and-dealership-upload)
    - [2.5.7 Payments](#257-payments)
    - [2.5.8 Data Visualization](#258-data-visualization)
  - [2.6 Test acceptance criteria](#26-test-acceptance-criteria)
    - [2.6.1 Unit testing](#261-unit-testing)
    - [2.6.2 Integration testing](#262-integration-testing)
    - [2.6.3 End to end testing (validation test)](#263-end-to-end-testing-validation-test)
  - [2.7 Test Deliverables](#27-test-deliverables)
  - [2.8 Milestone List](#28-milestone-list)
  - [2.9 Test Effort Estimate](#29-test-effort-estimate)
- [3. Execution strategy](#3-execution-strategy)
  - [3.1 Entry and Exit Criteria](#31-entry-and-exit-criteria)
- [4. Test Management Process](#4-test-management-process)
  - [4.1 Test Execution Process](#41-test-execution-process)
  - [4.2 Test Risks and Mitigation Factors](#42-test-risks-and-mitigation-factors)
  - [4.3 Communications Plan and Team Roster](#43-communications-plan-and-team-roster)
    - [4.3.1 Role Expectations](#431-role-expectations)
    - [4.3.2 Project Management](#432-project-management)
    - [4.3.3 Activities Schedule](#433-activities-schedule)
- [5. Test Environment](#5-test-environment)
- [6. Tests](#6-tests)
- [7. Conclusion](#7-conclusion)

**Version**: 0.0.1

**Status:** DRAFT

### Team

Pablo Rocha Ojeda

Miguel Arriaga Velasco

Jacobo Soffer Levy

# Revision and Sign Off Sheet

## Document History

| Version | Date       | Author                                                                        | Description of Change                      |
| ------- | ---------- | ----------------------------------------------------------------------------- | ------------------------------------------ |
| 0.0.1   | 06/03/2023 | Pablo Rocha, Miguel Arriaga, Jacobo Soffer                                    | Initial Commit: Structure and introduction |
| 0.0.2   | 08/03/2023 | Salvador Salgado                                                              | Test Strategy                              |
| 0.0.3   | 13/03/2023 | Pablo Rocha, Miguel Arriaga, Jacobo Soffer, Salvador Salgado, Stephan Guingor | Execution strategy and corrections         |
| 0.1.0   | 30/03/2023 | Miguel Arriaga, Diego Araque, Manuel Barreda, Juan Munian                     | Test plans merging                         |

## Approvers Lists

| Name                    | Role             | Status                     | Approval Date   | Signature |
| ----------------------- | ---------------- | -------------------------- | --------------- | --------- |
| Gilberto Echeverria     |                  |                            |                 |           |
| Esteban Castillo Juarez | Testing reviewer | Reviewed, gave us pointers | @March 13, 2023 |           |
| Eduardo Rubinstein      |                  |                            |                 |           |
| Ivan Santiago           |                  |                            |                 |           |

### Reference Documents

| Version | Date           | Document                                                                                                               |
| ------- | -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| v2      | @March 3, 2023 | [Functional Requirements ](https://github.com/IvanDLar/MOVU-Docs/blob/main/wiki/Functional%20requirements.md)          |
| v2      | @March 3, 2023 | [Non Functional Requirements](https://github.com/IvanDLar/MOVU-Docs/blob/main/wiki/Non%20Functional%20requirements.md) |

# 1. Introduction

## 1.1 Purpose

The purpose of the testing document is to outline the various tests that will be conducted to ensure the software is working as intended. This document provides a comprehensive overview of the software testing process, including the test plan, test cases, and expected results. The document will ensure that all aspects of the software are thoroughly tested and that any potential defects are identified and corrected before release. Additionally, it will serve as a reference guide for future testing and development, providing valuable insights and information for developers and testers to use in future projects.

In particular it will include:

- This is a test plan for a project that aims to create a website for purchasing cars online.
- The document outlines the purpose of the testing, the project overview, and the intended audience.
- The test strategy includes informal and black-box testing, as well as unit, integration, and end-to-end testing.
- The document lists the test objectives, assumptions, and acceptance criteria for unit, integration, and end-to-end testing.
- The functional requirements that will be tested include user authentication, role management, search feature, consumer dashboard, admin dashboard, car and dealership upload, payments, and data visualization.

## 1.2 Project Overview

The project aims to create a website that offers customers the ability to purchase a car entirely online. The website will feature a range of services, including searching for vehicles, making payments, communicating with sellers and dealerships, scheduling test drives, uploading documents, and more.

The project will also include an admin interface. This will allow automobile groups to register in the page, add their different dealerships and corresponding managers. Managers will be able to define the salesmen. From there the salesman and end user will be able to interact.

## 1.3 Audience

This document will serve as a comprehensive guide for team members to ensure that everyone is on the same page regarding the testing requirements for our project. It will be accessible to members of other teams, including approvers who will review and provide feedback on the document. The SCRUM master will rely on the document to plan the sprints in which the testing will occur and ensure that the testing is completed within the established deadlines.

Additionally, the document will be an integral part of our wiki, providing clients with the opportunity to review the testing requirements and ensure that they are being satisfactorily met. The document will contain detailed instructions that developers must follow to write tests or perform manual tests effectively. By using this document, we can ensure that all testing is done uniformly across the entire project, resulting in a higher quality final product.

In summary:

- This document will be written by team members for them to use, including members of other teams in case that our project gets selected to use for the entire class.
- The approvers will also be able to read and review this document, indicating in case of any comments or areas of opportunities.
- The SCRUM master will use this document to plan the sprints in which the testing will occur, ensuring that the deadlines for the testing are met.
- The SCRUM master will also use this documents to comply with the static tests.
- This document will also be part of our wiki, in case that the clients and stakeholders want to review the document and make sure that the testing requirements are being satisfied.
- The developers must use this document in order to write dynamic tests (unit tests) or perform manual tests as it is indicated in this document.
- The static tests will be conducted by the management team: the project management and SCRUM master.

# 2. Test strategy

## 2.1 Test Description

### 2.2.1 Dynamic tests:

**Informal tests**

| Purpose                                                                                                                    | SCOPE                                                     | TESTERS                      | METHOD                                                                | TIMING      |
| -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------- | --------------------------------------------------------------------- | ----------- |
| Informal tests will be used as part of “test driven development”, in which each developer will informally test their code. | Directly in the code: functions, classes, endpoints, etc. | Every developer of the team. | Informal tests will be based on pieces of code written by developers. | When coding |

**Unit testing**

| Purpose                                                                                                             | SCOPE                                                                                                          | TESTERS                                                         | METHOD                                                                                                                                                                            | TIMING                                                     |
| ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| To comprehensively test each section of the software and determine whether the software satisfies the requirements. | Unit testing will be conducted on all important sections (priority Medium or High in functional requirements). | The testing team will be responsible for conducting unit tests. | The unit testing process will employ user stories, use cases, and input-output sections. In the event that the testing results in failure, white box testing will be implemented. | Unit testing will be conducted at the start of each cycle. |

**Integration testing**

| Purpose                                                                                                                                                                  | SCOPE                                                                  | TESTERS                                                                         | METHOD                                                                                                                                                                                                    | TIMING                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integration testing will allow us to verify different components in the system work together as intended. This includes third party systems such as a payment processor. | Main component interactions (Priority High in functional requirements) | Testing team, preferably one developer for each component that is being tested. | Integration testing will draw on user stories and functional requirements. In case of failure white box testing will be used, extending to the individual components being tested if needed and possible. | Integration testing will be conducted after two or more components are integrated, the components involved change their public interfaces or at the end of each cycle. |

**End to end testing**

| Purpose                                                                                                 | SCOPE                                    | TESTERS                                                                                                      | METHOD                                                                                                                                                                    | TIMING                                                |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| E2E tests will allow us to ensure the platform is working as expected from the point of view of a user. | Main user interactions with the platform | Testing team would be in charge of creating integration tests, ideally the team responsible for each system. | E2E testing will be based on main user stories from each service. This will be a type of black box testing where we only care about user actions and the expected output. | When completing the service E2E tests will be created |

### 2.2.2 Static tests:

**Route:**

| Purpose                                              | SCOPE                                          | TESTERS                        | METHOD                                                                                | TIMING                      |
| ---------------------------------------------------- | ---------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------- | --------------------------- |
| Document that indicates the flow of the application. | The UI functionalities of the web application. | Project manager / SCRUM master | Diagrams will be made at the end of each feature as well as at the end of development | At the end of each feature. |

**Api documentation:**

| Purpose                                                                                                       | SCOPE              | TESTERS          | METHOD                                                   | TIMING                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------ | ---------------- | -------------------------------------------------------- | ------------------------ |
| Evaluate the product by checking its conformance to the development standards, guidelines and specifications. | All API endpoints. | Backend testers. | It will be created with a reliable tool such as swagger. | All the time in backend. |

**User manual:**

| Purpose                                                                                             | SCOPE                                                                                            | TESTERS                         | METHOD                                                                          | TIMING                                                                                     |
| --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Provide an installation and usage manual in order for the users and clients to use the application. | The manual will cover the installation and use of the UI functionalities of the web application. | Project manager / SCRUM Master. | The project manager will create a user manual with the help of some developers. | Before every important deployment with the final version once the application is finished. |

Taking into account the project deadline and complexity of the project the team has decided to create a strategy that focuses on black-box testing and informal testing. Test will only be ran in functional requirements.

This was decides as black-box testing is particularly useful when there is limited time for testing. By focusing on black-box testing and informal testing, the team can will identify any major issues or bugs in the system without spending too much time on testing.

On the other hand as is it is a complex project with many modules, it may be difficult to test each component in isolation. In this case, black-box testing can help the team identify any issues with the system as a whole, rather than focusing on individual components. Similarly, informal testing can help the team get a better understanding of how the system behaves in the real world, which may not be apparent through more formal testing methods.

Finally as we will be working in big team black-box and informal testing will allow all developers to create tests for any part of the system as they will not need to know all the insides of the code.

We will mainly focus on un unit, integration and some end to end testing. This will ensure that the system is thoroughly tested at all levels. By testing each component in isolation, as well as how different components work together and the system as a whole, the team can identify and address any issues or bugs early in the development process, before they become more difficult and costly to fix.

## 2.2 Test Objectives

The goal of testing is to ensure that the functional and non-functional requirements of the web application are being met. As well as ensuring that the application is stable, bug-free, scalable and fast.

Some of the requirements that we will be testing are the following:

- The clients are able to make their payments online to the agency, using existing payment services: Stripe
- The client is able to select from a variety of payment types: Down payment, Financing, Upfront payment
- Car dealership can perform CRUD operations on cars through admin dashboard
- The salesman is able to manage driving tests for users.
- The manager of a car agency can define the payment plans that they offer.
- The user will be able to create and use their credentials to log in to the app.

The complete list of requirements can be found in:

- [Functional Requirements](https://github.com/IvanDLar/MOVU-Docs/blob/main/wiki/Non%20Functional%20requirements.md)
- [Non Functional Requirements](https://github.com/IvanDLar/MOVU-Docs/blob/main/wiki/Non%20Functional%20requirements.md)

## 2.3 Test Assumptions

### 2.3.1 Key assumptions

1.  Software is being run on a compatible environment with all dependencies installed.
2.  All tests are being run on the same environment.
3.  Due to time and budget constraints, only functional tests will be performed.
4.  Black box tests will be performed first.
5.  For the same inputs, the tests should always produce the same outputs.
6.  White box testing will be reserved as a fallback option in case the black box tests fail.
7.  Test and their results will be documented.
8.  Tests will be a collaborative effort between developers, development leads and project manager.
9.  The project manager will review all tests deliverables.

### 2.3.2 General

1. Most of the testing will be used for the functional requirements
2. Every test should always return the same outcome
3. All critical priority functionalities need to be tested
4. It is important to follow the step-by-step testing for every function (informal testing, black box testing, integration testing)
5. Every test will require documentation
6. All test must have all the inputs necessary to ensure it is working correctly as well as the outputs expected.
7. For every test there must a standard template that allows better structure.
8. In order to conclude a test it has to be approved by PM.
9. Before the test execution, the Business Analyst has to review and approve the test cases.

## 2.4 Test Objects

1. Test the login
2. Test the signup
3. Test the search
4. Test role assignment
5. Test car uploads
6. Test the payment
7. Test the costumer dashboard view
8. Test the agency dashboard view

## 2.5 Scope

The web functionality that will be tested includes:

- User authentication
- Role management
- Search feature
- Consumer Dashboard
- Admin Dashboard
- Car and dealership upload
- Payments
- Data Visualization

### 2.5.1 User authentication

- Users are able to log in through the UI:
  - If the right credentials are entered, they will be redirected to the home page or previous page.
  - If the wrong credentials are entered, an error message alerts the user of their mistake.
- Users are able to access the backend and retrieve information (if they have permission) using their access token:
  - Access tokens have enough information to identify and authorize any given user.
  - The backend recognizes access tokens.
  - Expired or invalid access tokens are rejected.
  - Revoked refresh tokens are rejected.
  - Users can fetch a fresh access token through their refresh token.
  - Unauthenticated users are rejected.
  - Requests from users with missing permissions are rejected

### 2.5.2 Role management

- Admin users are able to assign roles to other users through the UI
  - There is a list of roles that can be selected to assign the user
  - Only one role can be assigned at a time
  - Any user should always have a role assigned
  - Roles are scoped to a tenant

### 2.5.3 Search feature

- Natural Language Search:
  - Key terms can be extracted from a prompt, mainly filters compatible with the search system such as make, model, seats, colors, year, type of car, etc. [Link to full list when available].
  - Full text search will be applied for some fields, observations, descriptions, etc
- Users can share a url containing the applied filters
  - If user reloads the url it should not change
- Users can modify the search results by applying filters.
- As the user scrolls down results are paginated
- A search known to yield results will always yield results.
- Search results are ranked through a score based on relevance.
- If no results are found, the user is presented with a helpful error message / related searches.

### 2.5.4 Consumer Dashboard

- Consumers are able to observe all their current purchasing status in their Dashboard
- They will be able to select any of them and inspect more details (Driving Test Date, Procede to payment, current document status)
- In case the purchasing status is yet to be payed, a consumer will be able to cancel the process.
- In case the user is not a Consumer, this information will not be displayed

### 2.5.5 Admin Dashboard

- Admin will be able to visualize information depending on their role in the system (current deals processes, agency sales, vendors information, etc)
- Admin will be able to analyze the data shown for a better review
- If the user is not an admin, there will have a completely different dashboard

### 2.5.6 Car and dealership upload

- A automobile group owner is able to register a new dealership
  - Dealership data can be added
  - Dealerships documents can be uploaded
  - The automobile group owner can add a dealership manager
  - The automobile group owner can NOT add a dealership to another group
  - With incorrect information dealership is not added
- A salesman or dealership manager is able to manage dealership cars
  - The car data can be added
  - Car add-ons can be added
  - Car spec sheet can be added
  - Car can be removed
  - Car data can be edited
  - With incorrect data car ca not be added

### 2.5.7 Payments

- A user is able to pay to the agency through the UI
  - If payment succeeds/fails user should receive a notification
  - User can select their payment method
  - User can save their preferred payment method

### 2.5.8 Data Visualization

- Agency Users are able view graphs of how much each vendor is selling
- Agency Users are able to view a graph with MRR, expected MRR for next month

## 2.6 Test acceptance criteria

### 2.6.1 Unit testing

**Authentication**

Front:

- Emails and passwords should be validated before being sent to the server.
- During a loading state, the user should not be able to modify their input.
- If a success response is received:
  - If the user was on a page before logging in, the user should be redirected to said page.
  - Else, the user should be redirected to the homepage.
  - In all cases the authentication token should be stored in a cookie to be retrieved when needed.
- If an error response is received:
  - A clear error message should be displayed to inform the user.

Back:

- The backend should recognize access tokens in requests:
  - It can validate that the token is valid.
    - If the token is valid it should be stored in a request context.
    - Else the request should be aborted.
  - It can identify the user id and role from the token, if it can’t the token is invalid.
  - If the token is expired it is treated as an invalid token.
  - It authorizes requests depending on the user’s role.
- If a token is missing on a protected route the request is aborted immediately.
- Users can request a fresh authentication token using a refresh token
  - If a refresh token is expired, the request is aborted.
  - If a refresh token is revoked the request is aborted.
- Users can invalidate their refresh tokens (in case of a sign out/password change).

**Role and User Management**

Front and Back (tested in isolation):

- Managers can list the users in their dealership.
- Managers can add users to their dealership tenant.
- Managers can delete users from their dealership tenant.
- Managers assign roles to users and can only assign one of the roles recognized by the system.
- Every user must have one and only one role assigned.
- Roles are scoped to a tenant.

Front End only

- In case of a success response to any request a success message is displayed and the interface accordingly.
- In case of an error response to any request an error message is displayed.

**Search Functionality**

- Users can see and apply filters from the UI.
- If no results are found, the user is presented with a helpful error message / related searches.

### 2.6.2 Integration testing

**Authentication**

- The frontend can reach the backend and obtain a token.
- If invalid credentials are provided, the backend returns an error.

**Payments functionality:**

- At the end of the month the user should receive an email with the total usage, it should be automatically charged to the preferred method
- Track usage of created listings in stripe
- Transferring money to destination account from user, and getting a commission to NDS account.

**Search functionality:**

- When creating a new listing data should be available in elastic search, we then should be able to use the search service to view it.
- Do a natural language search from the frontend and see extracted keywords in the frontend as well as relevant results
- User can pay to have priority in the search system, and when searching have the listing at the top

**Chat functionality:**

- Users can send a message through a chat interface in the frontend, and an agent from the agency should be able to reply through the admin dashboard. Only vendors are able to use the chat system to reply.

**Admin Dashboard:**

- Salesmen should only be able to create new cars, car variants and new listings
- Admins should be able to create agencies
- Managers should not be able to see other agencies

**Metrics System:**

- Depending on a role you can see different metrics
- Logs are being generated after creating a subscription

**Devops:**

- After a merge to production lambdas are deployed to cloud environment, using terraform

### 2.6.3 End to end testing (validation test)

**Admin Dashboard:**

- Admins are able to change the role of a user.
- The change is reflected immediately for the user.

**Chat**

- Users can start a chat session and send messages.
- Salesmen are able to see the messages and reply.
- The reply is seen immediately on the user side.

**Payments**

- Admins are able to register a bank account through Stripe.
- Admins are able to visualize their payments through the Stripe portal.
- Users are able to complete a purchase and this is:
  - Reflected in our systems upon payment completion.
  - The money is deposited to the dealer account immediately.

## 2.7 Test Deliverables

| No. |            Name             |  Author   |         Reviewer         |
| :-: | :-------------------------: | :-------: | :----------------------: |
|  1  |          Test Plan          | Test Team |     Esteban Castillo     |
|  2  |       Unit Test Cases       | Test Team |        Test Lead         |
|  3  | Recurrent Integration Tests | Test Team | Esteban Castillo, Felipe |
|  4  |     Recurrent E2E Test      | Test Team | Esteban Castillo, Felipe |
|  5  | Example of successful tests | Test Team | Esteban Castillo, Felipe |
|  6  |         Test report         | Test Lead |     Project Manager      |

## 2.8 Milestone List

|     |      Test Type      |          Test Example (SUT)          |                                          Dependency (DOC)                                          |
| :-: | :-----------------: | :----------------------------------: | :------------------------------------------------------------------------------------------------: |
|  1  |    Unit testing     |      Login functionality test.       |                      Login front end page, login endpoint, database created.                       |
|  2  |    Unit testing     |       Buy a car functionality        |                    Buy a car endpoint, database, interface, stripe integration.                    |
|  3  |    Unit testing     |             Search test              |                            Elastic setup for search, database, filters                             |
|  4  | Integration testing |     Backend connection to stripe     |                                Database created, buy a car endpoint                                |
|  5  | Integration testing |        Natural language test         | ChatGPT integration with backend, database created, search functionality done, database populated. |
|  6  | End to end testing  | UI test from production environment. |          Users will test the applications functionalities from a production environment.           |

## 2.9 Test Effort Estimate

| Num. |                                                       Main functionality                                                       | Black box minutes | White box minutes (ideally not performed) |
| :--: | :----------------------------------------------------------------------------------------------------------------------------: | :---------------: | :---------------------------------------: |
|  1   | Authentication. Fulfill requirements: REQ*FUN*[002], REQ*FUN*[032], REQ*FUN*[033], REQ*FUN*[046], REQ*FUN*[047], REQ*FUN*[048] |        220        |                    440                    |
|  2   |                                                        Role management                                                         |        150        |                    300                    |
|  3   |                                                             Search                                                             |        310        |                    620                    |
|  4   |                                                       Consumer Dashboard                                                       |        100        |                    200                    |
|  5   |                                                        Admin Dashboard                                                         |        100        |                    200                    |
|  6   |                                                         Car management                                                         |        130        |                    260                    |
|  7   |                                                     Payments and purchases                                                     |        200        |                    400                    |
|  8   |                                                 Metrics and data visualization                                                 |        200        |                    400                    |
|      |                                                             Total                                                              |       1,410       |                   2,820                   |
|      |                                                    Other testing activities                                                    |                   |                                           |
|  9   |                                                       Test plan creation                                                       |       2,400       |                   4,800                   |
|  10  |                                                         Formal Review                                                          |        210        |                    420                    |
|  11  |                                                           Inspection                                                           |        220        |                    440                    |
|      |                                                             Total                                                              |       2,830       |                   5,660                   |
|      |                                                          Global total                                                          |       4,240       |                   8,480                   |

# 3. Execution strategy

## 3.1 Entry and Exit Criteria

1. The entry criteria are the desirable conditions that should be met before starting test execution. At the end of each cycle, only the code migration and fixes need to be assessed.
2. The exit criteria are the desirable conditions that should be met in order to proceed with implementation.
3. Entry and exit criteria are flexible benchmarks, subject to assessment by the test team if they are not met. The team will then identify mitigation actions and provide a recommendation. All of this information will be input to the project manager for a final "go-no go" decision.
4. To start the execution phase of testing, all activities listed in the Test Planning section of the schedule must be 100% completed.
5. To start each cycle, all activities listed in the Test Execution section of the schedule must be 100% completed.

| Exit Criteria                                                                                   | Test Team | Technical Team | Notes |
| ----------------------------------------------------------------------------------------------- | --------- | -------------- | ----- |
| 100% Test Scripts executed                                                                      |           |                |       |
| 95% pass rate of Test Scripts                                                                   |           |                |       |
| No open Critical and High severity defects                                                      |           |                |       |
| 95% of Medium severity defects have been closed                                                 |           |                |       |
| All remaining defects are either canceled or documented as Change Requests for a future release |           |                |       |
| All expected and actual results are captured and documented with the test script                |           |                |       |

# 4. Test Management Process

## 4.1 Test Execution Process

![Execution diagram](/wiki/Test%20Plan/Testing-Flow-Diagram.png)

## 4.2 Test Risks and Mitigation Factors

| Risk                                                                                                               | Probability | Impact | Mitigation Plan                                                                             |
| ------------------------------------------------------------------------------------------------------------------ | ----------- | ------ | ------------------------------------------------------------------------------------------- |
| Third party service being tested goes down                                                                         | Low         | Medium | Write unit tests that test the functionality without relying on the third party             |
| Low black test coverage                                                                                            | Low         | High   | Add checks in the repo that do not allow PRs to be merged if they have low test coverage    |
| Skipping review process for tests                                                                                  | Low         | Medium | Ensure the project manager enforces these reviews.                                          |
| Not running white box testing appropriately                                                                        | Medium      | Medium | Enforce peer reviews for tests and test results.                                            |
| Testing CI pipeline crashes due to volume of commits or other external factors.                                    | Low         | Medium | Run tests by hand                                                                           |
| Bias induced in tests                                                                                              | Low         | Medium | Write tests before code, write tests with other developers, do test reviews.                |
| Tests taking too long to run. Specially integration or E2E tests that require network requests that might timeout. | High        | Medium | Run some tests ( Integration and E2E) as a cron job so it doesn't block developer workflow. |

## 4.3 Communications Plan and Team Roster

### 4.3.1 Role Expectations

| No. | Role               | Description                                                                                                                                                                                                                                                                                                     |
| --- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Project Manager    | The person responsible for leading and managing a project from start to finish. They plan, organize, monitor, and control all aspects of the project to ensure it meets its goals and objectives.                                                                                                               |
| 2   | Architect Lead     | The person responsible for designing the overall structure and organization of a software system or application. They identify the key components and interactions needed to achieve the desired functionality and ensure the system is scalable, maintainable, and meets the requirements of the stakeholders. |
| 3   | Backend Lead       | The person responsible for leading the development and maintenance of the backend system of a software application. They work closely with the Architect Lead to ensure the backend system is designed to meet the needs of the application, and oversee the backend developers who implement the design.       |
| 4   | Frontend Lead      | The person responsible for leading the development and maintenance of the frontend system of a software application. They work closely with the Architect Lead to ensure the frontend system is designed to meet the needs of the application, and oversee the frontend developers who implement the design.    |
| 5   | Backend Developer  | A software developer who specializes in implementing the server-side logic, data storage, and APIs that enable the frontend to communicate with the backend. They ensure the backend system is performant, reliable, and scalable.                                                                              |
| 6   | Frontend Developer | A software developer who specializes in implementing the user interface and client-side logic of a software application. They write code in programming languages such as HTML, CSS, and JavaScript, and ensure the frontend system is responsive, accessible, and user-friendly.                               |
| 7   | Test Lead          | The person responsible for managing the testing process of a software application. They work with the Project Manager and other leads to plan and organize the testing effort, and oversee the testing team to ensure the application is thoroughly tested and meets the quality standards.                     |
| 8   | Test Developer     | A software developer who specializes in writing automated tests for a software application. They write code in testing frameworks and ensure the application is thoroughly tested and free of bugs. They work closely with the Test Lead to plan and execute the testing effort.                                |

### 4.3.2 Project Management

The project manager and tech leads should review the test plan, strategy and estimates and sign off on it. The project manager and the tech lead should also be responsible for enforcing reviews and the testing strategy. Additionally, the project manager should be involved in formal reviews. The tech lead will also be included in this meetings, since he will have a better technical understanding of all the differents tests of their area.

### 4.3.3 Activities Schedule

![Untitled](/wiki/Test%20Plan/Untitled.png)

[Activities Schedule](https://docs.google.com/spreadsheets/d/1Ufw-DndqkXT1jG2fCXSPx_80Q-OTM8Ir/edit?usp=sharing&ouid=105313523088712462882&rtpof=true&sd=true)

# 5. Test Environment

Unit Tests:

- Upon PR creation an automatic pipeline will be in charge of running github actions that run different tests, this will be done for specific requirements.

E2E:

- We will run run github actions for specific requirements with an automatic pipeline.

Integration Tests:

- We will run run github actions for specific requirements with an automatic pipeline.

Tools:

- For unit tests, integration tests and E2E we will use cypress to tests all our requirements
- If we have time, we will use locust for performance tests.
- We will make use of Cypress Docker Images for running E2E and component tests in different browsers, such as Chrome and Firefox, by specifying container and browser attributes within the Github Actions .yml.

# 6. Tests

This section will be completed in the following sprints.

**Dynamic testing template:**

**6.1 Integration test case I1**

| Test Case Identifier | I1T1                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Test Item(s)         | Login Functionality                                                                                                                                                                                                                                     |
| Input Specification  | I1. Enter valid username and password. I2. Enter invalid credentials. I3. Leave field blanks.                                                                                                                                                           |
| Output Specification | O1. User will log in successfully and enter main dashboard. O2. Error message will appear indicating that the information is wrong, without specifying which was incorrect. O3. The field blanks will mark a message requiring the missing information. |
| Environmental Needs  | 1.1 A functional web browser. 1.2 A valid account to test functionality. 1.3 Internet connection.                                                                                                                                                       |

**Route testing template:**

**6.1 Integration test case I1**

| Test Case Identifier | R1T1                                                                                              | Confirmed |
| -------------------- | ------------------------------------------------------------------------------------------------- | --------- |
| Test Item(s)         | Payment Functionality                                                                             | ✅        |
| Test step 1          | 1. Select a car                                                                                   | ✅        |
| Test step 2          | 2. Select car configuration                                                                       | ✅        |
| Test step 3          | 3. Select payment                                                                                 | ✅        |
| Test step 4          | 4. Checkout through stripe                                                                        | ✅        |
| Environmental Needs  | 1.1 A functional web browser. 1.2 A valid account to test functionality. 1.3 Internet connection. |           |

# 7. Conclusion

Testing is an important part of any commercial project, and this test plan will greatly help deliver a quality product that’s able to compete in an international market. The tests detailed in this document will be implemented continuously through the development of this project, while adhering to our test plan and other strategies such as reviews. This will greatly minimize risks during project development, ensure we maintain and deliver a quality codebase and guarantee we deliver a best in class experience to our users, without bugs and adhering to our project plan and requirements.

The process of testing is an integral component of any commercial project, as it ensures that the final product is of high quality and able to successfully compete in the international market. To this end, the development team has prepared a comprehensive test plan that will serve as a guide throughout the project's lifecycle.

It is essential to note that the testing procedures detailed in this document will be implemented consistently and continuously during the development of the project. The team will adhere strictly to the guidelines outlined in the test plan and other complementary strategies, such as reviews, to minimize any risks that may arise during project development. This approach will ensure that the codebase is of high quality and that the final product delivers a best-in-class experience to users, devoid of bugs and in full adherence to the project's plan and requirements.

By following the test plan meticulously, the development team can confidently assure stakeholders that the final product will be of the highest quality, meeting all of their requirements and expectations. The continuous testing process, in tandem with our adherence to the test plan and other complementary strategies, will facilitate a seamless development process, ensuring that the final product is delivered on time and with the highest level of quality.

In summary, the development team recognizes the importance of testing in the overall success of the project, and is committed to implementing the test plan comprehensively to deliver a product that is of the highest quality and meets all project requirements.
