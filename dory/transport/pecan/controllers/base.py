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

from pecan import rest


class Controller(rest.RestController):

    @property
    def manager_driver(self):
        return self._manager_driver

    @manager_driver.setter
    def manager_driver(self, value):
        self._manager_driver = value

    def add_controller(self, path, controller):
        setattr(self, path, controller)
        getattr(self, path).manager_driver = self.manager_driver
