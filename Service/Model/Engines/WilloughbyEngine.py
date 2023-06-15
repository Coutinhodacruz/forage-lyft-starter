from Service.Model.Engines.Engine import Engine


class WilloughbyEngine(Engine):

    def __init__(self, current_mileage: int, last_service_mileage: int):
        self._last_service_mileage: int = last_service_mileage
        self._current_mileage: int = current_mileage

    def needs_service(self) -> bool:
        return (self._current_mileage - self._last_service_mileage) >= 60000
