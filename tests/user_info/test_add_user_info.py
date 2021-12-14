from fixtures.constants import ResponseText
from fixtures.register.models import RegisterUser, RegisterUserResponse
from fixtures.users.model import AddUserInfo


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
