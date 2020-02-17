import tweepy
import requests
import configparser

# Set up Twitter using credentials from a Config file
config = configparser.ConfigParser()
config.read("config.cfg")

api_key = config['DEFAULT']['api_key']
api_secret_key = config['DEFAULT']['api_secret_key']
access_token = config['DEFAULT']['access_token']
access_token_secret = config['DEFAULT']['access_token_secret']

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


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
                    self.images.append({"image": media["media_url"]})

    def __repr__(self):
        return f'{{"user": {self.username}, "text": {self.text},\
             "media": {self.images}}}'

    def __str__(self):
        return f"{self.time}: @{self.username} - \"{self.text}\" \
            -- Media: {self.images}"

    def to_json(self):
        return {"user": self.username, "text": self.text, "media": self.images}


def get_tweets(username):
    user_timeline = api.user_timeline(username, tweet_mode='extended')
    tweets = [Twitter(tweet) for tweet in user_timeline]
    return tweets


def get_num_followers(username):
    user = api.get_user(username)
    return user.followers_count


def get_image(url):
    response = requests.get(url, stream=True)
    image = response.content
    return image


if __name__ == '__main__':
    print("Main function")
    tweets = get_tweets('michelleobama')
    example_tweet = tweets[0]
    print(f"name: {example_tweet.name}\nusername: {example_tweet.username}\n\
          time: {example_tweet.time_stamp}\ntext: {example_tweet.text}\n\
          profile_pic: {example_tweet.profile_pic}\n\
          images: {example_tweet.images}")
