import requests
import allure
from test_api_davseiko.endpoints.endpoint import Endpoint


class GetObjectInfo(Endpoint):

    @allure.step('Get object info')
    def get_object_info(self, object_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            f'{self.url}/{object_id}',
            headers=headers
        )
        self.response_json = self.response.json()
        return self.response
