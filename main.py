import requests
import json


class MySession(requests.Session):
    def __init__(self, *, url: str, username: str, password: str, params: dict = None):
        super().__init__()
        self.url = url
        self.username = username
        self.password = password
        self.auth = (self.username, self.password)
        self.params = params
        self.headers["Content-Type"] = "application/json"

    def get_response(self):
        response = self.get(self.url, headers=self.headers, params=self.params)
        return response.json()

    def print_response(self):
        try:
            response = self.get_response()
            print(json.dumps(response, indent=4))
        except json.JSONDecodeError as e:
            print(f"Failed to decode response: {e.msg}\nResponse Text: {e.doc}")