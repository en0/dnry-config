from dnry_configuration.arg import ArgumentSource
from dnry_configuration.configuration_factory import ConfigurationFactory
from dnry_configuration.memory import InMemorySource


def main():
    print("Reads vaules from an in-memory configuration\n")
    fact = ConfigurationFactory()
    fact.add_source(InMemorySource({
        "key": {"one": "value"}
    }));
    conf = fact.build()
    print("key is", conf.get("key:one"))


if __name__ == "__main__":
    main()