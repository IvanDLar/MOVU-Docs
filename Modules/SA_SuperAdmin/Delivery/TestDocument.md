# Test Document: Super Admin Unit Tests

## Introduction

This test document focuses on verifying the correct functionality of the Super Admin module. We will go through each functionalify of the super admin module and ensure that they work as expected. This document provides a summary of each test and their expected results.

## Summary of Tests

1. **Get all super administrators**: Verify that the endpoints get all the super administrators.
2. **Create super administrator**: Verify that the the endpoint creates a super administrator with a valid body. Verify that the endpoint returns an error with an invalid body.
3. **Get super admin by id**: Verify that the endpoints returns a successful response with a valid uid, and an error response with an invalid uid.
4. **Get all automotive groups**: Verify that the endpoints get all the automotive groups.
5. **Get all automotive groups requests**: Verify that the endpoints get all the automotive groups requests.
6. **Update automotive group data**: Verify that the endpoints returns a successful response with a valid body, and an error response with an invalid body.

## Test Execution

Tests will be executed both manually and automatically. Manual tests will be performed by developers and testers during development, while automatic tests will be executed by the Github Actions Pipeline on every pull request.

## Test Documents

Unit Tests:
https://docs.google.com/spreadsheets/d/1e0sDwA3gLGfe6FoM_edHYy6b4L5oIycC/edit?usp=sharing&ouid=107797780739456330946&rtpof=true&sd=true

Path Tests:
https://docs.google.com/spreadsheets/d/18OWtyMobF3E9ONWEruaHJ3E6yLIqWg5X/edit?usp=sharing&ouid=107797780739456330946&rtpof=true&sd=true
