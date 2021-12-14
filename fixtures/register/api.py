import logging

from requests import Response
import requests
import cattr

from common.custom_log import custom_looger
from fixtures.register.models import RegisterUserResponse

from common.deco import logging as log



class Register:
    def __init__(self, app):
        self.app = app

    POST_REGISTER = '/register'

    @log('Register new user')
    def register(self, data, type_response=RegisterUserResponse) -> Response:
        res = requests.post(f"{self.app.url}{self.POST_REGISTER}", json=data.to_dict())
        res.custom_response = cattr.structure(res.json(), type_response)
        # custom_looger(res)
        return res
