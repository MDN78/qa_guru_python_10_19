import os
from utils.validator_json import validator_all_json_schemas
from utils.reqres_api import api


def test_validate_resource_schema():
    validator_all_json_schemas('create', 'create_new_user_schema.json')


def test_create_new_user():
    name = os.getenv('NEW_USER_FIRST_NAME')
    surname = os.getenv('NEW_USER_LAST_NAME')
    job = os.getenv('NEW_USER_JOB')
    new_user = api.create_new_user(name, surname, job)
    status_code = new_user[1]
    assert status_code == 201
    assert new_user[0]["first_name"] == name


def test_update_user_info():
    name = os.getenv('NEW_USER_FIRST_NAME')
    job = os.getenv('NEW_USER_JOB')
    new_user = api.update_user_info(name, job)
    status_code = new_user[1]
    assert status_code == 200
    assert new_user[0]["name"] == name


def test_delete_user_by_id():
    delete_user = api.delete_user()
    status_code = delete_user[1]
    assert delete_user[0] == 'deleted'
    assert status_code == 204
