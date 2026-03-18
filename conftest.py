import pytest
from utils.api_client import APIClient

BASE_URL = "https://qa-testing-navy.vercel.app"
CANDIDATE_ID = "rohitchoukiker2803@gmail.com"

@pytest.fixture(scope="session")
def client():
    api = APIClient(BASE_URL, CANDIDATE_ID)
    res = api.auth()
    
    if res.status_code != 200:
        print("Auth not stable, continuing for testing")
    
    return api