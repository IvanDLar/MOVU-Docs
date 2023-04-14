### Thursday 13, 2023

# User stories complete

## Issues In progress

- AC  Set up Firebase Auth 
- AC  customJWT lambda
- AC  Create api validator middleware
- AC  Auth context on next
 
# Risks

* Having an insceure login/signup proccess 
 
    **Mitigation** Use firebase as an authentication provider
    
* Having insecure endpoints in API allows for unauthenticated clients to send requests to api.
 
    **Mitigation** Create a middleware validator that will check for the validity of the user's jwt. Allow access to the main function or not, depending on 
    if the token is valid

* User's with weak passwords are vulnerable to attakcs
 
    **Mitigation** Add validators on the frontend to ensure only secure passwords are allowd


# Things we did good 
 
- Got familiar with firebase as an authentication provider 
- Created endpoints to retrieve user's data 
- Defined all the tasks we need to achieve in order to complete all user stories related to this module.

# Things we can improve

- Start working on tickets since day 1 of the sprint
- Complete at least 1 user story 
- Faster implementation time for every ticket
