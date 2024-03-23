import requests


class ReqresApi:

    def __init__(self, url):
        self.url = url

    # def get_users_list(self, page=2):
    #     resp = requests.get(f'{self.url}users?page={page}')
    #     return resp.json()

    def get_users_list(self, page=2):
        my_param = {
            "page": page
        }
        resp = requests.get(f'{self.url}users', params=my_param)
        return resp.json()


api = ReqresApi("https://reqres.in/api/")
