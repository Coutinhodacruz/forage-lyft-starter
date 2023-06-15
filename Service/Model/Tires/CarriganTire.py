from Service.Model.Tires.Tire import Tire


class CarriganTire(Tire):

    def __init__(self, wear_sensors: list[float]):
        self._wear_sensors: list[float] = wear_sensors

    def needs_service(self):
        wear_value = 0.9

        return any(tire_wear_value >= wear_value for tire_wear_value in self._wear_sensors)
