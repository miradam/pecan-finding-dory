import uuid

from dory.manager import base
from dory.openstack.common import local


class TodosController(base.TodosControllerBase):

    def list(self):
        return [local.store.context.tenant, 1, 2, 3]

    def create(self, title, text):
        return uuid.uuid4()

    def update(self, todo_id, title, text):
        return todo_id

    def delete(self, todo_id):
        return todo_id

    def get(self, todo_id):
        return todo_id
