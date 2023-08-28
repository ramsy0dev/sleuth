import json

from rich import print

from sleuth.utils.clock import clock

def print_config(config: dict) -> None:
    """ Prints the config in a beautified way """
    config = json.dumps(
        config,
        indent=7
    )
    config_with_clock = "\n".join([f"{clock()}{' '*13}{line}" for line in config.split("\n")])

    print(config_with_clock)
