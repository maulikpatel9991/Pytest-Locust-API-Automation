import pytest
import allure
import requests
from actions import get_actions as get
from faker import Faker

fake = Faker()


@pytest.mark.get
def test_get_all_posts():
    session = requests.Session()
    result = get.get_user_api(session)
    print(result.json())
    assert result.status_code == 200
    
    