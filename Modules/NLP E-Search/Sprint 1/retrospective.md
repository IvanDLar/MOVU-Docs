### Thursday 13, 2023

# User stories

## User stories / milestones

- [US40 - NL Search](https://github.com/IvanDLar/MOVU-Docs/milestone/50)
- [US42 - Filter search](https://github.com/IvanDLar/MOVU-Docs/milestone/54)

## Validations

- [VA403](https://github.com/IvanDLar/MOVU-Docs/issues/126)
- [VA423](https://github.com/IvanDLar/MOVU-Docs/issues/175)
- [VA402](https://github.com/IvanDLar/MOVU-Docs/issues/125)
- [VA404](https://github.com/IvanDLar/MOVU-Docs/issues/175)

## Issues progress

- NS - Integrate Luis to AWS SSO: not longer required
- NS - Luis base configuration: 50%
- NS - Create Search Endpoint V1: 100% 
- NS - Create ML pipeline to create text embedding: 50%
- NS - Upload Dummy Data: 40%
- NS - Upload ML Model to ElasticSearch: 100%
- NS - Define Model for ElasticSearch: 50%

# Risks + mitigation

- OpenSearch does not have an ui to manage ML models: Use API / Search alternatives
- ML model might not perform well for spanish queries: Find multi-lingual model, model infrastructure as code
- Azure student accounts cannot use active directory to use in conjunction with AWS: Create and manage users from Azure / use free tier account
- Search lambda does not have access to the internet: Create a nat-getway / Do not use VPC for services that need internet access
- Databse design changes might impact other teams/systems: Constant iterating and communication with other teams / weekly group meetings
- Team members might not be available for meetings: Record the meetings, the perticipants that cant attend must provide their status in groupchat
- The scraped data might not match the database model / business case: make some pre-processing of the information before uploading it to the db.

# Things we can improve

- Base tasks on user stories, do not jump straight into coding without the correct project planning.
- Define priorities based on user story points.
- Document process and add readme files for new functionality / web scraping / database design.

# Things we did good

- Stephan did a good job with base configuration and helping the team
- Meetings throghout the week, good communication
- Good planning of how the system is going to work, makign sure that everyone on the team understands
- Extraction of a good data set for the db
