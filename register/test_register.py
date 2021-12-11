import requests

from fixtures.constants import ResponseText
from fixtures.register.models import RegisterUser


class TestRegister:
    def test_register_valid_data(self):
        body = {"username": 'test111', "password": "Password11"}
        res = requests.post('https://stores-tests-api.herokuapp.com/register', json=body)
        assert res.json().get('message') == 'User created successfully.'
        assert res.json().get('uuid')
        assert res.status_code == 201

    def test_register_invalid_data(self):
        body = {"username": 'test111111'}
        res = requests.post('https://stores-tests-api.herokuapp.com/register',
                            json=body)
        assert res.json().get('message').get('password') == 'This field cannot be blank.'
        assert res.status_code == 400

    def test_register_valid_data_2(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data)
        assert res.status_code == 201, "Check response"
        # assert res.data.message == ResponseText.MESSAGE_REGISTER_USER
        isinstance(data, RegisterUser)
        assert res.json().get('message') == ResponseText.MESSAGE_REGISTER_USER

