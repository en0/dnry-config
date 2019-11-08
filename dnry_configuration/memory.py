from dnry_configuration.types import IConfigurationSource


class InMemorySource(IConfigurationSource):
    def __init__(self, data: dict):
        self.__data = data

    def load(self) -> dict:
        return self.__data
