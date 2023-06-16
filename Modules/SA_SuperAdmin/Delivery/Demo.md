# Demo

## Introduction

This document presents the demo of the Super Admin module, showcasing its visual appearance and functionality. The demo highlights the features of the creation of new super admins, approval of new automotive groups, and view billing data of the automotive groups.

## User Stories

The following are the user stories that were developed and fulfilled by this module.

- [**US06 - Manage automotive group sign up requests**](https://github.com/IvanDLar/MOVU-Docs/milestone/42)
  - **Description:** To be able to view all requests made by new automotive groups. The administrator should be able to see both the request data and the group information.
  - **Validation:** The Requests section was developed, where a list of all requests made by new groups is displayed. By clicking on each request, both the group and request data are shown. Additionally, the uploaded documents by the group can be viewed.
- [**US62 - Automotive Groups Documentation Application Approvals**](https://github.com/IvanDLar/MOVU-Docs/milestone/64)
  - **Description:** A super administrator should be able to respond to new group requests by accepting or rejecting them.
  - **Validation:** In the details view of a request, there is also a form where a super administrator can respond to the request. The form allows accepting or rejecting individual documents, as well as providing a general response and entering comments regarding the request.
- [**US05 - Super admin register**](https://github.com/IvanDLar/MOVU-Docs/milestone/38)
  - **Description:** The system should allow the creation of new super administrator accounts and provide a login mechanism for accessing the super admin platform.
  - **Validation:** The system allows the creation of new super administrator accounts. This process should be performed by another super administrator to ensure control over administrator users. Additionally, the system allows login from the general login page since our authentication provider (Firebase) enables role differentiation.
- [**US25 - Data Privacy**](https://github.com/IvanDLar/MOVU-Docs/milestone/7)
  - **Description:** Not everyone should be able to create a super administrator account since this role is not intended for public access. Therefore, the creation of new accounts should be protected and restricted.
  - **Validation:** The creation of new super administrators is restricted to users with the super administrator role. This control ensures that only authorized individuals have access to the platform. When a super administrator creates a new super administrator account, they must enter the account's details. The email associated with the new account will receive a temporary password, which can be changed by the user to enhance privacy.

## Demo URL

Please find the Super Admin module demo at the following URL:

https://drive.google.com/file/d/1nE7Kz-zXEE2WgTLHO1XOjMIW3CJy-RNf/view?usp=sharing
