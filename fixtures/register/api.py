from requests import Response
import cattr

from fixtures.register.models import RegisterUserResponse

from common.deco import logging as log


class Register:
    def __init__(self, app):
        self.app = app

    POST_REGISTER = '/register'

    @log('Register new user')
    def register(self, data, type_response=RegisterUserResponse) -> Response:
        res = self.app.client.request(method='POST', url=f"{self.app.url}{self.POST_REGISTER}", json=data.to_dict())
        res.custom_response = cattr.structure(res.json(), type_response)
        return res
