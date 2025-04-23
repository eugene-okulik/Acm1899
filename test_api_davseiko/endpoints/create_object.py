import requests
import allure
from test_api_davseiko.endpoints.endpoint import Endpoint


class CreateObject(Endpoint):
    object_id = None

    @allure.step('Create new object')
    def create_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']
        return self.response
