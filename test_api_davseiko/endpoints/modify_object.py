import requests
import allure
from test_api_davseiko.endpoints.endpoint import Endpoint


class ModifyObject(Endpoint):

    @allure.step('Modify an object')
    def change_name_in_object(self, object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{object_id}',
            json=body,
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
