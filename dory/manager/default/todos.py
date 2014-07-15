# Copyright (c) 2014 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid

from dory.manager import base
from dory.openstack.common import local


class DefaultTodosController(base.TodosController):

    def list(self):
        return [local.store.context.tenant, 1, 2, 3]

    def get(self, todo_id):
        return todo_id

    def create(self, title, text):
        return uuid.uuid4()

    def update(self, todo_id, title, text):
        return todo_id

    def delete(self, todo_id):
        return todo_id
