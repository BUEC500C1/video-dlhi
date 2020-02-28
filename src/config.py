import os
import configparser
from util import parent_dir


parentfolder = parent_dir(__file__)


def get_config_key(key, section='auth'):
    if os.path.exists(parentfolder + '/keys'):
        config_parser = configparser.ConfigParser()
        config_parser.read(parentfolder + '/keys')
        return config_parser.get(section, key).strip()
    return None
