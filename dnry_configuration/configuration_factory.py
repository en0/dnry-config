from typing import List

from dnry_configuration.configuration_section import ConfigurationSection
from dnry_configuration.types import IConfigurationFactory, IConfigurationSource, IConfigurationSection


def merge(a: dict, b: dict) -> dict:
    queue = list()
    ret = dict()
    queue.append((ret, a, b))
    while len(queue) > 0:
        root, left, right = queue.pop()
        for rk, rv in right.items():
            if rk not in left:
                root[rk] = rv
            elif isinstance(rv, list) and isinstance(left[rk], list):
                root[rk] = left[rk] + rv
            elif isinstance(rv, dict) and isinstance(left[rk], dict):
                root[rk] = {}
                queue.append((root[rk], left[rk], rv))
            else:
                root[rk] = rv
        for lk, lv in left.items():
            if lk not in right:
                root[lk] = lv
    return ret


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
            context = ConfigurationFactory.__merge(context, source.load())
        return ConfigurationSection(context)
