from Service.Model.Engines.Engine import Engine


class SternmanEngine(Engine):

    def __init__(self, warning_light_on: bool):
        self._warning_light_on: bool = warning_light_on

    def needs_service(self) -> bool:
        return self._warning_light_on
