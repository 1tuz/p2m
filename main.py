import requests
import json
from params import Params


class MySession(requests.Session):
    def __init__(self, url, username, password, params=Params()):
        super().__init__()
        self.url = url
        self.username = username
        self.password = password
        self.headers = {
            'Content-Type': 'application/json',
        }
        self.auth = (self.username, self.password)
        self.params = params

    def get_response(self):
        response = self.get(self.url, headers=self.headers, params=self.params.get_params())
        return response.json()

    def print_response(self):
        response = self.get_response()
        print(json.dumps(response, indent=4))
