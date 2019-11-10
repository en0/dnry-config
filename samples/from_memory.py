from dnry.configuration import ConfigurationFactory
from dnry.configuration.in_memory import InMemorySource


def main():
    print("Reads values from an in-memory configuration\n")
    fact = ConfigurationFactory()
    fact.add_source(InMemorySource({
        "key": {"one": "value"}
    }));
    conf = fact.build()
    print("key is", conf.get("key:one"))


if __name__ == "__main__":
    main()