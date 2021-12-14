import logging

import pytest

from fixtures.app import App
from fixtures.auth.model import AuthResponse, AuthUser
from fixtures.base_model import UserModel
from fixtures.register.models import RegisterUser, RegisterUserResponse

logger = logging.getLogger("api")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    ),


@pytest.fixture(scope='session')
def app(request):
    url = request.config.getoption("--api-url")
    logger.info(f"Start api tests, url is {url}")
    return App(url)


@pytest.fixture
def register_data(app):
    data = RegisterUser.random()
    res = app.register.register(data=data, type_response=RegisterUserResponse)
    data.uuid = res.custom_response.uuid
    return data

@pytest.fixture
def auth_data(app, register_data):
    data = AuthUser(username=register_data.username, password=register_data.password)
    res = app.auth.login(data=data)
    return UserModel(uuid=register_data.uuid, token=res.custom_response.access_token)
