from utils.reqres_api import api
import os

from utils.validator_json import validator_all_json_schemas


def test_validate_users_schema():
    validator_all_json_schemas('users', 'users_schema.json')


def test_get_users_list():
    user_page = '1'
    response = api.get_users_list(user_page)
    status_code = response[1]
    assert response[0]['page'] == int(user_page)
    assert status_code == 200


def test_get_single_user_info():
    user_ids = os.getenv('USER_ID')
    response = api.get_single_user(user_ids)
    status_code = response[1]
    assert response[0]['data']["email"] == os.getenv('USER_EMAIL')
    assert response[0]['data']['first_name'] == os.getenv('USER_FIRST_NAME')
    assert response[0]['data']['last_name'] == os.getenv('USER_LAST_NAME')
    assert status_code == 200


def test_get_single_unknown_user_info():
    user_ids = os.getenv('UNKNOWN_USER_ID')
    response = api.get_single_user(user_ids)
    status_code = response[1]
    assert response[0] == {}
    assert status_code == 404
