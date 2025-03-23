import requests


def get_all_objects():
    response = requests.get('http://167.172.172.115:52353/object')
    assert response.status_code == 200, 'Status code is incorrect'


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
    return response.json()['id']


def clear(object_id):
    requests.delete(f'http://167.172.172.115:52353/object/{object_id}')


def get_object():
    object_id = get_object_id()
    response = requests.get(f'http://167.172.172.115:52353/object/{object_id}').json()
    assert response['id'] == object_id


def create_an_object():
    body = {
        "name": "Test object2",
        "data": {
            "color": "test_color2",
            "size": "test_size2"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'http://167.172.172.115:52353/object',
        json=body,
        headers=headers
    )
    assert response.status_code == 200, 'Status code is incorrect'


def put_an_object():
    object_id = get_object_id()
    body = {
        "name": "Test object_upd_put",
        "data": {
            "color": "test_color_upd_put",
            "size": "test_size_upd_put"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.put(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test object_upd_put'
    clear(object_id)


def patch_an_object():
    object_id = get_object_id()
    body = {
        "name": "Test object_upd_patch"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(
        f'http://167.172.172.115:52353/object/{object_id}',
        json=body,
        headers=headers
    ).json()
    assert response['name'] == 'Test object_upd_patch'
    clear(object_id)


def delete_an_object():
    object_id = get_object_id()
    response = requests.delete(f'http://167.172.172.115:52353/object/{object_id}')
    assert response.status_code == 200, 'Status code is incorrect'


get_all_objects()
get_object()
create_an_object()
put_an_object()
patch_an_object()
delete_an_object()
