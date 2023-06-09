### Retrospective Document - Friday, June 9th, 2023

#### Validations

- Validations completed during the sprint:

| Validation ID | Done |
| ------------- | ---- |
| VA075         | Yes  |
| VA073         | Yes  |
| VA074         | Yes  |
| VA371         | Yes  |
| VA174         | Yes  |
| VA341         | Yes  |
| VA331         | Yes  |
| VA335         | Yes  |
| VA332         | Yes  |
| VA334         | Yes  |

#### Issues Progress

- CR - REST endpoints for financing plans

  - Assignees: marriagav, StephanGuingor
  - Status: 100%

- CR - REST endpoints for listings

  - Assignees: DiegoAraque21
  - Status: 100%

- CR - Polish UI

  - Assignees: AnYelg
  - Status: 100%

- CR - Car dealership admin dashboard to add and manage their employees

  - Assignees: DiegoAraque21
  - Status: 100%

- CR - REST endpoints for car variants

  - Assignees: DiegoAraque21
  - Status: 100%

- CR - REST endpoints for car dealerships to register accounts for their employees

  - Assignees: DiegoAraque21
  - Status: 100%

- CR - Financing Plans View, upload, manage

  - Assignees: PRocha0503, marriagav
  - Status: 100%

- CR - Salesman dashboard to view sales/orders and client status

  - Assignees: marriagav
  - Status: 100%

- CR - REST endpoints for car_models

  - Assignees: marriagav
  - Status: 100%

- CR - Create Front End view for login page

  - Assignees: lfvm, ariigat0
  - Status: 100%

- CR - Add claims for different user types

  - Assignees: marriagav
  - Status: 100%

- CR - Endpoint to approve automotive groups

  - Assignees: StephanGuingor, marriagav
  - Status: 100%

- CR - REST endpoints for brands/makes
  - Assignees: PRocha0503
  - Status: 100%

#### Risks + Mitigations

- This is a very big module and it touches a lot of other modules, which could provoke interference with each other's work: Have a sprint planning every Monday to assign tasks and invite other module leaders to the meeting.
- There are a lot of people in the module, and we can't all always attend the meetings: Report status in chat and record the meetings.
- The data model does not align with the car dealership registration request: Create a separate table for the requests.
- Testing the endpoints is difficult because we require accounts of different types to test them: Create fake accounts with privileges to test the endpoints.
- Documentation was not started earlier, which led to delays in completing it: Prioritize documentation from the beginning of the next sprint.
- Lack of documentation impacted the overall progress: Improve communication and prioritize documentation alongside development tasks.

#### Things We Did Well

- We managed to finish the development of the module this sprint, including functionalities to create listings, car models, and car variants.
- We also finished pending functionalities like creating and updating an automotive group request, creating financing plans, and creating accounts for employees of a dealership, as well as adding other owners to the automotive group.
- Good coordination between backend and frontend functionalities.
- Quickly ideated how to implement new functionalities.
- Communicated efficiently to avoid repeating work.
- Integrated all the functionalities to work together.

#### Things We Will Do to Improve Next Sprint

- Start the sprint sooner and organize task assignments better.
- Make sure that everyone understands their assigned tasks and knows who to go to for questions.
- Communicate better with the database and authentication teams to avoid misunderstandings.
- Prioritize documentation alongside code development to avoid delays.
- Ensure that documentation is started early in the sprint and completed in a timely manner.

#### Additional Information

- The documentation, including API docs, user manual for dealerships, and test reports, was not started until this week. This was mainly due to the fact that we had to focus on development as the end of the project nears.
