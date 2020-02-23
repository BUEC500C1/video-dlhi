import os
import sys
import configparser

sys.path.append('./src')
sys.path.append('../')


def test_key_twitter_file():
    # Test if key file exists
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile('keys') is False:
        assert True
        return

    config = configparser.ConfigParser()
    config.read(thisfolder + "keys")

    # If key credential file exists, test twitter function
    from twitter import get_num_followers
    num = get_num_followers('michelleobama')
    assert num is not None
