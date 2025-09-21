import requests
import allure
from final_api_project.endpoints.endpoint import Endpoint


class DeleteMeme(Endpoint):
    id = None
    token = None

    #@allure.step('Delete an object')
    def delete_meme(self, id, token):
        #headers = headers if headers else self.headers
        self.headers['Authorization'] = token
        self.response = requests.delete(
            f'{self.url}/{id}',
            headers=self.headers
        )
        return self.response

