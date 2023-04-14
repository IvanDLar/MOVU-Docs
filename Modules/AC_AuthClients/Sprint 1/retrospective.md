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


# Things we can improve
