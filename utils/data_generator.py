from dataclasses import asdict

from faker import Faker

from models.category import Category
from models.pet import Pet
from models.tag import Tag

fake = Faker()


def generate_pet():
    category = Category(
        id=fake.random_digit(),
        name=fake.language_name()
    )
    tag = Tag(
        id=fake.random_digit(),
        name=fake.color_name()
    )
    pet = Pet(
        id=fake.random_number(digits=5),
        category=category,
        name=fake.first_name_nonbinary(),
        photoUrls=[fake.url()],
        tags=[tag],
        status="available"
    )
    result = asdict(pet)
    return result
