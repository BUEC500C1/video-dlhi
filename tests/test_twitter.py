import sys
from unittest.mock import MagicMock
import twitter

sys.path.append('./src')
sys.path.append('../')

from config import get_config_key  # noqa:E402

if get_config_key('consumer_key') is None:
    # Mock out all instances of get_tweets
    twitter.get_tweets = MagicMock(return_value=[twitter.Twitter(
        "Elon Musk", "elonmusk", 'Test Morning', "Hello Testers!",
        './img/tests/elon_profile_pic.jpg', [])])
    twitter.get_num_followers = MagicMock(return_value=10)


def test_twitter_keys():
    # Test if key file exists
    if get_config_key('consumer_key') is None:
        elon_tweet = twitter.get_tweets
        assert elon_tweet is not None

    # If key credential file exists, test twitter function
    num = twitter.get_num_followers('elonmusk')
    assert num is not None


def test_get_tweets():
    # Check if key file is present
    if get_config_key('consumer_key') is None:
        elon_num = twitter.get_num_followers
        assert elon_num is not None

    # If key credential file exists, test get tweets function
    num = twitter.get_tweets('elonmusk')
    assert num is not None
