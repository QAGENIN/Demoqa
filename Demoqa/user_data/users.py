from faker import Faker
import dataclasses
import datetime

fake = Faker()


class CreateTestUser:
    name = fake.name()
    email = fake.email()
    current_address = fake.street_address()
    permanent_address = fake.street_address()


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: datetime.date
    subjects: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str


test_user = User(
    first_name='Testfirstname',
    last_name='Testlastname',
    email='tests@demoqa.com',
    gender='Male',
    mobile='9115678907',
    date_of_birth=datetime.date(1989, 1, 11),
    hobbies='Sports',
    subjects='Maths',
    picture='images.png',
    address='Russia, Moscow, str.Testers',
    state='NCR',
    city='Delhi',
)
