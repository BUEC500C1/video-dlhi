import os
import configparser


def get_config_key(key, section='auth'):
    if os.path.exists('../keys'):
        config_parser = configparser.ConfigParser()
        config_parser.read("../keys")
        return config_parser.get(section, key).strip()
    return None
