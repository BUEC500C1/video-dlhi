import os
import tweepy
import configparser

# Set up Twitter using credentials from a file named keys
# This keys file should be stored in the base directory
config = configparser.ConfigParser()

thisfolder = os.path.dirname(os.path.abspath(__file__))

try:
    config.read(thisfolder + "/../keys")

    api_key = config.get('auth', 'consumer_key').strip()
    api_secret_key = config['auth']['consumer_secret']
    access_token = config['auth']['access_token']
    access_token_secret = config['auth']['access_secret']

    auth = tweepy.OAuthHandler(api_key, api_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

except FileNotFoundError:
    print("No Key file found!")


class Twitter():
    def __init__(self, tweet):
        self.name = tweet.user.name
        self.username = "@" + tweet.user.screen_name
        self.time_stamp = tweet.created_at
        self.text = tweet.full_text
        self.profile_pic = tweet.user.profile_image_url_https.replace('\
            _normal', '')
        self.images = []

        # If there are any images, it will be in the entities extended section
        if 'media' in tweet.entities:
            for media in tweet.extended_entities['media']:
                if media.get("type", None) == "photo":
                    self.images.append(media["media_url"])

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
    tweets = [Twitter(tweet) for tweet in user_timeline]
    return tweets


def get_num_followers(username):
    user = api.get_user(username)
    return user.followers_count


if __name__ == '__main__':
    print("Main function")
    tweets = get_tweets('michelleobama')
    # tweets = get_tweets('DavidLi19628923')
    # example_tweet = tweets[0]
    '''
    print(f"name: {example_tweet.name}\nusername: {example_tweet.username}\n\
          time: {example_tweet.time_stamp}\ntext: {example_tweet.text}\n\
          profile_pic: {example_tweet.profile_pic}\n\
          images: {example_tweet.images}")
    '''
    for i in range(0, 4):
        # print(tweets[i].get_profile_pic())
        # print(tweets[i].get_images())
        print(tweets[i].images)
