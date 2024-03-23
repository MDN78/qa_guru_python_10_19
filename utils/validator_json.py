import json
import requests
from jsonschema import validate
from reqres_tests import resource

url = 'https://reqres.in/api/'

def validator_all_json_schemas(date, name, page=2):
    if date == 'users':
        my_param = {
            "page": page
        }
        response = requests.get(f'{url}users', params=my_param)

        schema = json.load(open(resource.path_log_file(file_name=name)))
        validate(response.json(), schema)
    elif date == 'resource':
        response = requests.get(f'{url}unlnown')
        schema = json.load(open(resource.path_log_file(file_name=name)))
        validate(response.json(), schema)
    elif date == 'create':
        payload = {
            'name': 'Tom',
            'job': 'student'
        }
        response = requests.post(f'{url}users', json=payload)
        schema = json.load(open(resource.path_log_file(file_name=name)))
        validate(response.json(), schema)