from datetime import date

from Service import Battery
from Service import SpindlerBattery
from Service.Model.Cars.car import Car
from Service.Model.Engines.Engine import Engine
from Service.Model.Engines.SternmanEngine import SternmanEngine


class PalindromeCar(Car):
    def __init__(self, current_date: date, last_service_date: date, warning_light_on: bool):
        self._sternman_engine: Engine = SternmanEngine(warning_light_on)
        self._spindler_battery: Battery = SpindlerBattery(current_date, last_service_date)

        super().__init__(self._sternman_engine, self._spindler_battery)

    def engine_needs_service(self) -> bool:
        return self._sternman_engine.needs_service()

    def battery_needs_service(self) -> bool:
        return self._spindler_battery.needs_service()

    def needs_service(self) -> bool:
        return self.engine_needs_service() or self.battery_needs_service()
