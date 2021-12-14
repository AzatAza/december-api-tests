from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()


@attr.s
class AuthUser(BaseClass):
    username: str = attr.ib(default=None)
    password: str = attr.ib(default=None)

    @staticmethod
    def random():
        return AuthUser(username=fake.email(), password=fake.password())


@attr.s
class AuthResponse:
    access_token: str = attr.ib(validator=attr.validators.instance_of(str))