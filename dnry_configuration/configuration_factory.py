from typing import List

from dnry_configuration.configuration_section import ConfigurationSection
from dnry_configuration.helpers import merge
from dnry_configuration.types import IConfigurationFactory, IConfigurationSource, IConfigurationSection


class ConfigurationFactory(IConfigurationFactory):

    __sources: List[IConfigurationSource]
    __merge = merge

    def __init__(self, sources: List[IConfigurationSource] = None):
        self.__sources = sources or list()

    def add_source(self, source: IConfigurationSource) -> None:
        self.__sources.append(source)

    def build(self) -> IConfigurationSection:
        context = {}
        for source in self.__sources:
            context = ConfigurationFactory.__merge(context, source.load(self))
        return ConfigurationSection(context)
