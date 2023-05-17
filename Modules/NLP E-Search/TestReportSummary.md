# Test Title: Unit Tests Search Endpoints
- Priority: Medium
- Test Case ID: TC1
- Test Number ID: TN1
- Test Date: 04/25/2023
- Priority Key: Low

## Test Description:
The test focused on verifying the correctness of endpoints by ensuring that the error codes and responses were correct, assuming that the API integrations functioned as expected. The endpoints were mocked for testing purposes.

Test Designer: Stephan Guingor Falcon
Test Executioner: Github Actions Pipeline
Execution Date: On every pull request

## Test Dependencies and Conditions:

The test does not require any external dependencies as it mocks the elasticsearch service and geolocation API.
To run the tests, Node.js and Jest must be installed. After running npm install, executing npm test will run the tests.
The endpoints do not require any credentials, allowing users to search without logging in.
In addition to manual testing, the tests are automatically executed on every pull request in the Github Actions environment. They run in an ubuntu-latest environment with Node.js version 18.x.

## Additional Notes:
The test report includes images that can provide further visual evidence and details for each test step.

The overall execution priority for the test units was categorized as follows:

High priority for the test description and execution.
Medium priority for the test dependencies and conditions.
Low priority for the test title and priority key.
The test units focused on various endpoints, including /listings/search and /listings/autocomplete, and covered different scenarios such as querying with or without keywords, enabling tracking, and handling various error cases.

The tests were designed to ensure the correct behavior of the endpoints by checking the expected status codes, response contents, and error handling. Mocked services like elasticsearch and geolocation were utilized to simulate the expected behavior.

The test executioner was set up using the Github Actions Pipeline, which automatically runs the tests on every pull request. This ensures continuous integration and helps identify any issues or failures early in the development process.

Overall, the test report provides a comprehensive overview of the planning, execution, and results of the unit tests performed on the search endpoints. The tests validate the functionality and correctness of the API endpoints under various scenarios, contributing to the overall quality assurance of the system.

## Summary of Test Steps:

Step S1:
GET /listings/search returns a 200 status code and a response containing the expected listings from the mocked elasticsearch service.

Step S2:
GET /listings/search returns a 400 status code when no query is provided on neural search. No call to the elasticsearch service should be made.

Step S3:
GET /listings/search returns a 200 status code when no query is provided on keyword search. The response should contain items from the elasticsearch service.

Step S4:
GET /listings/search returns a 200 status code when enable_tracking is true, and a call to the geolocation API is made. The response should contain items from the elasticsearch service.

Step S5:
GET /listings/search returns a 400 status code for an invalid type in a field. The response should include an error specifying the expected type for the given field.

Step S6:
GET /listings/autocomplete returns a 200 status code and a response containing the expected listings from the mocked elasticsearch service.

Step S7:
GET /listings/autocomplete returns a 200 status code and an empty array response when no hits are found.

Step S8:
GET /listings/autocomplete returns a 400 status code when no query is provided. The response should include an error message.

Step S9:
GET /listings/autocomplete returns a 400 status code when the query length is greater than 256 characters. The response should include an error message.

Step S10:
POST /listings/autocomplete returns a 201 status code and a 'query successfully processed' message when a query is provided.

Step S11:
POST /listings/autocomplete returns a 400 status code when the query parameter is greater than 256 characters. The response should include an error message.

Step S12:
POST /listings/autocomplete returns a 400 status code when no query is provided. The response should include an error message.

Step S13:
POST /listings/autocomplete returns a 500 status code with an error message if an unexpected failure occurs, such as with the elasticsearch service.

The test report provides details on the test units performed, their priorities, descriptions, dependencies, test steps, expected results, seen results, and approval status.
