import requests


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

    def get_resource_list(self):
        resp = requests.get(f'{self.url}unknown')
        status_code = resp.status_code
        return [resp.json(), status_code]

    def get_resource_list_by_id(self, date):
        resp = requests.get(f'{self.url}unknown/{date}')
        status_code = resp.status_code
        return [resp.json(), status_code]


api = ReqresApi("https://reqres.in/api/")
