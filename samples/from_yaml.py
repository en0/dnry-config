from dnry.configuration import ConfigurationFactory
from dnry.configuration.yaml import YamlSource


def main():
    print("Edit the ./config1.yaml to change values.\n")
    factory = ConfigurationFactory()
    factory.add_source(YamlSource("./config1.yaml"))
    conf = factory.build()
    print("Key one is", conf.get("key:one"))


if __name__ == "__main__":
    main()
