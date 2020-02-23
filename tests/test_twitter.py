import os
import sys
import configparser

sys.path.append('./src')
sys.path.append('../')


def test_key_twitter_file():
    # Test if key file exists
    thisfolder = os.path.dirname(os.path.abspath(__file__))
    config = configparser.ConfigParser()
    if os.path.isfile('/../keys') is False:
        assert True
        return

    config.read(thisfolder + "/../keys")

    # If key credential file exists, test twitter function
    from twitter import get_num_followers
    num = get_num_followers('michelleobama')
    assert num is not None


def test_get_image():
    from twitter import get_image
    image = get_image("https://d233bqaih2ivzn.cloudfront.net/100/640x360.jpg")
    with open('./tests/test_image.jpg', 'rb') as f:
        requested_image = f.read()
    assert requested_image == image
