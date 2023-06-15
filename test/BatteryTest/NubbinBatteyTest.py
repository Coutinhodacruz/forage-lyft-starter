from datetime import datetime, date
from unittest import TestCase

from Service.Model.Batteries.Battery import Battery
from Service.Model.Batteries.NubbinBattery import NubbinBattery


class TestNubbinBattery(TestCase):

    def setUp(self) -> None:
        self.current_date: date = datetime.today().date()

    def test_nubbin_battery_needs_service_when_in_use_for_2_years_or_more(self):
        last_service_date: date = self.current_date.replace(year=self.current_date.year - 4)
        nubbin_battery: Battery = NubbinBattery(self.current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service())

        last_service_date: date = self.current_date.replace(year=self.current_date.year - 5)
        nubbin_battery: Battery = NubbinBattery(self.current_date, last_service_date)
        self.assertTrue(nubbin_battery.needs_service())

    def test_nubbin_battery_needs_service_is_false_when_in_use_for_2_years_or_more(self):
        last_service_date: date = self.current_date.replace(year=self.current_date.year - 3)
        nubbin_battery: Battery = NubbinBattery(self.current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())

        last_service_date: date = self.current_date.replace(year=self.current_date.year - 2)
        nubbin_battery: Battery = NubbinBattery(self.current_date, last_service_date)
        self.assertFalse(nubbin_battery.needs_service())
