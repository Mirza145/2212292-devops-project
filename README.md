# DevOps Final Project

**Name:** Mirza Mashood ul Hassan  
**Registration Number:** 2212292  

## Project Overview
This repository contains a production-ready, containerised microservice application built for the DevOps Fundamentals final project. It features a complete CI/CD pipeline automating testing, building, and deployment to an AWS EC2 instance.

## Architecture Description
The architecture consists of the following components:
* **Web Service:** A REST API built with **FastAPI** and served via **Uvicorn** on port 8000.
* **Database:** A **PostgreSQL 15** database running on port 5432, utilizing a named Docker volume (`postgres_data`) for data persistence.
* **Containerization:** Both the web service and database are containerised using **Docker** and orchestrated locally and in production using **Docker Compose**.
* **Continuous Integration (CI):** Powered by **GitHub Actions**. On every push and pull request, the pipeline automatically lints the code using `flake8` and runs the test suite using `pytest` with an isolated SQLite test database.
* **Continuous Deployment (CD):** On every push to the `main` branch, the CD pipeline builds a new Docker image, pushes it to Docker Hub, and uses SSH to connect to an **AWS EC2** (Ubuntu) instance. It then pulls the latest image and seamlessly restarts the production containers using a `.env` file.

## API Endpoints
* `GET /health` - Health check endpoint returning the database connection status and registration number.
* `POST /students` - Creates a new student record in the database.
* `GET /students` - Retrieves a list of all students.
* `GET /students/{reg_no}` - Retrieves a specific student by their registration number.

## Setup Instructions

### Prerequisites
* Docker
* Docker Compose
* Git

### Local Development
1. Clone the repository:
   ```bash
   git clone [https://github.com/Mirza145/2212292-devops-project.git](https://github.com/Mirza145/2212292-devops-project.git)
   cd 2212292-devops-project
