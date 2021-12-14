import requests

from fixtures.constants import ResponseText
from fixtures.register.models import RegisterUser, RegisterUserResponse, \
    RegisterUserInvalidResponse


class TestRegister:
    # def test_register_valid_data(self):
    #     body = {"username": 'test111', "password": "Password11"}
    #     res = requests.post('https://stores-tests-api.herokuapp.com/register', json=body)
    #     assert res.json().get('message') == 'User created successfully.'
    #     assert res.json().get('uuid')
    #     assert res.status_code == 201

    # def test_register_invalid_data(self):
    #     body = {"username": 'test111111'}
    #     res = requests.post('https://stores-tests-api.herokuapp.com/register',
    #                         json=body)
    #     assert res.json().get('message').get('password') == 'This field cannot be blank.'
    #     assert res.status_code == 400

    def test_register_valid_data(self, app):
        """
        1. Try to register user with valid data
        2. Check that status code is 201
        3. Check response
        """
        data = RegisterUser.random()
        res = app.register.register(data=data, type_response=RegisterUserResponse)
        assert res.status_code == 201, "Check response"
        assert res.custom_response.message == ResponseText.MESSAGE_REGISTER_USER

    def test_register_invalid_data(self, app):
        """
        1. Try to register user with invalid data
        2. Check that status code is 400
        3. Check response
        """
        data = RegisterUser.random()
        data.password=None
        res = app.register.register(data=data, type_response=RegisterUserInvalidResponse)
        assert res.status_code == 400, "Check response"
        assert res.custom_response.message == ResponseText.PASSWORD_REQUIRED_FIELD

        #
        # 1. Степы
        # 2. Реквест, Респонс, Боди, Статус код, Метод

