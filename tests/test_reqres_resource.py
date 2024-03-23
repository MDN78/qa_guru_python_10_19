from reqres_tests.reqres_api import api
from utils.validator_json import validator_all_json_schemas


def test_validate_resource_schema():
    validator_all_json_schemas('recource', 'resource_scheme.json')


def test_get_resource_list():
    response = api.get_resource_list()
    status_code = response[1]
    assert response[0]['total'] == 12
    assert status_code == 200


def test_get_single_resource_list_by_id(resource_list):
    single_resource = api.get_resource_list_by_id(resource_list['data'][1]['id'])
    id_single_resource = single_resource[0]['data']['id']
    status_code = single_resource[1]
    assert id_single_resource == 2
    assert status_code == 200


def test_get_single_resource_list_by_id_non_found():
    single_resource = api.get_resource_list_by_id('23')
    status_code = single_resource[1]
    assert single_resource[0] == {}
    assert status_code == 404
