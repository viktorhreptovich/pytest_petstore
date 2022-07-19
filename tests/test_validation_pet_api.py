import allure

from utils.data_generator import generate_pet


@allure.suite('API petstore specification validations')
class TestSpecificationPetApi:

    @allure.title('Validation api creating pet')
    def test_add_pet(self, pet_api):
        pet = generate_pet()

        result = pet_api.add_pet(pet)
        result.validate_specification_api()

    @allure.title('Validation api updating pet')
    def test_update_pet(self, pet_api):
        pet = generate_pet()
        pet_api.add_pet(pet)
        pet['name'] = 'Vasiliy'

        result = pet_api.update_pet(pet)
        result.validate_specification_api()

    @allure.title('Validation api getting pet')
    def test_get_pet(self, pet_api):
        pet = generate_pet()
        pet_api.add_pet(pet)

        result = pet_api.get_pet(pet['id'])
        result.validate_specification_api()

    @allure.title('Validation api deleting pet')
    def test_delete_pet(self, pet_api):
        pet = generate_pet()
        pet_api.add_pet(pet)

        result = pet_api.delete_pet(pet['id'])
        result.validate_specification_api()
