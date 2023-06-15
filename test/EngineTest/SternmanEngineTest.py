from unittest import TestCase

from Service.Model.Engines.Engine import Engine
from Service.Model.Engines.SternmanEngine import SternmanEngine


class TestSternmanEngine(TestCase):

    def test_sternman_engine_needs_service_when_warning_indicator_is_on(self):
        warning_indicator_is_on = True
        sternman_engine: Engine = SternmanEngine(warning_indicator_is_on)

        self.assertTrue(sternman_engine.needs_service())

    def test_sternman_engine_needs_service_is_false_when_warning_indicator_is_not_on(self):
        warning_indicator_is_on = False
        sternman_engine: Engine = SternmanEngine(warning_indicator_is_on)

        self.assertFalse(sternman_engine.needs_service())
