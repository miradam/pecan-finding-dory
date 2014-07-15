"""Default manager driver implementation."""

from dory.common import decorators
from dory import manager
from dory.manager.default import controllers


class ManagerDriver(manager.ManagerDriverBase):

    def __init__(self, conf, storage):
        super(ManagerDriver, self).__init__(conf, storage)

    @decorators.lazy_property(write=False)
    def todos_controller(self):
        return controllers.Todos(self)
