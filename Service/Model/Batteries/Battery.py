import abc
from abc import ABC


class Battery(ABC):

    @abc.abstractmethod
    def needs_service(self) -> bool:
        pass
