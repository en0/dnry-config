from dnry.config import ConfigFactory
from dnry.config.yaml import YamlSource


def main():
    print("Edit the ./config1.yaml to change values.\n")
    factory = ConfigFactory()
    factory.add_source(YamlSource("./config1.yaml"))
    conf = factory.build()
    print("Key one is", conf.get("key:one"))


if __name__ == "__main__":
    main()
