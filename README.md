# CloudKart - DevOps CI/CD & Containerization

This repository contains the deployment automation and microservice architecture for the CloudKart application. The project demonstrates continuous integration, unit testing, and container delivery using GitHub Actions and Docker.

## Tech Stack
•⁠  ⁠*Language/Framework:* Python 3.11 / Flask API
•⁠  ⁠*Unit Testing:* PyTest
•⁠  ⁠*Containerization:* Docker (Slim Base Image)
•⁠  ⁠*CI/CD:* GitHub Actions Workflows

## Project Structure
•⁠  ⁠⁠ app.py ⁠: Main Flask microservice exposing status and health check endpoints.
•⁠  ⁠⁠ test_app.py ⁠: Automated PyTest suite for route verification.
•⁠  ⁠⁠ Dockerfile ⁠: Multi-stage build configuration for container delivery.
•⁠  ⁠⁠ requirements.txt ⁠: Python runtime libraries and dependencies.
•⁠  ⁠⁠ .github/workflows/devops-pipeline.yml ⁠: Automated CI/CD pipeline triggering on push and PR.

## Local Execution
To build and run the application container locally:

1.⁠ ⁠Build the Docker image:
   docker build -t cloudkart-service .

2.⁠ ⁠Run the application container:
   docker run -p 5000:5000 cloudkart-service
