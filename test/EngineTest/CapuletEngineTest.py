from unittest import TestCase

from Service.Model.Engines.CapuletEngine import CapuletEngine
from Service.Model.Engines.Engine import Engine


class TestCapuletEngine(TestCase):

    def setUp(self) -> None:
        self.last_service_mileage: int = 0

    def test_capulet_engine_needs_service_when_mileage_is_30000_or_above(self):
        current_mileage: int = 30000
        capulet_engine: Engine = CapuletEngine(current_mileage, self.last_service_mileage)

        self.assertTrue(capulet_engine.needs_service())

    def test_capulet_engine_needs_service_is_false_when_mileage_is_below_30000(self):
        current_mileage: int = 28900
        capulet_engine: Engine = CapuletEngine(current_mileage, self.last_service_mileage)

        self.assertFalse(capulet_engine.needs_service())
