from faker import Faker
import attr

from fixtures.base import BaseClass

fake = Faker()



@attr.s
class Address:
    city: str = attr.ib(default=None)
    street: str = attr.ib(default=None)
    home_number: str = attr.ib(default=None)


@attr.s
class AddUserInfo(BaseClass):
    phone: str = attr.ib(default=None)
    email: str = attr.ib(default=None)
    address: Address = attr.ib(default=None)

    @staticmethod
    def random():
        address = Address(city=fake.city(), street=fake.street_name(), home_number=fake.building_number())
        return AddUserInfo(phone=fake.phone_number(), email=fake.email(), address=address)

    # {
    #     "phone": "string",
    #     "email": "string",
    #     "address": {
    #         "city": "string",
    #         "street": "string",
    #         "home_number": "string"
    #     }
    # }