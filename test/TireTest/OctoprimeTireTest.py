from unittest import TestCase

from Service.Model.Tires.OctoprimeTire import OctoprimeTire
from Service.Model.Tires.Tire import Tire


class OctoprimeTireTest(TestCase):

    def test_that_octoprime_tire_is_not_null(self):
        octoprime_tire: Tire = OctoprimeTire([0, 0, 0, 0])
        self.assertIsNotNone(octoprime_tire)

    def test_that_octoprime_tire_needs_service(self):
        octoprime_tire: Tire = OctoprimeTire([1, 0.5, 0.8, 0.97])
        self.assertTrue(octoprime_tire.needs_service())

    def test_that_octoprime_tire_does_not_needs_service(self):
        octoprime_tire: Tire = OctoprimeTire([0.89, 0, 0.5, 0.5])
        self.assertFalse(octoprime_tire.needs_service())
