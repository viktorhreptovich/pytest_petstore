import allure

from utils.http_manager import HttpManager


class PetApi:

    def __init__(self):
        self.http = HttpManager()
        self.url = f'{self.http.base_url}/v2/pet'
        self.url_with_path = lambda pet: f'{self.http.base_url}/v2/pet/{pet}'

    @allure.step('Send request create pet')
    def add_pet(self, body: dict):
        return self.http.post(self.url, body);

    @allure.step('Send request update pet')
    def update_pet(self, body: dict):
        return self.http.put(self.url, body)

    @allure.step('Send request delete pet')
    def delete_pet(self, pet_id: int):
        return self.http.delete(self.url_with_path(pet_id))

    @allure.step('Send request get pet by id')
    def get_pet(self, pet_id: int):
        return self.http.get(self.url_with_path(pet_id))
