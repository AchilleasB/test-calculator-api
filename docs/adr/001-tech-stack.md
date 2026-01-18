# 1. Tech Stack

## Context 
The system is a versioned REST API that is production-ready, easily testable. and maintainable.

## Decision

### Language
Python for its readability and strong support for math and automation libraries.

### Framework
Fast API for its native support for Pydantic (data validation), asynchronous capabilities, and automatic Swagger documentation generation.

### Dependency Management
Poetry sits on top of *pip* managing dependencies more comprehensively by tracking exact versions, managing virtual environments, building packages and etc.

### Testing
Pytest is the primary testing framework due to its powerful fixture system and compatibility with FastAPI's *TestClient*