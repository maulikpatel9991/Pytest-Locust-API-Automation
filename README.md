# Introduction

This is a sample project to showcase how API functional test automation can be performed with Python & Pytest framework.

The APIs defined for the functional tests are then reused to run performance & load tests using the locust framework.

For further information on pytest, take a look at https://docs.pytest.org/en/stable/

For further information on locust, take a look at https://locust.io/

# Project Setup

This project is build with `python 3.10`

Once your python environment is setup, you need to install the required packages by running

```
pip install -r requirements.txt
```

## Functional Tests

To run functional tests run

```
pytest
```

## Performance Tests

### In the GUI Mode

To run the performance tests run in the UI

```
locust -f load_tests/post_perf_run.py
```


## Framework Organization

```
├── README.md
├── actions
│   ├── base_actions.py     - Base API actions for all other actions file
│   └── post_actions.py     - API actions related to posts feature
│   └── get_actions.py     - API actions related to posts feature
├── utils
│   ├── commonutils.py           - Common Methods
│   ├── configutils.py           - Environment configs
├── locust_headless.conf    - locust headless execution configs
├── .env                    - Environments Setups
├── locustfile.py           - Execution All testcase
├── load_tests
│   ├── post_perf_run.py    - Performance test file
│   ├── get_perf_run.py     - Performance test file
├── e2e_tests
│   ├── get_crud_test.py    - e2e functional test file
├── requirements.txt        - Required python libraries
```