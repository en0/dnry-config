from argparse import ArgumentParser

from dnry_configuration.arg import ArgumentSource
from dnry_configuration.configuration_factory import ConfigurationFactory


def main():
    print("Execute as:\n $ python from_args.py --key value\n")
    ap = ArgumentParser(description="Sample from arguments")
    ap.add_argument("--key")
    fact = ConfigurationFactory()
    fact.add_source(ArgumentSource(ap))
    conf = fact.build()
    print("key is", conf.get("key"))


if __name__ == "__main__":
    main()