import requests
import pytest


@pytest.fixture()
def get_object_id():
    body = {
        "name": "Test object",
        "data": {
            "color": "test_color",
            "size": "test_size"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


@pytest.fixture()
def conditions():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='session')
def run():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.mark.critical
def test_get_all_objects(conditions, run):
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


@pytest.mark.medium
def test_get_object(get_object_id, conditions):
    response = requests.get(f'http://167.172.172.115:52353/object/{get_object_id}').json()
    assert response['id'] == get_object_id


@pytest.mark.parametrize('body', [{"name": "Test object1", "data": {"color": "red", "size": "1"}},
                                  {"name": "Test object2", "data": {"color": "blue", "size": "2"}},
                                  {"name": "Test object3", "data": {"color": "white", "size": "3"}}])
def test_create_an_object(conditions, body):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'


def test_put_an_object(get_object_id, conditions):
    body = {
        "name": "Test object_upd_put",
        "data": {
            "color": "test_color_upd_put",
            "size": "test_size_upd_put"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{get_object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test object_upd_put'


def test_patch_an_object(get_object_id, conditions):
    body = {
        "name": "Test object_upd_patch"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{get_object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test object_upd_patch'


def test_delete_an_object(get_object_id, conditions):
    response = requests.delete(f'http://167.172.172.115:52353/object/{get_object_id}')
    assert response.status_code == 200, 'Status code is incorrect'
