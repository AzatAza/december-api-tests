from fixtures.auth.api import Auth
from fixtures.register.api import Register
from fixtures.requests import Client
from fixtures.users.api import User


class App:
    def __init__(self, url):
        self.url = url
        self.register = Register(self)
        self.auth = Auth(self)
        self.user_info = User(self)
        self.client = Client
