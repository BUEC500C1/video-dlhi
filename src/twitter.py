import tweepy
from config import get_config_key
from util import current_dir

# Set up Twitter using credentials from a file named keys
# This keys file should be stored in the base directory

thisfolder = current_dir(__file__)

api_key = get_config_key('consumer_key')
api_secret_key = get_config_key('consumer_secret')
access_token = get_config_key('access_token')
access_token_secret = get_config_key('access_secret')

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class Twitter():
    def __init__(self, name, username, time_stamp, text, profile_pic, images):
        self.name = name
        self.username = "@" + username
        self.time_stamp = time_stamp
        self.text = text
        self.profile_pic = profile_pic
        self.images = images

    def get_profile_pic(self):
        return self.profile_pic

    def __repr__(self):
        return f'{{"name": {self.name}, "user": {self.username}, \
            "text": {self.text}, "media": {self.images}}}'

    def __str__(self):
        return f"{self.time}: @{self.username} - \"{self.text}\" \
            -- Media: {self.images}"

    def to_json(self):
        return {"name": self.name, "username": self.username,
                "text": self.text, "media": self.images}


def get_tweets(username):
    user_timeline = api.user_timeline(username, tweet_mode='extended')
    tweets = []

    for tweet in user_timeline:
        name = tweet.user.name
        username = "@" + tweet.user.screen_name
        time_stamp = tweet.created_at
        text = tweet.full_text
        profile_pic = tweet.user.profile_image_url_https.replace('\
        _normal', '')
        images = []

        # If there are any images, it will be in the entities extended section
        if 'media' in tweet.entities:
            for media in tweet.extended_entities['media']:
                if media.get("type", None) == "photo":
                    images.append(media["media_url"])

        tweets.append(Twitter(name, username, time_stamp, 
                              text, profile_pic, images))

    return tweets


def get_num_followers(username):
    user = api.get_user(username)
    return user.followers_count


if __name__ == '__main__':
    print("Main function")
    tweets = get_tweets('elonmusk')

    example_tweet = tweets[0]
    print(example_tweet.profile_pic)

    # tweets = get_tweets('DavidLi19628923')
    # example_tweet = tweets[0]
    '''
    print(f"name: {example_tweet.name}\nusername: {example_tweet.username}\n\
          time: {example_tweet.time_stamp}\ntext: {example_tweet.text}\n\
          profile_pic: {example_tweet.profile_pic}\n\
          images: {example_tweet.images}")
    '''
