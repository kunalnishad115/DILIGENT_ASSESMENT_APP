
# AI Notes

I used ChatGPT as a development assistant during this assignment. The goal was to speed up development while making sure I understood every part of the implementation before keeping it in the project.

## What AI helped with

* Discussing the overall project structure
* Designing a layered architecture
* Suggesting improvements to repository and service organization
* Reviewing code for readability and consistency
* Generating initial versions of some helper functions and test cases
* Reviewing error handling and logging approach

## What I implemented and verified myself

* Implemented the project using FastAPI
* Connected all layers (routes, services, repository, models, and schemas)
* Fixed runtime issues while integrating different modules
* Adjusted validation logic based on application behavior
* Corrected JSON file handling and persistence
* Wrote and modified tests until all test cases passed
* Verified API behavior manually using Swagger
* Ran Ruff formatting and lint checks
* Ran Pytest and confirmed all tests passed with high coverage

## Changes made to AI suggestions

Several AI-generated suggestions were modified before being used:

* Simplified some implementations to keep the project aligned with the assignment requirements.
* Avoided adding unnecessary abstractions that would increase complexity.
* Refactored parts of the service layer for better readability.
* Updated logging messages and exception handling after testing.

## AI suggestions not used

Some suggestions were intentionally not implemented, including:

* Database integration
* Authentication
* Response wrapper objects
* Docker support
* Generic repository abstraction

These ideas could improve a larger production application but were outside the scope of this assignment, which requested a lightweight REST API with local storage.
