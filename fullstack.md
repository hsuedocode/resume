<!-- The (first) h1 will be used as the <title> of the HTML page -->
# Martin Hsueh

<!-- The unordered list immediately after the h1 will be formatted on a single
line. It is intended to be used for contact details -->
- <mhsueh2@gmail.com>
- <https://www.linkedin.com/in/martinhsueh>
- Seattle
- Willing to relocate

<!-- The paragraph after the h1 and ul and before the first h2 is optional. It
is intended to be used for a short summary. -->

## Skills

- **Language**: Typescript, Python, Bash
- **Framework**: Node-Express,  Node-Nest, React-Redux, Python-Flask
- **Database**  MongoDb, PostgresSQL, Redis, ElasticSearch, DynamoDB
- **Other**: Git, AWS EC2/ECS/S3/Lambda/SQS, Docker, Kubernetes, Temporal, TDD

## Experience

<!-- You have to wrap the "left" and "right" half of these headings in spans by
hand -->
### <span>Career Break</span><span>05/2023 - 09/2023</span>
- Fulfilled my dream of bikepacking around the island of Taiwan, jogged along the streneous 12-mile loop of the historic Seoul Wall, embarked on 5 river tracing expeditions, and indulged in all of the 8 cuisines of China. 
### <span>Tech Lead - Internal Tools, Xealth</span><span>02/2022 - 05/2023</span>
- Led an agile team of 5 engineers in managing the Xealth tooling ecosystem, including 2 mission-critical distributed systems and 5 full-stack applications written in TypeScript.
- Collaborated with PM to create a code-free email template editor with React and TinyMCE, cutting cost per change by 80% and boosting turnaround time by 300%.
- Designed 10+ ElasticSearch indices. Optimized a search algorithm, achieving an average latency of <3ms, far below the 80ms constraint.
- Founded, architected and built a distributed Content Delivery System, resulting in a 40% reduction in operational costs per customer request.
      - Composed a 90+ page design doc through 5 iterations, reviewed by principal engineers
      - Built 30 unique/10 generic UI Extensions with 80% test coverage, used across 4 React applications.
      - Architected and built a Node-Nest Server with 80% test coverage. It collects 200 events per second from 4 webhooks and acts as a proxy to deliver data from Elasticsearch and various RESTful APIs.
      - Engineered a scalable and reliable Temporal Worker to transform and write data to OpenSearch, maintaining 100% data integrity even during 2 dependency outages. Utilized Kubernetes to scale pods 3 times expected loads, successfully completing a critical 40-minute production migration. 
      - Built the migration job, extracting 3TB of live data from ElasticSearch/S3 and transforming and writing it to rate-limited external APIs in batches.
      - Developed scripts for deploying App Config As Code to 3rd-party APIs to ensure a single source of truth.
- Experimented with NestJS, Temporal, NX, Contentful and Vite, implemented them in production, and authored tech blogs to promote their adoption within the company.
- Partnered with cross-functional engineers to tackle intricate engineering challenges, then translated the design into roadmap.
- Mentored junior engineers with code and design reviews, following industry best practices.
- Resolved critical production bugs within tight deadlines, leveraging tools such as AWS Cloudwatch and Prometheus



### <span>Full Stack Software Engineer, Xealth</span><span>09/2019 - 02/2022</span>
- Maintained the Automated Ordering system, which processed over 1M events per hour. It's a Dockerized state machine written in TypeScript and integrated with AWS SQS and S3, driving 60% of revenue
- Contributed to the design of core Node/Express APIs, which serve the patient portal, doctor portal, data reporting, ordering, internal tools, and vendor callbacks.
- Developed an Event Notification service using AWS Lambdas, SQS, and S3, consistently delivering 300K events daily to subscribers, resulting in 5% of total orders.
- Optimized a sluggish Lambda API through caching and concurrent request management, slashing response latency by 85% and increasing user productivity by over 30%.
- Identified inefficiencies in release tasks and enhanced developer efficiency by 50% via automation using a Bash script.
- Designed and implemented 5+ external API integrations, handling 200K requests via SOAP or REST/OAuth protocols.
- Reduced developer configuration requirements by 25% by employing Object-Oriented design principles, minimizing code duplication.
- Contributed 35% of the code for the Config Manager UI (project of 3 engineers), which was built on React-Redux and consisted of hundreds of components and containers.
- Collaborated with customers and vendors to resolve bugs and support design decisions.

### <span>Software Engineer Internship, Bespoke Metrics</span><span>01/2018 – 09/2018</span>
- Enhanced 15+ JWT secured Python-Flask APIs with 95%+ code coverage
- Improved development efficiency by 50% by implementing a set of typed data validators
- Built the Bespoke framework, which consists of 8 generic APIs secured by OAuth2 and backed by PostgreSQL DB
- Trained full stack coops to build APIs for the flagship COMPASS application


### <span>Frontend Software Engineer Internship, TD Asset Management</span><span>04/2017 – 08/2017</span>
- Enhanced 15+ React-Redux UI features for the Portfolio Management App.
- Improved user workflow by building the user notification component on top of the UI 
- Executed new features by working directly with team VP and end users

## Projects

### <span>NBA Game Winner Prediction ML Model</span> <span>2019</span>
- Extracted 14 features from 20 years of historical NBA games.
- Built supervised learning models using algorithms such as regression, kNN, SVC, and linear discriminants with Python and its scikit-learn library
- Achieved 72% win/loss prediction accuracy with linear discriminant

## Education

### <span>University of Waterloo, BASc in Mechatronics Engineering</span> <span>2015 - 2019</span>