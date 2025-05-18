import allure
import json
from actions import base_actions
import requests
from faker import Faker

fake = Faker()

def get_user(client, **kwargs):
    """
    Sends a GET request to retrieve a list of users.

    Args:
        client: Locust's HttpUser.client instance.
        **kwargs: Optional parameters like `headers`, `params`, or `catch_response`.

    Returns:
        Response object (LocustResponse) from the /users endpoint.
    """
    return base_actions.get(client, "/users", **kwargs)

def get_user_api(client, **kwargs):
    """
    Sends a GET request to retrieve a list of users.

    Args:
        client: Locust's HttpUser.client instance.
        **kwargs: Optional parameters like `headers`, `params`, or `catch_response`.

    Returns:
        Response object (LocustResponse) from the /users endpoint.
    """
    return base_actions.get_api(client, "/users", **kwargs)