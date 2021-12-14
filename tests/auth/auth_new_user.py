from fixtures.constants import ResponseText
from fixtures.register.models import RegisterUser, RegisterUserResponse


class TestAuth:
    def test_auth_valid_data(self, app, register_data):
        """
        1. Try to register user with valid data
        2. Try to auth user with data from step 1
        3. Check that status code is 200
        4. Check response
        """
        res_login = app.auth.login(register_data)
        assert res_login.status_code == 200, "Check response"
