from faker import Faker

from fixtures.base import BaseClass

fake = Faker()


class RegisterUser(BaseClass):
    def __init__(self, username, password):
        self.password = password
        self.username = username

    @staticmethod
    def random():
        return RegisterUser(username=fake.email(), password=fake.password())
