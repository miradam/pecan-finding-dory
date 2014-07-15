import abc
import six


@six.add_metaclass(abc.ABCMeta)
class ManagerDriverBase(object):
    """Add some docstrings"""

    def __init__(self, conf, storage):
        self._conf = conf
        self._storage = storage

    @abc.abstractproperty
    def todos_controller(self):
        """Returns the driver's Todos controller."""
        raise NotImplementedError


@six.add_metaclass(abc.ABCMeta)
class ControllerBase(object):

    """Top-level class for controllers.

    :param driver: Instance of the driver
        instantiating this controller.
    """

    def __init__(self, driver):
        self.driver = driver


@six.add_metaclass(abc.ABCMeta)
class TodosControllerBase(ControllerBase):

    def __init__(self, driver):
        super(TodosControllerBase, self).__init__(driver)

    @abc.abstractmethod
    def list(self, project_id):
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, project_id, service_name, service_json):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, project_id, service_name):
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, project_id, service_name):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, todo_id):
        raise NotImplementedError
