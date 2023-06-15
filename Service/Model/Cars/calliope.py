from datetime import date

from Service.Model.Batteries.Battery import Battery
from Service import SpindlerBattery
from Service import CapuletEngine
from Service import Engine
from Service.Model.Cars import Car


class CalliopeCar(Car):

    def __init__(self,  current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self._capuletEngine: Engine = CapuletEngine(current_mileage, last_service_mileage)
        self._spindlerBattery: Battery = SpindlerBattery(current_date, last_service_date)

        super().__init__(self._capuletEngine, self._spindlerBattery)

    def engine_needs_service(self) -> bool:
        return self._capuletEngine.needs_service()

    def battery_needs_service(self) -> bool:
        return self._spindlerBattery.needs_service()

    def needs_service(self) -> bool:
        return self.engine_needs_service() or self.battery_needs_service()
