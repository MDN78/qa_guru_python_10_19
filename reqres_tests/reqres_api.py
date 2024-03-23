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

    def create_new_user(self, first_name, last_name, job):
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "job": job
        }
        resp = requests.post(f'{self.url}users', json=payload)
        status_code = resp.status_code
        return [resp.json(), status_code]

    def update_user_info(self, name, job):
        payload = {
            "name": name,
            "job": job,
        }
        resp = requests.put(f'{self.url}users/2', json=payload)
        status_code = resp.status_code
        return [resp.json(), status_code]

    def delete_user(self, user_id=2):
        resp = requests.delete(f'{self.url}users/{user_id}')
        status_code = resp.status_code
        status = f'{resp.text}deleted'
        return [status, status_code]


api = ReqresApi("https://reqres.in/api/")
