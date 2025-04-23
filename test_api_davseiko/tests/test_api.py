import pytest


TEST_DATA = [{"name": "Test object2", "data": {"color": "test_color2", "size": "test_size2"}},
             {"name": "Test object3", "data": {"color": "test_color3", "size": "test_size3"}}]


@pytest.mark.parametrize('data', TEST_DATA)
def test_create_an_object(create_object_endpoint, delete_object_endpoint, data):
    create_object_endpoint.create_new_object(body=data)
    create_object_endpoint.check_response_status_code_is_200()
    create_object_endpoint.check_response_name_is_correct(data['name'])
    delete_object_endpoint.delete_object(create_object_endpoint.object_id)


def test_put_an_object(update_object_endpoint, object_id):
    body = {
        "name": "Test object_upd_put",
        "data": {
            "color": "test_color_upd_put",
            "size": "test_size_upd_put"
        }
    }
    update_object_endpoint.make_changes_in_object(object_id, body)
    update_object_endpoint.check_response_status_code_is_200()
    update_object_endpoint.check_response_name_is_correct(body['name'])


def test_patch_an_object(modify_object_endpoint, object_id):
    body = {
        "name": "Test object_upd_patch"
    }
    modify_object_endpoint.change_name_in_object(object_id, body)
    modify_object_endpoint.check_response_status_code_is_200()
    modify_object_endpoint.check_response_name_is_correct(body['name'])


def test_delete_an_object(delete_object_endpoint, object_id):
    delete_object_endpoint.delete_object(object_id)
    delete_object_endpoint.check_response_status_code_is_200()


def test_get_all_objects(get_all_objects_endpoint):
    get_all_objects_endpoint.get_all_objects()
    get_all_objects_endpoint.check_response_status_code_is_200


def test_get_object_info(get_object_info_endpoint, object_id):
    get_object_info_endpoint.get_object_info(object_id)
    get_object_info_endpoint.check_response_status_code_is_200
    get_object_info_endpoint.check_response_id_is_correct(object_id)
