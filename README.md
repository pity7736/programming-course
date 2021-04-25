# Programming Course

This repo is for teach programing and doing exercises in python.

## Workflow

1. Get new changes from repo:
    1. `git pull origin main`.
1. Program exercises
1. Commit changes.

## Python Exercises

### Setup dev environment

1. Install [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
1. Create virtual environment: `mkvirtualenv -a . -p $(which python3.8) env_name`. **env_name** is the environment name, you can use whatever.
1. Install requirements: `pip install -r requirements.txt`


### Testing

We are using [pytest framework](https://docs.pytest.org/en/stable/index.html) to write/run tests.

1. Run all tests: `pytest`
    1. You can add verbosity adding `-v`. Example: `pytest -v` or `pytest -vvv` for more verbosity.
1. Run specific test: `pytest path/to/test_file:test_name`
1. Run tests with coverage: `pytest -vvv --cov=src --cov-report term-missing tests`
1. See [pytest usage](https://docs.pytest.org/en/stable/usage.html) for more information. 
