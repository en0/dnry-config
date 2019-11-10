from argparse import ArgumentParser

from dnry.configuration import ConfigurationFactory, IConfigurationSection, IConfigurationFactory
from dnry.configuration.arg import ArgumentSource
from dnry.configuration.delegate import DelegateSource
from dnry.configuration.in_memory import InMemorySource
from dnry.configuration.yaml import YamlSource


def add_sources(fact: IConfigurationFactory, conf: IConfigurationSection):
    # Add defaults
    fact.add_source(InMemorySource({"greeting": "Hello"}))

    # If the user specified a configuration file, load it.
    if conf.has("config"):
        fact.add_source(YamlSource(conf.get("config")))

    # The parsed command line is passed in in conf. Adding this to the factory
    # will allow CLI inputs to override keys from previous sources if they
    # are specified
    fact.add_configuration(conf)


def main():
    ap = ArgumentParser()
    ap.add_argument("--config")
    ap.add_argument("--name", default="world")
    fact = ConfigurationFactory()
    fact.add_source(ArgumentSource(ap))
    fact.add_source(DelegateSource(add_sources))
    conf = fact.build()
    print(f"{conf.get('greeting')}, {conf.get('name')}!")


if __name__ == "__main__":
    main()
