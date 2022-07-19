import allure

from schema.jsonschema import Schema
from utils.data_generator import generate_pet


@allure.suite('API petstore tests')
class TestPetApi:

    @allure.title('Create pet')
    def test_add_pet(self, pet_api):
        pet = generate_pet()

        result = pet_api.add_pet(pet)
        result.assert_status_code_is(200)
        result.validate_json_schema(Schema.PET)
        result.assert_body_equal(pet)

    @allure.title('Update pet')
    def test_update_pet(self, pet_api):
        pet = generate_pet()
        pet_api.add_pet(pet)
        pet['name'] = 'Vasiliy'

        result = pet_api.update_pet(pet)
        result.assert_status_code_is(200)
        result.validate_json_schema(Schema.PET)
        result.assert_body_equal(pet)

    @allure.title('Get pet by id')
    def test_get_pet(self, pet_api):
        pet = generate_pet()
        pet_api.add_pet(pet)

        result = pet_api.get_pet(pet['id'])
        result.assert_status_code_is(200)
        result.validate_json_schema(Schema.PET)
        result.assert_body_equal(pet)

    @allure.title('Delete pet')
    def test_delete_pet(self, pet_api):
        pet = generate_pet()
        pet_api.add_pet(pet)

        result = pet_api.delete_pet(pet['id'])
        result.assert_status_code_is(200)
        result.validate_json_schema(Schema.API_RESPONSE)
        result.assert_field_equal('message', pet['id'])

        result = pet_api.get_pet(pet['id'])
        result.assert_status_code_is(404)
