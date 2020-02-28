import sys

sys.path.append('./src')
sys.path.append('../')

from config import get_config_key  # noqa:E402


def test_key_twitter_file():
    # Test if key file exists
    if get_config_key('consumer_key') is None:
        assert True
        return

    # If key credential file exists, test twitter function
    from twitter import get_num_followers
    num = get_num_followers('michelleobama')
    assert num is not None
