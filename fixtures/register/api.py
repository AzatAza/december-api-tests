from requests import Response
import requests


class Register:
    def __init__(self, app):
        self.app = app

    POST_REGISTER = '/register'

    def register(self, data) -> Response:
        return requests.post(f"{self.app.url}{self.POST_REGISTER}", json=data.to_dict())