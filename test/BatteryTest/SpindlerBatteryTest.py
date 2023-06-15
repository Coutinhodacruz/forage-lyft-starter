from datetime import datetime
from unittest import TestCase

from Service.Model.Batteries.Battery import Battery
from Service.Model.Batteries.SpindlerBattery import SpindlerBattery


class TestSpindlerBattery(TestCase):

    def setUp(self) -> None:
        self.current_date = datetime.today().date()

    def test_spindler_battery_needs_service_when_in_use_for_3_years_or_more(self):
        last_service_date = self.current_date.replace(year=self.current_date.year - 3)
        spindler_battery: Battery = SpindlerBattery(self.current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())

        last_service_date = self.current_date.replace(year=self.current_date.year - 4)
        spindler_battery: Battery = SpindlerBattery(self.current_date, last_service_date)
        self.assertTrue(spindler_battery.needs_service())

    def test_spindler_battery_needs_service_is_false_when_in_use_for_2_years_or_less(self):
        last_service_date = self.current_date.replace(year=self.current_date.year - 2)
        spindler_battery: Battery = SpindlerBattery(self.current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())

        last_service_date = self.current_date.replace(year=self.current_date.year - 0)
        spindler_battery: Battery = SpindlerBattery(self.current_date, last_service_date)
        self.assertFalse(spindler_battery.needs_service())
