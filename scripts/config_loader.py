import json


def load_devices(config_file):
    """
    Load device configuration from a JSON file.
    """

    with open(config_file, "r") as file:
        data = json.load(file)

    return data["devices"]