# Airbnb Clone Project

Welcome to the AirBnB clone project!

THIS PROJECT IS A TEAM PROJECT BY DANIEL NTOW AND JOEJO TURKSON


## Overview
This project is an Airbnb clone developed as part of [Project Title]. It aims to replicate the core functionality of the Airbnb platform.


## Project Structure
The project is organized into the following components:

- **models**: Contains the data models for different entities (e.g., BaseModel, User, Place).
- **console**: Implements the command-line interface for interacting with the application.
- **tests**: Includes unit tests for various functionalities.


## Testing
Ensure the correctness of the application by running unit tests. Use the following command:
```bash
python -m unittest discover tests

```



Before starting, please read the AirBnB concept page.


# instructions
First step: Write a command interpreter to manage your AirBnB objects.

This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
create the first abstracted storage engine of the project: File storage.
create all unittests to validate all our classes and storage engine

How to create a Python package
How to create a command interpreter in Python using the cmd module
What is Unit testing and how to implement it in a large project
How to serialize and deserialize a Class
How to write and read a JSON file
How to manage datetime
What is an UUID
What is *args and how to use it
What is **kwargs and how to use it
How to handle named arguments in a function
