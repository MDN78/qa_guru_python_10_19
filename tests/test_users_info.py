from utils.reqres_api import api
import requests

def test_get_users_list():
    user_page = '1'
    users_list = api.get_users_list(user_page)
    assert users_list['page'] == int(user_page)


def test_users():
    response = requests.get('https://reqres.in/api/users?page=2')
    print(response.text)