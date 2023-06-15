from unittest import TestCase

from Service.Model.Engines.Engine import Engine
from Service.Model.Engines.WilloughbyEngine import WilloughbyEngine


class TestWilloughbyEngine(TestCase):
    def setUp(self) -> None:
        self.last_service_mileage: int = 0

    def test_willoughby_engine_needs_service_when_mileage_is_60000_or_above(self):
        current_mileage: int = 60000
        willoughby_engine: Engine = WilloughbyEngine(current_mileage, self.last_service_mileage)

        self.assertTrue(willoughby_engine.needs_service())

    def test_willoughby_engine_needs_service_is_false_when_mileage_is_below_60000(self):
        current_mileage: int = 59999
        Willoughby_engine: Engine = WilloughbyEngine(current_mileage, self.last_service_mileage)

        self.assertFalse(Willoughby_engine.needs_service())
