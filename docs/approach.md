# Quality-First Calculator API

The goal is to build a production-ready REST API that emphasizes maintainability and testability.

## Test-Driven Development (TDD)
Follow a Red-Green-Refactor cycle, committing tests before implementation to ensure high coverage and QA-centric mindset

## Layered Architecture
Separate the API Routing (FastAPI) from the Business Logic (Calculator Service) to ensure code remain clean and easy to extend.

## DevOps & Portability
The application is fully containerized using Docker and managed via Poetry to ensure it runs with a single command on any machine.

## Extensibility
Implementing an in-memory history feature to demonstrate how the system can handle stateful operations in a stateless API environment.