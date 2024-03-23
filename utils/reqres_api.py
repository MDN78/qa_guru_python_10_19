import requests
import json
from jsonschema import validate
from reqres_tests import resource


class ReqresApi:

    def __init__(self, url):
        self.url = url

    def get_users_list(self, page=2):
        my_param = {
            "page": page
        }
        resp = requests.get(f'{self.url}users', params=my_param)
        status_code = resp.status_code
        return [resp.json(), status_code]

    def get_single_user(self, user_id):
        resp = requests.get(f'{self.url}users/{user_id}')
        status_code = resp.status_code
        return [resp.json(), status_code]

    def validator_json_schemas(self, name, page=2):
        my_param = {
            "page": page
        }
        response = requests.get(f'{self.url}users', params=my_param)

        schema = json.load(open(resource.path_log_file(file_name=name)))
        validate(response.json(), schema)


api = ReqresApi("https://reqres.in/api/")
