import abc
from abc import ABC


class Engine(ABC):

    @abc.abstractmethod
    def needs_service(self) -> bool:
        pass
