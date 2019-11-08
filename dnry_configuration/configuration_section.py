from typing import Union

from dnry_configuration.types import IConfigurationSection


class ConfigurationSection(IConfigurationSection):
    def __init__(self, root: dict):
        self.__root = root

    def get(self, key: str) -> any:
        root = self.__root
        for k in key.split(":"):
            if k in root:
                root = root[k]
            else:
                return None
        return root

    def get_section(self, key: str) -> Union["IConfigurationSection", None]:
        val = self.get(key)
        if isinstance(val, dict):
            return ConfigurationSection(val)
        return None
