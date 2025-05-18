from environs import Env
import yaml

env = Env()
env.read_env()

def load_config(env: str) -> dict:
    f"""
    Function to load configuration settings based on the specified environment.
    Parameters:
    - env (str): The environment for which configuration settings are to be loaded.
    Returns:
    - dict: A dictionary containing configuration settings for the specified environment.
    """

    with open('config.yml', 'r') as file:
        config = yaml.safe_load(file)
        return config.get(env, {})



def get_environment():
    """Retrieve environment variables"""
    app_env = load_config(env("app_env", "local"))
    print(f"""Tests will be run against {app_env} environment""")
    return app_env
