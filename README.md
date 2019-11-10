# DNRY-Configuration

A multi-source configuration library. 

The goal of DNRY-Configuration is to simplify configuration
loading and overriding.  With DNRY-Configuration you can 
easily specify several configuration sources and use them
from your application without dealing with the details.

DNRY-Configuration resolve conflicts and provides namespaced
access to keys to support well organized configuration files.

## Quick Start

Install DNRY-Configuration

```bash
pip install dnry_configuration
```

Read a Yaml file in your program.

```python
from dnry.configuration import ConfigurationFactory
from dnry.configuration.yaml import YamlSource

conf = ConfigurationFactory([
    YamlSource("./config1.yaml")
]).build()

config_value = conf.get("app:message")
```

There are many examples in the `samples/` directory.