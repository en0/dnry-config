from typing import Union

from dnry.configuration.types import IConfigurationSection


class ConfigurationSection(IConfigurationSection):
    """Basic configuration section implementation.

    The basic implementation provides access to nested key values
    by separating namespace using a colon ':'.

    For example, given the following logical configuration tree:
        { "parent": { "child": "value" } }

    You could access "value" by using
        configuration.get("parent:child")
    """
    def __init__(self, root: dict):
        self.__dict__ = root

    def has(self, key: str) -> bool:
        root = self.__dict__
        for k in key.split(":"):
            if k in root:
                root = root[k]
            else:
                return False
        return True

    def get(self, key: str) -> any:
        root = self.__dict__
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
