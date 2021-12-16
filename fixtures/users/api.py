from requests import Response
import requests

from fixtures.auth.model import AuthResponse

from common.deco import logging as log



class User:
    def __init__(self, app):
        self.app = app

    POST_ADD_USER_INFO = '/user_info/{}'

    @log('Add user info')
    def add_user_info(self, user_id,  data, token=None, type_response=AuthResponse) -> Response:
        headers = {"Authorization": f"JWT {token}"}
        res = requests.post(f"{self.app.url}{self.POST_ADD_USER_INFO.format(user_id)}", json=data.to_dict(), headers=headers)
        # res.custom_response = cattr.structure(res.json(), type_response)
        return res
