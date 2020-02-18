import ffmpeg
from PIL import Image
from io import BytesIO
from textwrap import wrap
from twitter import get_tweets


# Resize image to predetermined size
def resize_image(image):
    baseheight = 400

    img = Image.open(image)
    hpercent = (baseheight / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(hpercent)))
    img = img.resize((wsize, baseheight), Image.ANTIALIAS)

    temp = BytesIO()
    img.save(temp, format="jpeg")

    return temp


def create_single_tweet(position, handle, tweet):
    stream = ffmpeg.input(
        'img/white.jpg',
        pattern_type='glob',
        framerate=1
    )

    print(tweet.get_profile_pic())

    stream = ffmpeg.overlay(
        stream,
        ffmpeg.input(tweet.profile_pic),
        x=200,
        y=75
    )

    stream = ffmpeg.drawtext(
        stream,
        text=tweet.name,
        font="fonts/OpenSansEmoji.ttf",
        fontsize=25,
        box=1,
        boxborderw=15,
        escape_text=True,
        x=300,
        y=50
    )

    stream = ffmpeg.drawtext(
        stream,
        text=tweet.username,
        font="fonts/OpenSansEmoji.ttf",
        fontsize=25,
        box=1,
        boxborderw=15,
        escape_text=True,
        x=300, y=100
    )

    wrapped_tweet = wrap(tweet.text, 50)

    for i, line in enumerate(wrapped_tweet):
        stream = ffmpeg.drawtext(
            stream,
            text=line,
            fontfile="fonts/OpenSansEmoji.ttf",
            fontsize=28,
            box=1,
            boxborderw=15,
            escape_text=True,
            x=300,
            y=200 + (50 * i)
        )

    stream = ffmpeg.output(stream, f'videos/{handle}-{position}.mp4')
    ffmpeg.run(stream)


def generate_indiv_slides(handle):
    # Obtain the previous tweets from the desired user
    tweets = get_tweets(handle)
    # Store the number of tweets fetched, number is generally 20
    num_tweets = len(tweets)

    # Generate videos for individual tweets
    for position in range(0, 3):
        create_single_tweet(position, handle, tweets[position])


def create_video(handle):
    all_tweets = []
    # Create a 'slide' of each tweet and store inside dir video
    for position in range(0, 3):
        all_tweets.append(ffmpeg.input(f'videos/{handle}-{position}.mp4'))

    stream = ffmpeg.concat(*all_tweets)
    # stream = ffmpeg.overlay(stream, ffmpeg.input(profile_pic))
    # stream = ffmpeg.drawbox(stream, 0, 0, 400, 400, color='black', thickness=10)
    stream = ffmpeg.output(stream, f'videos/{handle}.mp4')
    ffmpeg.run(stream)

    # (
    #     ffmpeg
    #     .concat(*all_tweets)
    #     #.overlay(ffmpeg.input(status[0]._json["user"]["profile_image_url_https"][:-11] + ".jpg"))
    #     #.drawbox(0, 0, 400, 400, color='black', thickness=10)
    #     .output(f'videos/{handle}.mp4')
    #     .run()
    # )


if __name__ == '__main__':
    print("Main function!")
    generate_indiv_slides('DavidLi19628923')
    # create_video('DavidLi19628923')
