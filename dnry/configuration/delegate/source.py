from typing import Callable, Union

from dnry.configuration.types import IConfigurationSource, IConfigurationFactory, IConfigurationSection


class DelegateSource(IConfigurationSource):
    def __init__(self, delegate: Callable[[IConfigurationFactory], Union[dict, None]]):
        self.__delegate = delegate

    def load(self, fact: IConfigurationFactory, conf: IConfigurationSection) -> dict:
        return self.__delegate(fact, conf) or {}
