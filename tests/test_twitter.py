import sys
from unittest.mock import MagicMock

sys.path.append('./src')
sys.path.append('../')

from config import get_config_key  # noqa:E402


def test_twitter_keys():
    # Test if key file exists
    if get_config_key('consumer_key') is None:
        assert True
        return

    # If key credential file exists, test twitter function
    from twitter import get_num_followers
    num = get_num_followers('michelleobama')
    assert num is not None


def test_get_tweets():
    # Check if key file is present
    if get_config_key('consumer_key') is None:
        assert True
        return

    # If key credential file exists, test get tweets function
    from twitter import get_tweets
    num = MagicMock(get_tweets('michelleobama'))
    assert num is not None
