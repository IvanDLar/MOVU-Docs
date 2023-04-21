### Thursday 20, 2023

# User stories

## User stories / milestones

- [US40 - NL Search](https://github.com/IvanDLar/MOVU-Docs/milestone/50)
- [US42 - Filter search](https://github.com/IvanDLar/MOVU-Docs/milestone/54)

## Validations

- [VA403](https://github.com/IvanDLar/MOVU-Docs/issues/126) : FINISHED WITH OUR MODULE ISSUES
- [VA423](https://github.com/IvanDLar/MOVU-Docs/issues/175) : IN PROGRESS
- [VA402](https://github.com/IvanDLar/MOVU-Docs/issues/125) : DONE
- [VA404](https://github.com/IvanDLar/MOVU-Docs/issues/175) : IN PROGRESS

## Issues progress

- NS - Luis base configuration: 100%
- NS - Create ML pipeline to create text embedding: 100%
- NS - Upload Dummy Data: 100%
- NS - Define Model for ElasticSearch: 80%
- NS - Deploy NER model v1.0: 100%
- NS - Label dataset for ner: 100%
- NS - Generate API DOCS: 80%
- NS - Create Autocompletion endpoint V1: 100%
- NS - Search service V2: 85%
- NS - Search Front V1: 100%

# Risks + mitigation

- Synchronization issues between postgres and elastic: use an existing service like PGSync / research ways to trigger lambdas on db change.
- The semantic search model might not be the most precise: use a different model, such as the openAI model or LLaMA / leverage keyword search and semantic search for specific use cases.
- The listings descriptions are not written in natural language and that might impact search: when an agency uploads a listing, they should provide a description for it / use LUIS to identify properties in listings in natural languages / use a model to build this descriptions.

# Things we can improve

- Perform tests to ensure quality
- Advance in the documentation deliverables 
- Prioritize blocking tasks instead of new features

# Things we did good

-  LUIS configuration was compleated quicker than expected
-  All the base services are now configured
-  Close to finishing the first demo
