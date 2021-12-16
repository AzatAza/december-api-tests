from fixtures.constants import ResponseText
from fixtures.register.models import RegisterUser, RegisterUserResponse
from fixtures.users.model import AddUserInfo
import pytest


class TestAdduserInfo:
    def test_add_user_info(self, app, auth_data):
        """
        1. Try to register user with valid data
        2. Try to auth user with data from step 1
        3. Check that status code is 200
        4. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(user_id=auth_data.uuid, data=data, token=auth_data.token)
        assert res.status_code == 200

    @pytest.mark.xfail(reason='bug')
    def test_add_user_info_long_phone(self, app, auth_data):
        """
        1. Register and auth new user
        2. Try to add user info with long phone
        3. Check that status code is 400
        4. Check response
        """
        data = AddUserInfo.random()
        data.phone = "1"*3000
        res = app.user_info.add_user_info(user_id=auth_data.uuid, data=data, token=auth_data.token)
        assert res.status_code == 400

    def test_add_user_info_none_exist_user(self, app, auth_data, uuid=10000000):
        """
        1. Register and auth new user
        2. Try to add user info with none exist user
        3. Check that status code is 404
        4. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(user_id=uuid, data=data,
                                          token=auth_data.token)
        assert res.status_code == 404

    @pytest.mark.parametrize('uuid', [True, None])
    def test_add_user_info_none_exist_user(self, app, auth_data, uuid):
        """
        1. Register and auth new user
        2. Try to add user info with none exist user
        3. Check that status code is 404
        4. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(user_id=uuid, data=data,
                                          token=auth_data.token)
        assert res.status_code == 404

    def test_add_user_info_none_exist_token(self, app, auth_data, token='1234'):
        """
        1. Register and auth new user
        2. Try to add user info with none exist token
        3. Check that status code is 401
        4. Check response
        """
        data = AddUserInfo.random()
        res = app.user_info.add_user_info(user_id=auth_data.uuid, data=data,
                                          token=token)
        assert res.status_code == 401