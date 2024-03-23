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

    def validator_all_json_schemas(self, date, name, page=2):
        if date == 'users':
            my_param = {
                "page": page
            }
            response = requests.get(f'{self.url}users', params=my_param)

            schema = json.load(open(resource.path_log_file(file_name=name)))
            validate(response.json(), schema)
        elif date == 'resource':
            response = requests.get(f'{self.url}unlnown')
            schema = json.load(open(resource.path_log_file(file_name=name)))
            validate(response.json(), schema)

    def get_resource_list(self):
        resp = requests.get(f'{self.url}unknown')
        status_code = resp.status_code
        return [resp.json(), status_code]

    def get_resource_list_by_id(self, date):
        resp = requests.get(f'{self.url}unknown/{date}')
        status_code = resp.status_code
        return [resp.json(), status_code]


api = ReqresApi("https://reqres.in/api/")
