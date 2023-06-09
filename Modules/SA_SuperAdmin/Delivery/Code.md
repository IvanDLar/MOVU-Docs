# Code Document: Super Admin Module

## Table of Contents

1. [Introduction](#introduction)
2. [Main Files](#main-files)
3. [Page Descriptions](#component-descriptions)
   - [1. Automotive groups list](#1.-automotive-groups-list)
   - [2. Automotive group details](#2.-Automotive-group-details)
   - [3. Automotive group dealerships](#3.-Automotive-group-dealerships)
   - [4. My profile](#4.-My-profile)
   - [5. Change password](#2.-Automotive-group-details)
   - [6. Requests list](#2.-Automotive-group-details)
   - [7. Super admins users list](#2.-Automotive-group-details)
   - [8. Super admin user details](#2.-Automotive-group-details)
   - [9. Create new super admin](#9.-Create-new-super-admin)
4. [Key Functionality](#key-functionality)
5. [API Integration](#api-integration)
6. [Responsive Design](#responsive-design)
7. [Accessibility](#accessibility)

## Introduction

This code document provides an in-depth explanation of the Super Addmin module, including its pages, key functionality, and design considerations. The Super Admin module is built using Next.js, TypeScript, React, and Tailwind CSS, and it features various sections to deliver a seamless user experience. The purpose of this document is to provide insights into the code structure and the implementation details of each page.

## Main Files

1. `pages/super-admin/groups/index.tsx`
2. `pages/super-admin/groups/[automotiveGroupId]/index.tsx`
3. `pages/super-admin/groups/[automotiveGroupId]/concesionarias.tsx`
4. `pages/super-admin/profile/index.tsx`
5. `pages/super-admin/profile/change-password.tsx`
6. `pages/super-admin/requests/index.tsx`
7. `pages/super-admin/users/index.tsx`
8. `pages/super-admin/users/detalles.tsx`
9. `pages/super-admin/users/nuevo.tsx`

## Page Descriptions

### 1. Automotive groups list

`/groups/index.tsx` On this page, you can view a list of all automotive groups registered in the system. For each group, you can see its name, logo, creation date, and a button to view the group details.

### 2. Automotive group details

`/groups/[automotiveGroupId]/index.tsx` On this page, you can view the details of a group. In addition to its basic information such as name and location, you can see the billing data: the number of dealerships it has, the number of listed cars, and the total sales.

### 3. Automotive group dealerships

`/groups/[automotiveGroupId]/concesionarias.tsx` On this page, you can view the list of all dealerships within a group, as well as their details.

### 4. My profile

`/profile/index` On this page, you can view the data of the logged-in super administrator, such as their name, email, phone number, etc.

### 5. Change password

`/profile/change-password.tsx` On this page, the super administrator can update their password.

### 6. Requests list

`/requests/index.tsx` On this page, you can view the list of requests made by new groups. Additionally, you can see the details of each request and have the ability to approve or reject them.

### 7. Super admins users list

`/users/index.tsx` On this page, you can see a list of all super administrators in the system.

### 8. Super admin user details

`/users/detalles.tsx` On this page, the details of a super administrator are displayed, including their name, email, and phone number.

### 9. Create new super admin

`/users/nuevo.tsx` On this page, you can create a new super administrator account. It is a form that requests the data of the new administrator, such as name, email, and other required information.
