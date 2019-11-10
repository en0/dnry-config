from typing import List, Any

from dnry.configuration.section import ConfigurationSection
from dnry.configuration.helpers import merge
from dnry.configuration.types import IConfigurationFactory, IConfigurationSource, IConfigurationSection


class ConfigurationFactory(IConfigurationFactory):
    """Builds a single configuration section from a set of configuration sources.

    Configuration sources will be loaded and merged in order. If configuration sources
    collide key names, the value for the last source loaded containing the key will
    be used.

    You can override the merge behavior by providing your own implementation and setting it
    on ConfigurationFactory.merge.

    You can provide your own IConfigurationSection implementation by setting it on
    ConfigurationFactory.Section. Note: you must accept a single dict in __init__.
    """

    __explicit_configs: List[IConfigurationSection]
    __sources: List[IConfigurationSource]
    Section = ConfigurationSection
    merge = merge

    def __init__(self, sources: List[IConfigurationSource] = None):
        self.__explicit_configs = list()
        self.__sources = sources or list()

    def add_source(self, source: IConfigurationSource) -> None:
        self.__sources.append(source)

    def add_configuration(self, conf: IConfigurationSection):
        self.__explicit_configs.append(conf)

    def build(self) -> IConfigurationSection:
        context = {}
        for source in self.__sources:
            context = ConfigurationFactory.merge(context, source.load(self, ConfigurationFactory.Section(context)))
        for conf in self.__explicit_configs:
            context = ConfigurationFactory.merge(context, vars(conf))
        return ConfigurationFactory.Section(context)
