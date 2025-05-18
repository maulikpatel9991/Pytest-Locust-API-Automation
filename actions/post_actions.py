import allure
import json
from actions import base_actions
import requests
from faker import Faker


fake = Faker()

@allure.step("Create user post with title: {title} and job: {post_body}")
def create_posts(title, post_body, client, **kwargs):
    """
    Sends a POST request to create a user.

    Args:
        title (str): The name of the user (e.g., a fake name).
        post_body (str): The job or description associated with the user.
        client: Locust's HttpUser.client instance.
        **kwargs: Optional parameters like `headers`, `catch_response`, etc.

    Returns:
        Response object (LocustResponse) from the /users endpoint.
    """
    # Create the request body as a JSON string
    body = json.dumps({
        "name": title,
        "job": post_body
    })

    # Send POST request using the shared base_actions helper
    return base_actions.post(client, "/users", data=body, **kwargs)

