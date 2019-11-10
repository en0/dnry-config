from typing import List

from dnry.configuration.helpers import explode
from dnry.configuration.types import IConfigurationSource, IConfigurationFactory, IConfigurationSection
from argparse import ArgumentParser


class ArgumentSource(IConfigurationSource):
    """Read configuration values from an argparse.ArgumentParser object."""
    def __init__(self, argument_parser: ArgumentParser, argv: List[str] = None):
        self.__argv = argv
        self.__ap = argument_parser

    def load(self, fact: IConfigurationFactory, conf: IConfigurationSection) -> dict:
        opts = self.__ap.parse_args(self.__argv)
        return explode(vars(opts))
