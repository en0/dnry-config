import os
from argparse import ArgumentParser

from dnry.configuration import ConfigurationFactory
from dnry.configuration.environ import EnvironmentSource


def main():
    print("To test, execute as:\n$ SAMPLE_key=value python ./from_environment.py\n")
    factory = ConfigurationFactory()
    factory.add_source(EnvironmentSource("SAMPLE"))
    conf = factory.build()
    print("Key one is", conf.get("key"))


if __name__ == "__main__":
    main()
