from datetime import date

from Service.Model.Batteries.Battery import Battery
from Service import SpindlerBattery
from Service.Model.Cars import Car
from Service import Engine
from Service import WilloughbyEngine


class GlissadeCar(Car):
    def __init__(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        self._willoughby_engine: Engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self._spindler_battery: Battery = SpindlerBattery(current_date, last_service_date)

        super().__init__(self._willoughby_engine, self._spindler_battery)

    def engine_needs_service(self) -> bool:
        return self._willoughby_engine.needs_service()

    def battery_needs_service(self) -> bool:
        return self._spindler_battery.needs_service()

    def needs_service(self) -> bool:
        return self.engine_needs_service() or self.battery_needs_service()
