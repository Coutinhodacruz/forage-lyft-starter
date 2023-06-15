from unittest import TestCase

from Service.Model.Tires.CarriganTire import CarriganTire
from Service.Model.Tires.Tire import Tire


class CarriganTireTest(TestCase):

    def test_that_carrigan_tire_is_not_null(self):
        carrigan_tire: Tire = CarriganTire([0, 0, 0, 0])
        self.assertIsNotNone(carrigan_tire)

    def test_that_carrigan_tire_needs_service(self):
        carrigan_tire: Tire = CarriganTire([0, 0, 0.5, 0.97])
        self.assertTrue(carrigan_tire.needs_service())

    def test_that_carrigan_tire_does_not_needs_service(self):
        carrigan_tire: Tire = CarriganTire([0.89, 0, 0.5, 0.5])
        self.assertFalse(carrigan_tire.needs_service())
