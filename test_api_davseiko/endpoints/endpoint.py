import allure
import requests


class Endpoint:
    url = 'http://167.172.172.115:52353/object'
    response = None
    response_json = None
    headers = {'Content-Type': 'application/json'}

    @allure.step('Check that status code is 200')
    def check_response_status_code_is_200(self):
        assert self.response.status_code == 200, 'Status code is not 200'

    @allure.step('Check that name is the same as sent')
    def check_response_name_is_correct(self, name):
        assert self.response_json['name'] == name

    @allure.step('Check that id is the same as sent')
    def check_response_id_is_correct(self, object_id):
        assert self.response_json['id'] == object_id

    @allure.step('Clear object')
    def clear_object(self, object_id):
        requests.delete(f'{self.url}/{object_id}')
