from dnry.configuration.types import IConfigurationSource, IConfigurationFactory, IConfigurationSection


class InMemorySource(IConfigurationSource):
    """Read configuration values from a dictionary"""
    def __init__(self, data: dict):
        self.__data = data

    def load(self, fact: IConfigurationFactory, conf: IConfigurationSection) -> dict:
        return self.__data
