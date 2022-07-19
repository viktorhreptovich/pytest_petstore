import pytest

from services.pet_api import PetApi


@pytest.fixture
def pet_api():
    return PetApi()
