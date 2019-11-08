import yaml
from typing import Union, List
from os.path import exists
from dnry_configuration.types import IConfigurationSource


class YamlSource(IConfigurationSource):
    def __init__(self, path: Union[str, List[str]], required: bool = False, **kwargs):
        self.__paths = path if isinstance(path, list) else [path]
        self.__required = required
        self.__loader = kwargs.get("loader", yaml.SafeLoader)

    def load(self) -> dict:
        path = self.__get_first_existing_path()
        if path is None and self.__required:
            paths = ",".join(self.__paths)
            raise RuntimeError(f"Configuration Error: None of these paths could be found: {paths}")

        with open(path, 'r') as f:
            # TODO: What happens if the yaml cannot be parsed?
            # It should probably raise even if not required because
            # the intent from the user was clearly to use the file.
            return yaml.load(f, Loader=self.__loader)

    def __get_first_existing_path(self) -> Union[str, None]:
        try:
            return next(p for p in self.__paths if exists(p))
        except StopIteration:
            return None
