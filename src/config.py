import os
import configparser

thisfolder = os.path.dirname(os.path.abspath(__file__))
parentfolder = os.path.dirname(thisfolder)


def get_config_key(key, section='auth'):
    if os.path.exists(parentfolder + '/keys'):
        config_parser = configparser.ConfigParser()
        config_parser.read(parentfolder + '/keys')
        return config_parser.get(section, key).strip()
    return None
