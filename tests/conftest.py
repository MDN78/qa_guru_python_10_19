import pytest
from dotenv import load_dotenv
import requests


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture
def resource_list():
    resp = requests.get('https://reqres.in/api/unknown')
    return resp.json()
