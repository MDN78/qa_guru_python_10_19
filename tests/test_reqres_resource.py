from utils.reqres_api import api
import os


def test_get_resource_list():
    response = api.get_resource_list()
    status_code = response[1]
    assert response[0]['total'] == 12
    assert status_code == 200


def test_get_single_resource_list_by_id(resource_list):
    single_resource = api.get_resource_list_by_id(resource_list['data'][1]['id'])
    id_single_resource = single_resource[0]['data']['id']
    assert id_single_resource == 2
