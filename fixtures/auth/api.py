from requests import Response
import requests
import cattr

from fixtures.auth.model import AuthResponse
from fixtures.register.models import RegisterUserResponse

from common.deco import logging as log



class Auth:
    def __init__(self, app):
        self.app = app

    POST_AUTH = '/auth'

    @log('Auth user')
    def login(self, data, type_response=AuthResponse) -> Response:
        res = requests.post(f"{self.app.url}{self.POST_AUTH}", json=data.to_dict())
        res.custom_response = cattr.structure(res.json(), type_response)
        return res
