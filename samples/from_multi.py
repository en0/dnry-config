from argparse import ArgumentParser

from dnry.config import ConfigFactory
from dnry.config.arg import ArgumentSource
from dnry.config.environ import EnvironmentSource
from dnry.config.in_memory import InMemorySource
from dnry.config.yaml import YamlSource


def main():

    print("Try running a few different ways.")
    print(" 1. Run without arguments")
    print(" 2. Add key1 under app in ./config1.yaml")
    print(" 2. Run with environment SAMPLE_app_key2 set with a value.")
    print(" 3. Run with commandline: --app:key2 'humans'")

    defaults = {
        "app": {
            "key1": "Hello",
            "key2": "World"
        }
    }

    ap = ArgumentParser(description="Full Example")
    ap.add_argument("--app:key1")
    ap.add_argument("--app:key2")

    fact = ConfigFactory()
    fact.add_source(InMemorySource(defaults))
    fact.add_source(EnvironmentSource("SAMPLE"))
    fact.add_source(YamlSource("./config1.yaml", False))
    fact.add_source(ArgumentSource(ap))

    conf = fact.build()
    print(f"{conf.get('app:key1')}, {conf.get('app:key2')}!")


if __name__ == "__main__":
    main()