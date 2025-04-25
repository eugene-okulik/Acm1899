import requests
import allure
from test_api_davseiko.endpoints.endpoint import Endpoint


class GetAllObjects(Endpoint):

    @allure.step('Get all objects')
    def get_all_objects(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers
        )
        return self.response
