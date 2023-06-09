# Super Admin Delivery

## Table of Contents

1. [Introduction](#introduction)
2. [User Stories](#user-stories)
3. [Project Structure](#project-structure)
4. [Delivery Components](#delivery-components)
   - [Test Document](#test-document)
   - [Demo](#demo)
   - [User Manual](#user-manual)
   - [Code](#code)
   - [API Documentation](#api-documentation)
5. [Technologies and Libraries](#technologies-and-libraries)

## User Stories

The following are the user stories that were developed and fulfilled by this module. In the [demo deliverable](./Delivery/Demo.md), there is a more detailed description of how the requirements of each of these stories are met.

- [US06 - Manage automotive group sign up requests](https://github.com/IvanDLar/MOVU-Docs/milestone/42)
- [US62 - Automotive Groups Documentation Application Approvals](https://github.com/IvanDLar/MOVU-Docs/milestone/64)
- [US05 - Super admin register](https://github.com/IvanDLar/MOVU-Docs/milestone/38)
- [US25 - Data Privacy](https://github.com/IvanDLar/MOVU-Docs/milestone/7)

## Introduction

This README file outlines the delivery of the Super Admin module, which is part of a larger Next.js project. The Super Admin features various components and functionalities, including creation of new super admins, approval of new automotive groups, and view billing data of the automotive groups. The goal of this document is to provide a comprehensive overview of the project, as well as instructions on how to access and review the delivery components.

## Project Structure

The Super Admin module is organized in a modular fashion to ensure easy maintainability and scalability. The main code files for the module includes:

1. `pages/super-admin/groups/index.tsx`
2. `pages/super-admin/groups/[automotiveGroupId]/index.tsx`
3. `pages/super-admin/groups/[automotiveGroupId]/concesionarias.tsx`
4. `pages/super-admin/profile/index.tsx`
5. `pages/super-admin/profile/change-password.tsx`
6. `pages/super-admin/requests/index.tsx`
7. `pages/super-admin/users/index.tsx`
8. `pages/super-admin/users/detalles.tsx`
9. `pages/super-admin/users/nuevo.tsx`

## Delivery Components

### Test Document

A comprehensive test document is provided, which details the results of all tests conducted for the Super Admin module.

The test document can be found here: [Test Document](./Delivery/TestDocument.md)

### Demo

A demo video is provided to showcase the visual result of the implemented Super Admin module, as well as the proper functioning of all its features and screens. The demo also includes a list of completed user stories with their respective validations.

The demo video can be found here: [Demo](./Delivery/Demo.md)

### User Manual

A document that provides instructions, guidelines, and information about how to use the Super Admin module or perform a specific task effectively and safely as the final user (movu super administrators).

The user manual document can be found here: [User Manual](./Delivery/UserManual.md)

### Code

The code for the Super Admin module is available in the repository. The modular approach ensures maintainability and ease of future updates.
Additionally, a document was created describing the features and functionality of the module's pages.

The code description document can be found here: [Code Description](./Delivery/Code.md)

### API Documentation

The API Documentation is a set of instructions and guidelines that explain how to interact with a particular endpoints developed for the Super Admin Module.

The API Documentation description document can be found here: [API Documentation](./Delivery/APIDocumentation.md)

## Technologies and Libraries

The Super Admin module is built using the following technologies and libraries:

1. [Next.js](https://nextjs.org/)
2. [TypeScript](https://www.typescriptlang.org/)
3. [React](https://reactjs.org/)
4. [Tailwind CSS](https://tailwindcss.com/)
5. [Firebase Auth](https://firebase.google.com/docs/auth)
