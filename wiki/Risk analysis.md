# Risk analysis

Created: March 9, 2023 7:49 PM
Last edited time: March 15, 2023 6:58 PM
Tags: document

| Risk No. | Description | Mitigation Action | Owner | Probability | Impact |
| --- | --- | --- | --- | --- | --- |
| 1 | SQL Injection | Prune user inputs to avoid SQL inputs. | Development team | High | High |
| 2 | DoS Attack: Malicious attempt to overwhelm a service by flooding it with traffic | Block IP user that makes more 1000 requests per minute by ensuring the correct firewall configuration. | Development team | Low | Medium |
| 3 | Database corruption/loss | Daily Backup to recover up to data. | Development team | Low | High |
| 4 | New teammates integrating to the project might lead to misunderstanding on work flow as well as the development planning and architecture | Assign a manager to each of the teams, all the managers will have weekly meetings with the project leader. The sprint plannings will happen here. | Product Manager | High | High |
| 5 | Infrastructure crashes or saturation | Ensure orchestraitor is configured so that crash services are replaced automaticlly and autoscaleablillity. | Architect | Medium | Low |
| 6 | As we purpose having different containers (per feature) for the development stages, at the moment of merging all of them into the final application, some features might break and need to be refactored. | Every two weeks, join all the containers and verify that everything is working as intended. | Architect | High | Medium |
