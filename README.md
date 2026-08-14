# Automated API Testing Framework

A reusable automated testing framework for Flask REST APIs using Pytest.

## Features

- Flask test client
- Pytest fixtures
- Isolated test database
- API validation tests
- Duplicate-data tests
- Product API tests
- Code coverage

## Technologies

- Python
- Flask
- SQLAlchemy
- Pytest
- Pytest-Cov
- SQLite

## Installation

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Coverage

```bash
pytest --cov=app
```

## HTML Coverage

```bash
pytest --cov=app --cov-report=html
```

## Purpose

Day 301 introduces automated API testing and prepares Flask applications for CI/CD pipelines.
