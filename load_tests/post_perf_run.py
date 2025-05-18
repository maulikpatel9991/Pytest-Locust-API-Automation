from locust import HttpUser, between, task
from utils.configutils import get_environment
from actions import post_actions as posts
from faker import Faker

# Initialize Faker to generate fake data
fake = Faker()

class PostPerformanceTests(HttpUser):
    """
    A Locust test class for performance testing of POST requests.
    
    This class simulates a user creating a post (user data) through the API.
    The goal is to assess how the API handles POST requests and ensure performance 
    under load.
    """
    
    # Define the wait time between task executions (0.3 to 0.8 seconds)
    wait_time = between(0.3, 0.8)
    
    # Dynamically retrieve the host URL from the environment configuration.
    # Alternatively, this could be hardcoded (e.g., host = "https://reqres.in/api").
    host = get_environment().get("host_url")
    
    @task
    def create_user_post(self):
        """
        Task to create a user by sending a POST request to the API.
        
        This task generates random user data (name and job) and sends it to the 
        API endpoint. The response is checked for a successful creation (HTTP status 201).
        """
        # Generate random data for the user (name and job)
        post_title = fake.name()  # Random user name
        post_body = fake.sentence()  # Random job title or description
        
        # Call the create_posts function from the `post_actions` module, 
        # sending the generated data to the API.
        response = posts.create_posts(
            post_title, post_body, client=self.client, catch_response=True
        )

        # If the response status is 201 (Created), no action is needed. 
        # You can log, assert, or handle the response as needed.
        if response and response.status_code == 201:
            pass  # Optional: Could log success or assert response values here.
