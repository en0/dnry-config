import os
from argparse import ArgumentParser

from dnry.config import ConfigFactory
from dnry.config.environ import EnvironmentSource


def main():
    print("To test, execute as:\n$ SAMPLE_key=value python ./from_environment.py\n")
    factory = ConfigFactory()
    factory.add_source(EnvironmentSource("SAMPLE"))
    conf = factory.build()
    print("Key one is", conf.get("key"))


if __name__ == "__main__":
    main()
