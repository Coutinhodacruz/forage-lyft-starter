import abc
from abc import ABC


class Serviceable(ABC):

    @abc.abstractmethod
    def needs_service(self) -> bool:
        pass
