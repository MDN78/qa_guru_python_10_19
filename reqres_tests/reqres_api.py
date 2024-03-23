import requests


class ReqresApi:

    def __init__(self, url):
        self.url = url

    def get_users_list(self, page=2) -> list:
        my_param = {
            "page": page
        }
        resp = requests.get(f'{self.url}users', params=my_param)
        status_code = resp.status_code
        return [resp.json(), status_code]

    def get_single_user(self, user_id: str) -> list:
        resp = requests.get(f'{self.url}users/{user_id}')
        status_code = resp.status_code
        return [resp.json(), status_code]

    def get_resource_list(self) -> list:
        resp = requests.get(f'{self.url}unknown')
        status_code = resp.status_code
        return [resp.json(), status_code]

    def get_resource_list_by_id(self, date: str) -> list:
        resp = requests.get(f'{self.url}unknown/{date}')
        status_code = resp.status_code
        return [resp.json(), status_code]

    def create_new_user(self, first_name: str, last_name: str, job: str) -> list:
        payload = {
            "first_name": first_name,
            "last_name": last_name,
            "job": job
        }
        resp = requests.post(f'{self.url}users', json=payload)
        status_code = resp.status_code
        return [resp.json(), status_code]

    def update_user_info(self, name: str, job: str) -> list:
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

    def registration_user(self, email: str, password: str) -> list:
        payload = {
            'email': email,
            'password': password
        }
        resp = requests.post(f'{self.url}register', json=payload)
        status_code = resp.status_code
        user_id = str(resp.json()['id'])
        return [user_id, status_code]

    def unsuccessful_registration_user(self, email: str) -> list:
        payload = {
            'email': email
        }
        resp = requests.post(f'{self.url}register', json=payload)
        status_code = resp.status_code
        user_info = resp.json()
        return [user_info, status_code]

    def login_user(self, email, password):
        payload = {
            'email': email,
            'password': password
        }
        resp = requests.post(f'{self.url}login', json=payload)
        status_code = resp.status_code
        user_token = resp.json()['token']
        return [user_token, status_code]


api = ReqresApi("https://reqres.in/api/")
