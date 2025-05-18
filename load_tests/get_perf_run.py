from locust import HttpUser, between, task
from utils.configutils import get_environment
from actions import post_actions as posts
from actions import get_actions as gets
from faker import Faker

fake = Faker()

class GetPerformanceTests(HttpUser):
    """
    A Locust test class for performance testing of GET requests.

    This class simulates a user interacting with an API by sending GET requests 
    to fetch data (e.g., a list of users).
    """
    
    # Define the wait time between tasks (0.3 to 0.8 seconds)
    wait_time = between(0.3, 0.8)
    
    # Get the host URL from the environment config (can also be hardcoded here)
    host = get_environment().get("host_url")
    
    @task
    def get_all_users(self):
        """
        Sends a GET request to retrieve all users from the API.

        This task simulates the action of fetching user data from the API.
        The response is captured for further validation (status code check, response body, etc.).
        """
        # Calls the `get_user` function from the `get_actions` module
        gets.get_user(client=self.client, catch_response=True)
