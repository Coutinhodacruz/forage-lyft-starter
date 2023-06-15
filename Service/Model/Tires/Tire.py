import abc
from abc import ABC


class Tire(ABC):

    @abc.abstractmethod
    def needs_service(self):
        pass
