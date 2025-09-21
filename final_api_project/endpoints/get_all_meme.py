import requests
import allure
from final_api_project.endpoints.endpoint import Endpoint


class GetAllMeme(Endpoint):
    token = None


    def get_all_meme(self, token):
        #headers = headers if headers else self.headers
        self.headers['Authorization'] = token
        self.response = requests.get(
            self.url,
            headers=self.headers
        )
        return self.response

