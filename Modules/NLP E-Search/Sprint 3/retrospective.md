### Friday 28, 2023

# User stories

## User stories / milestones

- [US40 - NL Search](https://github.com/IvanDLar/MOVU-Docs/milestone/50)
- [US42 - Filter search](https://github.com/IvanDLar/MOVU-Docs/milestone/54)

## Validations

- [VA403](https://github.com/IvanDLar/MOVU-Docs/issues/126) : FINISHED WITH OUR MODULE ISSUES
- [VA423](https://github.com/IvanDLar/MOVU-Docs/issues/175) : FINISHED WITH OUR MODULE ISSUES
- [VA402](https://github.com/IvanDLar/MOVU-Docs/issues/125) : DONE
- [VA404](https://github.com/IvanDLar/MOVU-Docs/issues/175) : FINISHED WITH OUR MODULE ISSUES

## Issues progress

- NS - Luis base configuration: 100%
- NS - Create ML pipeline to create text embedding: 100%
- NS - Upload Dummy Data: 100%
- NS - Define Model for ElasticSearch: 100%
- NS - Deploy NER model v1.0: 100%
- NS - Label dataset for ner: 100%
- NS - Generate API DOCS: 100%
- NS - Create Autocompletion endpoint V1: 100%
- NS - Search service V2: 100%
- NS - Search Front V1: 100%
- NS - Test Document: 100%
- NS - Technical Document: 100%
- NS - API Tests in Jest: 100%
- NS - Create custom tokenizer to ignore special characters: 100%
- NS - Fuzzy Search: 100%
- NS - Record Search: 100% 

# Risks + mitigation

- The Azure LUIS service was deprecated, and the new service is not as well documented: Search for the new SDK in github and how to use it.
- The NER search service is very slow: Use keyword and semantic search as our main search systems, include NER as an optional parameter in the endpoint.
- The frontend page that displays the results was not ready in time for the demo presentation: Demonstrate the search functionality in more low level.
- The credentials to deploy the backend from github actions could be wrong: Deploy and test locally while the issue persist, consult with project admin to solve the credentials. 

# Things we can improve

- As the frontend side of the search was not ready in time, we should have prepared a simple interface to display the search more visually.
- Help other teams once we finish with our tasks.
- Better communication with other teams to ensure the project structure is correct.

# Things we did good

- Good time managment: we managed to complete all of the tasks in the sprint.
- Good testing to compare different search methods and conclude which one is better.
- Managed to create the document deliverables.
- Good/clear explanations on the technical document.
