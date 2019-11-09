import os
from argparse import ArgumentParser

from dnry_configuration.configuration_factory import ConfigurationFactory
from dnry_configuration.enviroment import EnvironmentSource


def main():
    print("To test, execute as:\n$ SAMPLE_key=value python ./from_environment.py\n")
    factory = ConfigurationFactory()
    factory.add_source(EnvironmentSource("SAMPLE"))
    conf = factory.build()
    print("Key one is", conf.get("key"))


if __name__ == "__main__":
    main()
