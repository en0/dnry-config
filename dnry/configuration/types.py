from abc import ABC, abstractmethod
from typing import Union


class IConfigurationSection(ABC):
    @abstractmethod
    def get(self, key: str) -> any:
        raise NotImplemented()

    @abstractmethod
    def get_section(self, key: str) -> Union["IConfigurationSection", None]:
        raise NotImplemented()

    @abstractmethod
    def has(self, key: str) -> bool:
        raise NotImplemented()


class IConfigurationSource(ABC):
    @abstractmethod
    def load(self, fact: "IConfigurationFactory", conf: IConfigurationSection) -> dict:
        raise NotImplemented()


class IConfigurationFactory(ABC):
    @abstractmethod
    def add_source(self, source: IConfigurationSource) -> None:
        raise NotImplemented()

    @abstractmethod
    def build(self) -> IConfigurationSection:
        raise NotImplemented()

    @abstractmethod
    def add_configuration(self, conf: IConfigurationSection):
        raise NotImplemented()
