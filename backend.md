<!-- The (first) h1 will be used as the <title> of the HTML page -->
# Martin Hsueh

<!-- The unordered list immediately after the h1 will be formatted on a single
line. It is intended to be used for contact details -->
- <mhsueh2@gmail.com>
- <https://www.linkedin.com/in/martinhsueh>
- Seattle
- Willing to relocate

<!-- The paragraph after the h1 and ul and before the first h2 is optional. It
is intended to be used for a summary. -->

## Skills

- **Language**: Typescript/Javascript, Python, Bash, Matlab
- **Technology**: NodeJS, NestJS, ReactJS, Redux, Flask, AWS, Temporal, scikit-learn
- **Database**  MongoDB, PostgreSQL, Redis, ElasticSearch, DynamoDB
- **DevOps**: Git, Docker, Kubernetes (K8s), NX, Vite, Terraform

## Experience

<!-- You have to wrap the "left" and "right" half of these headings in spans by
hand -->
### <span>Career Break</span><span>05/2023 - 09/2023</span>
- Fulfilled my dream of bikepacking around the island of Taiwan, jogged along the strenuous 12-mile loop of the historic Seoul Wall, embarked on 5 river tracing expeditions, and indulged in all of the 8 cuisines of China. 
### <span>Tech Lead - Operations, Xealth</span><span>01/2022 - 05/2023</span>
- Led an agile team of 5 engineers in managing the Xealth tooling ecosystem, including 2 mission-critical distributed systems and 5 AWS applications written in TypeScript.
- Designed 10+ ElasticSearch indices. Optimized a search algorithm, achieving an average latency of <3ms, far below the 80ms constraint.
- Developed scripts to deploy App Config as Code for 3rd-party APIs, reducing DevOps overhead by 90%, and received personal praise from the CTO.
- Spearheaded the company's core Content Delivery System, resulting in a 40% reduction in operational costs per customer request.
      - Composed a 90+ page design doc through 5 iterations, reviewed by principal engineers, PM, and compliance.
      - Built a Node Server on Nest framework with 80% test coverage. It collects 200 events per second from 4 webhooks and acts as a proxy to deliver data from Elasticsearch and various RESTful APIs. Repo served as an exemplar for future projects.
      - Engineered a scalable and reliable Temporal Worker to transform and write data to OpenSearch, maintaining 100% data integrity even during 2 dependency outages. Utilized Kubernetes to scale pods 3 times the expected loads, completing a critical 40-minute production migration.
- Mentored junior engineers with code and design reviews, following industry best practices. 
- Experimented with NestJS, Temporal, NX, Contentful, and Vite, implemented them in production, and authored tech blogs to promote their adoption within the company.
- Resolved critical production bugs within tight deadlines, leveraging tools such as AWS Cloudwatch and Prometheus


### <span>Full Stack Software Engineer, Xealth</span><span>09/2019 - 01/2022</span>
- Maintained the Automated Ordering system, which processed over 1M events per hour. It's a Dockerized state machine written in TypeScript and integrated with AWS SQS and S3, driving 60% of revenue
- Contributed to the design of core Node/Express APIs, which serve the patient portal, doctor portal, data reporting, ordering, internal tools, and vendor callbacks.
- Developed an Event Notification service using AWS Lambdas, SQS, and S3, consistently delivering 300K events daily to subscribers, resulting in 5% of total orders.
- Optimized a sluggish Lambda API through caching and concurrent request management, slashing response latency by 85% and increasing user productivity by over 30%.
- Identified inefficiencies in release tasks and enhanced developer efficiency by 50% via automation using a Bash script.
- Designed and implemented 5+ external API integrations, handling 200K requests via SOAP or REST/OAuth protocols.
- Reduced developer configuration requirements by 25% by employing Object-Oriented design principles, minimizing code duplication.
- Collaborated with customers and vendors to resolve bugs and support design decisions.

### <span>Software Engineer, Bespoke Metrics</span><span>01/2018 – 09/2018</span>
- Enhanced 15+ JWT secured Python-Flask APIs with 95%+ code coverage
- Improved development efficiency by 50% by implementing a set of typed data validators
- Built the Bespoke framework, which consists of 8 generic APIs secured by OAuth2 and backed by PostgreSQL DB
- Trained full stack coops to build APIs for the flagship COMPASS application


## Projects

### <span>NBA Game Winner Prediction ML Model</span> <span>2019</span>
- Extracted 14 features from 20 years of historical NBA games.
- Built supervised learning models using algorithms such as regression, kNN, SVC, and linear discriminants with Python and its scikit-learn library
- Achieved 72% win/loss prediction accuracy with linear discriminant

## Education

### <span>University of Waterloo, BASc in Mechatronics Engineering</span> <span>2015 - 2019</span>