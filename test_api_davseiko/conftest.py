import pytest
from test_api_davseiko.endpoints.create_object import CreateObject
from test_api_davseiko.endpoints.update_object import UpdateObject
from test_api_davseiko.endpoints.modify_object import ModifyObject
from test_api_davseiko.endpoints.delete_object import DeleteObject
from test_api_davseiko.endpoints.get_all_objects import GetAllObjects
from test_api_davseiko.endpoints.get_object_info import GetObjectInfo


@pytest.fixture()
def create_object_endpoint():
    return CreateObject()


@pytest.fixture()
def update_object_endpoint():
    return UpdateObject()


@pytest.fixture()
def modify_object_endpoint():
    return ModifyObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()


@pytest.fixture()
def get_all_objects_endpoint():
    return GetAllObjects()


@pytest.fixture()
def get_object_info_endpoint():
    return GetObjectInfo()


@pytest.fixture()
def object_id(create_object_endpoint, delete_object_endpoint):
    body = {"name": "Test object1", "data": {"color": "test_color1", "size": "test_size1"}}
    create_object_endpoint.create_new_object(body)
    yield create_object_endpoint.object_id
    delete_object_endpoint.delete_object(create_object_endpoint.object_id)
