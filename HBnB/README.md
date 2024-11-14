
# New HBnB V2

This project is a simulation of a rental platform similar to HBnB. In this application, users can:
- Create and manage accounts.
- Create and list amenities.
- Create places.
- Leave reviews for the places they visit.

Data is stored in a database using **SQLAlchemy**, which supports CRUD operations to save and manage users, amenities, places, and reviews.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Architecture](#project-architecture)
4. [File Structure](#file-structure)
5. [Requirements](#requirements)
6. [Authors](#authors)

## Installation

1. Clone the repository:
    ```bash
    git clone <REPOSITORY_URL>
    cd hbnb
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your database environment variables (if applicable) in the `config.py` file.

## Usage

To run the project, open a terminal and execute the following command:

```bash
python3 run.py
```

## Project Architecture

The project follows a three-layer architecture pattern, which helps keep the code organized, scalable, and modular:

- **Presentation Layer (API)**: Manages HTTP requests and responses.
- **Business Logic Layer (Services)**: Handles business logic and coordinates operations between models.
- **Persistence Layer (Repository)**: Interacts with the database to perform storage and retrieval operations.

## File Structure

```plaintext
hbnb/
├── app/
│   ├── __init__.py                 # Main module initialization
│   ├── api/
│   │   ├── __init__.py             # API initialization
│   │   ├── v1/                     # API versioning (version 1)
│   │       ├── __init__.py         # API v1 initialization
│   │       ├── users.py            # Endpoints for handling users
│   │       ├── places.py           # Endpoints for handling places
│   │       ├── reviews.py          # Endpoints for handling reviews
│   │       ├── amenities.py        # Endpoints for handling amenities
│   ├── models/                     # Data model definitions
│   │   ├── __init__.py             # Models initialization
│   │   ├── user.py                 # User model
│   │   ├── place.py                # Place model
│   │   ├── review.py               # Review model
│   │   ├── amenity.py              # Amenity model
│   ├── services/                   # Services managing business logic
│   │   ├── __init__.py             # Services initialization
│   │   ├── facade.py               # Facade class for simplified logic handling
│   ├── persistence/                # Data persistence management
│       ├── __init__.py             # Persistence initialization
│       ├── repository.py           # Repositories for database interaction
├── run.py                          # Main file to run the app
├── config.py                       # Application configurations
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
```

## Requirements

- Python 3.x
- SQLAlchemy
- Flask (or the framework used for the API)

All specific requirements are listed in `requirements.txt`. Install them by running `pip install -r requirements.txt`.

## Authors

- [Author 1 Name](https://github.com/author1)
- [Author 2 Name](https://github.com/author2)

---

This README provides a clear and organized overview of the project, explaining how to install, run, and understand its structure to make it easy to use and navigate.
