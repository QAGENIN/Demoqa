from faker import Faker


class CreateTestUser:
    fake = Faker()
    name = fake.name()
    email = fake.email()
    current_address = fake.street_address()
    permanent_address = fake.street_address()
