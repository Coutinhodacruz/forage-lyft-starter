from datetime import date

from Service.Model.Cars.calliope_car import CalliopeCar
from Service.Model.Cars.car import Car
from Service.Model.Cars.glissade_car import GlissadeCar
from Service.Model.Cars.palindrome_car import PalindromeCar
from Service.Model.Cars.rorschach_car import RorschachCar
from Service.Model.Cars.thovex_car import ThovexCar


class CarFactory:

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        return CalliopeCar(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int) -> Car:
        return GlissadeCar(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date,
                          warning_light_on: bool) -> Car:
        return PalindromeCar(current_date, last_service_date, warning_light_on)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int) -> Car:
        return RorschachCar(current_date, last_service_date, current_mileage, last_service_mileage)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int) -> Car:
        return ThovexCar(current_date, last_service_date, current_mileage, last_service_mileage)
