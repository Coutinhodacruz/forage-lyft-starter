from Service.Model.Tires.Tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, wear_sensors: list[float]):
        self._wear_sensor: list[float] = wear_sensors

    def needs_service(self):
        sum_of_wear_values = sum(self._wear_sensor)
        wear_value = 3

        return sum_of_wear_values >= wear_value
