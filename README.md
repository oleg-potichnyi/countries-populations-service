# Countries populations service

This service retrieves and displays population data for countries grouped by region.

## Technology stack
* Python 3.10
* FastAPI
* SQLAlchemy
* BeautifulSoup
* Requests
* Pydantic

## Installation

Python3 must be already installed

```shell
* Сreate venv: "python3 -m venv venv"
# Activate the virtual environment on Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
* Install requirements: "pip install -r requirements.txt"
* Navigate to the project directory: cd countries_populations_service
* Build and run the Docker containers: docker-compose up --build
```

## Usage

### Retrieving Data
To retrieve and store population data for countries:
- Send a POST request to `/get_data`.

### Printing Data
To display summary data by region:
- Send a GET request to `/print_data`.
