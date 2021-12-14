from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()



@attr.s
class UserModel:
    token: str = attr.ib(default=None)
    uuid: int = attr.ib(default=None)
