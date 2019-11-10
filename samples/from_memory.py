from dnry.config import ConfigFactory
from dnry.config.in_memory import InMemorySource


def main():
    print("Reads values from an in-memory configuration\n")
    fact = ConfigFactory()
    fact.add_source(InMemorySource({
        "key": {"one": "value"}
    }));
    conf = fact.build()
    print("key is", conf.get("key:one"))


if __name__ == "__main__":
    main()