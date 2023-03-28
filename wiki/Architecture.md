# Architecture

Created: February 27, 2023 4:34 PM
Last edited time: March 9, 2023 9:47 PM
Tags: document

## Architecture first iteration

The first iteration of the diagram, which evolved into the second iteration.

First iteration link: [https://app.cloudcraft.co/view/930d39e6-a3d9-421d-aecf-05c7307facab?key=e6e37a49-c425-4d10-81cc-e2bed02ecad4&interactive=true&embed=true](https://app.cloudcraft.co/view/930d39e6-a3d9-421d-aecf-05c7307facab?key=e6e37a49-c425-4d10-81cc-e2bed02ecad4&interactive=true&embed=true)

![undefined.png](/wiki/Architecture/undefined.png)

## Architecture second iteration

Second iteration link: https://drive.google.com/file/d/159ueK4sskirVSlXrt5vOc8zrtNEi-vWX/view?usp=sharing 

Final version link: 

[](https://app.diagrams.net/#G1PIDPmEBkMv4x_li-4VjlRsrXWNS294y0)

### General

**While we are in the development environment we will use an EC2 server in AWS, here we deploy our application.**

We’ll have the following containers.

- **Postgresql**: a container that will hold our SQL-style database. Postgres was chosen because although it is a relational database it allows us to save jsonb objects. That is, unstructured or partially structured data. This will give us a nice balance to keep everything tidy, while having the flexibility to add unique attributes to cars or agencies.
- **Redis**: A cache-style key-value database. It will allow us to have data that is used frequently at a quick reach and improve the user experience.
- **Admin Dashboard:** Here will live the application of all the roles that are not common users. This includes NDS administrator, automobile group administrator, agency manager, salesperson.
- **User Dashboard**: It is the page that users who are looking to buy a car or are in the process will see. For the general public.
- **NGINX** ( optional ): It is open source web server software used for reverse proxying, load balancing, and caching. It provides HTTPS server capabilities and is primarily designed for maximum performance and stability.

---

![Screen Shot 2023-03-06 at 21.01.44.png](/wiki/Architecture/Screen_Shot_2023-03-06_at_21.01.44.png)

## Third Iteration

![k8s_arch.drawio (1).png](/wiki/Architecture/k8s_arch.drawio_(1).png)

This iteration replaces the use of Docker Compose running on a single server with a Kubernetes cluster. All services (including frontends) use Redis as a cache layer. Pods are managed through deployment, making scalability easy.

## Architecture for all systems ( Final Version )

********************************Payments System Final Version:********************************

*Architecture for priority system:*

![Screen Shot 2023-03-09 at 21.28.40.png](/wiki/Architecture/Screen_Shot_2023-03-09_at_21.28.40.png)

With this subsystem agencies are able to pay via stripe for a promotion on their listing, this will increase the rank on their listing. When we query from the search service, this will do two requests to ES one to get some listings to recommend based on ranking and another with the most relevant items.

**Tasks:** 

AVG Vel Per Week ( 5 people ): 55 

Total SP: **31**

| ID | Name | Description | Estimate | SCOPE |
| --- | --- | --- | --- | --- |
|  | create listings promote endpoint | Creates the function that’s in charge of returning a payment intent to the frontend | 3 | BACKEND |
|  | create webhook handler for stripe | Process payment events related to promotion and trigger microservice process-promotion-for-listing  | 3 | BACKEND |
|  | create process promotion success | Will update listing to have new rank and will schedule a a job to run a microservice in a month. ( finish-promotion-for-listing | 3 | BACKEND |
|  | finish-promotion-for-listing | Updates listing rank back to default and sends an email to notify the user | 5 | BACKEND |
|  | configure logstash container | Creates config files to run logstash in k8s | 3 | BACKEND |
|  | use logstash to pipeline data from aggregated listings to ES | create files to map PG to ES | 5 | BACKEND |
|  | create chat GPT client  | Creates a simple client so we can use it in the search system | 3 | BACKEND |
|  | create search endpoint | Service to query listings from elastic search, and returns 2 ads and rest of normal search | 3 | BACKEND |
|  | create ES storage to be used in search endpoint | Functions that interact with elastic, for the operations we will use in the search endpoint | 3 | BACKEND |
|  | configure ES in k8s | Make sure ES container is running properly | 5 | BACKEND |

*Architecture for charging per listing each month:*

![Screen Shot 2023-03-09 at 21.43.41.png](/wiki/Architecture/Screen_Shot_2023-03-09_at_21.43.41.png)

This system will create subscriptions that will track usage of the listing the user has published, it will charge at the end of the month using stripe subscriptions, and with a cron job add initial usage to clients based on their listings.

**************************************Architecture for commision per user payment:**************************************

**Tasks:** 

AVG Vel Per Week ( 5 people ): 55 

Total SP: **13**

| ID | Name | Description | Estimate | SCOPE |
| --- | --- | --- | --- | --- |
|  | create subscription endpoint | Creates the function that’s in charge of creating a stripe subscription | 5 | BACKEND |
|  | create webhook handler for stripe | Update delearship status to know its a paying delearship | 3 | BACKEND |
|  | create start-usage-new-month service | Will set initial usage for the upcoming month | 3 | BACKEND |
|  | create service to create a listing | We should track usage when we create a new listing | 2 | BACKEND |

### Future

Eventually, when we have more traffic and we want to scale our application, we propose to use the following architecture:

[https://lh6.googleusercontent.com/3q3O1177nxC_TR1r1b_XIXeL7GHtloudiyr8JEN-ytSXJWJqD9ptL-aQFEwwsxP4UYicC1J5cXoUEFmFNiF21YjF2KHCYzGO9umwQ7yul8xOa7JnPiosPujCikyLZXCVj4FM8AiCDI7lPZTVjUgEZA](https://lh6.googleusercontent.com/3q3O1177nxC_TR1r1b_XIXeL7GHtloudiyr8JEN-ytSXJWJqD9ptL-aQFEwwsxP4UYicC1J5cXoUEFmFNiF21YjF2KHCYzGO9umwQ7yul8xOa7JnPiosPujCikyLZXCVj4FM8AiCDI7lPZTVjUgEZA)

**In this diagram we can see that we would make use of several technologies in AWS, where we will use:**

| Service | Description | Reason why |
| --- | --- | --- |
| Amazon Cognito | Amazon Cognito is used for user sign-up, sign-in, and access control. It provides secure user authentication and authorization. | This will allow the users to sign to their account information (car status, payment options) knowing that no other user can view their information. |
| WAF | WAF (Web Application Firewall) is used to protect web applications from common web exploits. | Knowing the possibilities of web exploits such as query injections, is important for anyone who works with web applications. These types of attacks can be used to gain unauthorized access to sensitive information or even take control of an entire system. It is crucial to be aware of the potential risks and take steps to prevent them. |
| Route 53 | Route 53 is a DNS (Domain Name System) service that translates domain names into IP addresses to locate resources on the internet. | We will requiere a DNS that will let users access the application form the internet. |
| Cloudfront | Cloudfront is a Content Delivery Network (CDN) that distributes content globally, reducing latency and improving website speed. | This will distribute the content globally that will reduce the latancy of our users to  access our systems |
| EC2 | EC2 (Elastic Compute Cloud) provides scalable computing capacity in the cloud. | Will allow us to provice scalable computing capacity in the cloud. |
| Aplication Load Balancer | Application Load Balancer is a load balancing service that distributes incoming traffic across multiple targets, improving availability and scalability. | Will distribue incoming traffic across multiple targets, improving availability and scalability. |
| ECS | ECS (Elastic Container Service) runs and manages Docker containers on a cluster. | Will allow us to run our different applications with a docker container.  |
| RDS ( Postgres ) | RDS (Relational Database Service) is a managed database service that provides a scalable and highly available database solution. Postgres is one of the supported database engines. | Provides a scalable and highly available database solution that will allow us to host our DB. |
| Redis | Redis is an in-memory data store that provides low-latency data access for read-heavy workloads. | With it low-latency data access for read-heavy workloads we will be able to access most used and important data faster. |
| Elasticsearch | Elasticsearch is a search and analytics engine that provides fast and scalable search capabilities. | This service will allow us to seach all the cars in a faster way. |
| Chat GPT API | Chat GPT API is an AI-powered chatbot API that enables natural language processing and automated conversations with users. | Wee will use this to transfor natural language text into filter to provide the user with the best car. |

**Search system:**

![Screen Shot 2023-03-03 at 18.44.02.png](/wiki/Architecture/Screen_Shot_2023-03-03_at_18.44.02.png)

We would have a single Endpoint that would receive a Query in natural language, and apart you can receive extra filters to force them in the search.

Elastic search service will be used to facilitate the type of search on a wide variety of fields.

Option B: Simply use **RDS**

**Payments:**

For payments we will use the Stripe platform, and the Stripe Connect service, to facilitate the interaction between agencies, users, and us.

[https://lh4.googleusercontent.com/ig5JPBmUS80eEO9pHloqC9CKu8QuS7mEq-KtN4qdTXa_98-zMuFXCw_2Gyq1a7_ofG9b_9K29wC8-bKpJyGyA_gQSGtdfAT2SDdO6sk2qsI3QjTw-AMXKBMLkXV4eAT90-4BvoNuQ1_dPfD3-C5nCg](https://lh4.googleusercontent.com/ig5JPBmUS80eEO9pHloqC9CKu8QuS7mEq-KtN4qdTXa_98-zMuFXCw_2Gyq1a7_ofG9b_9K29wC8-bKpJyGyA_gQSGtdfAT2SDdO6sk2qsI3QjTw-AMXKBMLkXV4eAT90-4BvoNuQ1_dPfD3-C5nCg)

**Business Account Creation Subsystem:**

The business logic for creating an account as an agency would be as follow, they would go into our website and fill a form with their data, a super-admin of our platform would be then in charge of reviewing the request details and decide if it should be accepted or denied.

Upon approval a new account would be created and the agency would be notified, upon rejecting we would simply notify the agency and give them the appropriate reason.

[https://lh3.googleusercontent.com/0r9NeABLo90CXzaiqi5HdOxXnjr0ddCNasO0BpIqeBuUXDy3RDKi2vLgbvVh28rcwSBvQz_em_DigLm43-bog5KfV3vtXm7p_A_hdTMFW52oj2yZyBNdypWcU1Vg_QDysAl61B7H9o-PM28ET-P_Sw](https://lh3.googleusercontent.com/0r9NeABLo90CXzaiqi5HdOxXnjr0ddCNasO0BpIqeBuUXDy3RDKi2vLgbvVh28rcwSBvQz_em_DigLm43-bog5KfV3vtXm7p_A_hdTMFW52oj2yZyBNdypWcU1Vg_QDysAl61B7H9o-PM28ET-P_Sw)

**Communication System:**

[https://lh6.googleusercontent.com/UnYmqeAhMILkCIT7D0irHL3Nqjd6EYtP5hqT_PoIfis6_53A4KDyIyhXu7MYYpYmJgIuPVHs8ZDV_TJKrgtwsA0JgBM32i5NNyMXSIxirUtI4USIRN0bl4lMm_uff4UC0cfjAXNgoSB7YImRS45pcA](https://lh6.googleusercontent.com/UnYmqeAhMILkCIT7D0irHL3Nqjd6EYtP5hqT_PoIfis6_53A4KDyIyhXu7MYYpYmJgIuPVHs8ZDV_TJKrgtwsA0JgBM32i5NNyMXSIxirUtI4USIRN0bl4lMm_uff4UC0cfjAXNgoSB7YImRS45pcA)

**Authentication**

[https://lh5.googleusercontent.com/bKPLmBAk9gXm030jGXRsUFH8mMUqfsZY1w5K8Wbc1aiYcf4ve--qt9xCahHcM0CO3I0pPo2AiLh1VjcOjm9TNQCGdVOiv66I35IhLT45eAjSDfXv32g6d3cWV9CXyBZxpgT6_RPrkS3cqInQQVpMHQ](https://lh5.googleusercontent.com/bKPLmBAk9gXm030jGXRsUFH8mMUqfsZY1w5K8Wbc1aiYcf4ve--qt9xCahHcM0CO3I0pPo2AiLh1VjcOjm9TNQCGdVOiv66I35IhLT45eAjSDfXv32g6d3cWV9CXyBZxpgT6_RPrkS3cqInQQVpMHQ)

**Metrics System:**

We will have a service that will allow us to generate any type of query to any table based on permissions.

Option:

- We could have predefined metrics we could query

**CRUD:  Car Catalogue**

TBD: Configure requirements for purchase and use them on payout