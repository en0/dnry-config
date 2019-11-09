from dnry_configuration.types import IConfigurationSource, IConfigurationFactory


class InMemorySource(IConfigurationSource):
    """Read configuration values from a dictionary"""
    def __init__(self, data: dict):
        self.__data = data

    def load(self, fact: IConfigurationFactory) -> dict:
        return self.__data
