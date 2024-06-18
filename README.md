# Template for API in Flask

## Overview

This base project contains a scaffold for building a Flask API with the following features:

- Logging
- Testing
- Caching
- Containerization
- Linting verification
- CI/CD Integration

## Features

- **Logging:** Configured to output logs to both the terminal and a log file.
- **Testing:** Uses `pytest` for testing, with fixtures and examples.
- **Caching:** Configured with Flask-Caching for efficient data handling.
- **Containerization:** Ready to be containerized with Docker.
- **Linting:** Integrated with `flake8` for code style checking.
- **CI/CD:** Setup for continuous integration and deployment on AWS.

## Setup Environment

1. Set the local Python version:

   ```bash
   pyenv local 3.12
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   ```bash
   source ./venv/bin/activate
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   gunicorn --bind 0.0.0.0:8080 app:app
   ```

## Running Tests

If `pytest` does not recognize the `src` folder as a module, use the following command to set the `PYTHONPATH`:

```bash
export PYTHONPATH=$(pwd)
```

Run the tests with:

```bash
pytest
```

## Lint Check

Check the code style with `flake8`:

```bash
flake8 .
```

## Running with Gunicorn

To run the application using Gunicorn:

```bash
gunicorn --bind 0.0.0.0:8000 app:app
```

To build and run the Docker container:

```bash
docker build -t template-api:v1 .
docker run -p 8000:8000 --env-file .env template-api:v1
```

## CI/CD Integration

For continuous integration and deployment, we utilize GitHub Actions. Our setup includes refreshing the AWS ECR image and triggering AWS App Runner to refresh its service source.

### Variables that need to be set in GitHub Secrets:
- AWS_ACCESS_KEY_ID
- AWS_ACCOUNT_ID
- AWS_REGION
- AWS_SECRET_ACCESS_KEY

### If you update or install some library

To update the libraries requirements, run:

```bash
pip freeze > requirements.txt
```