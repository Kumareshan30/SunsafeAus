# Project Overview

This project is a comprehensive web application designed to provide users with personalized sun safety recommendations. It integrates real-time environmental data to enhance user experience and health awareness. The application is structured into three primary components:

1. **Frontend**: A multi-page application (MPA) developed using Vue.js, deployed on Cloudflare Pages.
2. **Backend**: Built with FastAPI, a modern web framework for Python, and hosted on Render.
3. **Database**: Implemented with PostgreSQL, managed through Amazon Web Services (AWS) Relational Database Service (RDS).

The live application is accessible at [https://sunsafeaus.pages.dev/](https://sunsafeaus.pages.dev/).

## Frontend: Vue.js Multi-Page Application

The frontend is crafted as a multi-page application (MPA) using Vue.js, offering a seamless and interactive user experience. Key features include:

- **Personalized Recommendations**: Users input their skin type, skin tone, activity level, and location to receive tailored sun safety advice.
- **Downloadable Reminders**: The application allows users to download `.ics` files, enabling them to set up reminders in their personal calendars for activities like sunscreen reapplication.
- **Responsive Design**: Ensures optimal usability across various devices, including desktops, tablets, and mobile phones.

**Deployment Details**:

- **Platform**: Cloudflare Pages, facilitating efficient global content delivery.
- **Build Process**: Utilizes Vue CLI for project scaffolding and building. The production build is optimized and served via Cloudflare's global content delivery network (CDN), ensuring low latency and high availability.
- **Continuous Deployment**: Integrated with a Git repository; any commits to the main branch trigger automatic builds and deployments, facilitating seamless updates.

## Backend: FastAPI Application

The backend is developed using FastAPI, known for its high performance and ease of use. It serves as the application's API layer, handling user input, processing data, and interacting with external services. Key integrations include:

- **Environmental Data Integration**: Incorporates real-time weather data from Ambee's Weather API to enhance the accuracy of sun safety recommendations.

**Deployment Details**:

- **Platform**: Render, a modern cloud platform for web applications.
- **Application Server**: Utilizes Gunicorn in conjunction with Uvicorn workers to serve the FastAPI application, ensuring efficient request handling and concurrency.
- **Continuous Deployment**: Connected to the Git repository; pushes to the main branch automatically trigger deployments, ensuring the backend remains up-to-date with the latest codebase.

## Database: PostgreSQL on AWS RDS

The application employs PostgreSQL for data storage, chosen for its robustness and advanced feature set. AWS RDS manages the database, offering automated backups, patching, and scaling, which reduces the operational overhead associated with database maintenance.

**Deployment Details**:

- **Platform**: Amazon Web Services Relational Database Service (RDS), providing scalable and managed PostgreSQL instances.
- **Security**: Implements AWS Identity and Access Management (IAM) roles and security groups to control access to the database.
- **Backup and Recovery**: Configured automated backups and multi-AZ deployments to ensure data durability and high availability.

## Environment Configuration

Environment variables are utilized across the application to manage configuration settings securely. Sensitive information, such as database connection strings, API keys (e.g., for Ambee's Weather API), and secret tokens, are stored in environment variables to prevent exposure in the codebase. Both Render and Cloudflare Pages provide interfaces to manage these variables, ensuring that deployment environments are consistently and securely configured.

## Security Considerations

Security best practices have been implemented throughout the application:

- **Data Transmission**: All data exchanged between the frontend, backend, and database is encrypted using HTTPS and SSL/TLS protocols to prevent interception and tampering.
- **Input Validation**: The backend performs rigorous validation and sanitization of user inputs to protect against injection attacks and ensure data integrity.
- **Access Control**: Role-based access controls are enforced to restrict administrative functionalities to authorized personnel only.

## Monitoring and Logging

To maintain the application's health and performance:

- **Monitoring**: Render provides monitoring tools to track the performance and uptime of the backend services. Additionally, AWS CloudWatch is configured to monitor database performance metrics.
- **Logging**: Structured logging is implemented in both the frontend and backend to capture and analyze application events, aiding in debugging and performance tuning.

## Conclusion

This project leverages modern web development frameworks and cloud services to deliver a responsive and reliable application. The integration of Vue.js, FastAPI, PostgreSQL, Cloudflare Pages, Render, AWS RDS, and Ambee's Weather API ensures a scalable architecture capable of providing users with timely and personalized sun safety recommendations.

For further details on deploying FastAPI applications to Render, consult Render's official documentation.

For guidance on integrating Ambee's Weather API, refer to Ambee's official API documentation.
