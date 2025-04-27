from locust import task, HttpUser
import random


class Object(HttpUser):

    @task(1)
    def get_all_objects(self):
        self.client.get(
            '/object',
        )

    @task(3)
    def get_one_object(self):
        self.client.get(
            f'/object/{random.choice([21, 29, 276, 239])}'
        )

    @task(1)
    def create_an_object(self):
        self.client.post(
            '/object',
            json={"name": "Test object2", "data": {"color": "blue", "size": "2"}},
            headers={'Content-Type': 'application/json'}
        )

    @task(1)
    def put_an_object(self):
        self.client.put(
            f'/object/{random.choice([21, 29, 276, 239])}',
            json={"name": "Test object_upd_put",
            "data": {
            "color": "test_color_upd_put",
            "size": "test_size_upd_put"}},
            headers={'Content-Type': 'application/json'}
        )

    @task(1)
    def patch_an_object(self):
        self.client.patch(
            f'/object/{random.choice([21, 29, 276, 239])}',
            json={"name": "Test object_upd_patch"},
            headers={'Content-Type': 'application/json'}
        )

    @task(1)
    def delete_an_object(self):
        self.client.delete(
            f'/object/{random.choice([21, 29, 276, 239])}',
        )
