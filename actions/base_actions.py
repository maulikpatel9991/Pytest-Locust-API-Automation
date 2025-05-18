import requests  # Not used here unless needed elsewhere (e.g., for setup)
import allure
from utils.configutils import get_environment

# Load environment configuration
env = get_environment()
host_url = env.get("host_url")

def get(client, path, **kwargs):
    """
    Sends an HTTP GET request using the provided Locust client.

    Args:
        client: Locust's HttpUser.client instance.
        path (str): API path (relative to base host).
        **kwargs: Additional request options like params, headers, etc.

    Returns:
        Response object (LocustResponse)
    """
    catch_response = kwargs.pop("catch_response", False)

    if catch_response:
        with client.get(path, catch_response=True, **kwargs) as response:
            return response  # You can add more handling if needed
    else:
        return client.get(path, **kwargs)


def post(client, path, **kwargs):
    """
    Sends an HTTP POST request using the provided Locust client.

    Args:
        client: Locust's HttpUser.client instance.
        path (str): API path (relative to base host).
        **kwargs: Additional request options like data, headers, etc.

    Returns:
        Response object (LocustResponse)
    """
    catch_response = kwargs.pop("catch_response", False)

    # Default headers
    headers = kwargs.pop("headers", {})
    headers.setdefault("Content-Type", "application/json")
    headers.setdefault("x-api-key", "reqres-free-v1")  # Required API key

    if catch_response:
        with client.post(path, headers=headers, catch_response=True, **kwargs) as response:
            return response  # Customize handling based on status_code if needed
    else:
        return client.post(path, headers=headers, **kwargs)


def get_api(client, path, **kwargs):
    """
    Handles GET request for both Locust and Pytest.

    Args:
        client: Either Locust's client or a requests.Session object.
        path (str): API endpoint path.
        **kwargs: Optional arguments like params, headers, etc.

    Returns:
        Response object (requests.Response or LocustResponse)
    """
    url = f"{host_url}{path}"
    catch_response = kwargs.pop("catch_response", False)

    if hasattr(client, 'get'):  # Locust or requests.Session both have .get()
        if catch_response and hasattr(client.get, '__call__'):
            with client.get(path, catch_response=True, **kwargs) as response:
                return response
        else:
            return client.get(url, **kwargs)
    else:
        raise ValueError("Unsupported client type")
