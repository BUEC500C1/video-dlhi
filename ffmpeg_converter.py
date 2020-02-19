import os
import ffmpeg
from PIL import Image
from io import BytesIO
from textwrap import wrap
from twitter import get_tweets, get_image


# Resize image to predetermined size
def resize_image(num_images, url, unique_code, position):
    img = get_image(url)

    basewidth = 350

    img = Image.open(BytesIO(img))
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)

    img.save(f'img/{unique_code}-{position}.jpeg', format="jpeg")

    return f'img/{unique_code}-{position}.jpeg'


def create_single_tweet(pos, handle, tweet, unique_code):
    stream = ffmpeg.input(
        'img/white.jpg',
        pattern_type='glob',
        framerate=1
    )

    stream = ffmpeg.overlay(
        stream,
        ffmpeg.input(tweet.profile_pic),
        x=100,
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
        x=200,
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
        x=200, y=100
    )

    stream = ffmpeg.drawtext(
        stream,
        text=tweet.time_stamp,
        font="fonts/OpenSansEmoji.ttf",
        fontsize=25,
        box=1,
        boxborderw=15,
        escape_text=True,
        x=1200,
        y=50
    )

    wrapped_tweet = wrap(tweet.text, 50)

    # The y value where the text begins
    vertical_y = 200

    for i, line in enumerate(wrapped_tweet):
        stream = ffmpeg.drawtext(
            stream,
            text=line,
            fontfile="fonts/OpenSansEmoji.ttf",
            fontsize=28,
            box=1,
            boxborderw=15,
            escape_text=True,
            x=200,
            y=200+(50 * i)
        )
        # Remember the offset for each new line of text
        vertical_y = vertical_y + (50 * (i + 1))

    num_images = len(tweet.images)

    if num_images != 0:
        for position in range(0, num_images):
            # resize the image and return the location
            # The order of images depebds on the number of images
            url = resize_image(num_images, tweet.images[position],
                               unique_code, position)

            if position < 2:
                stream = ffmpeg.overlay(
                    stream,
                    ffmpeg.input(url),
                    x=200 + (position * 400),
                    # Incorporate the offset and start below the final
                    # line of text
                    y=vertical_y
                )
            else:
                stream = ffmpeg.overlay(
                    stream,
                    ffmpeg.input(url),
                    x=200 + ((position - 2) * 400),
                    # Start another row of pictures
                    y=vertical_y + 300
                )

    stream = ffmpeg.output(stream, f'videos/{unique_code}-{pos}.mp4',
                           loglevel='panic')
    ffmpeg.run(stream)


def generate_indiv_slides(handle, unique_code):
    # Obtain the previous tweets from the desired user
    tweets = get_tweets(handle)
    # Store the number of tweets fetched, number is generally 20
    # num_tweets = len(tweets)

    # Default number of tweets fetched to 3
    num_tweets = 3

    # Generate videos for individual tweets
    for position in range(0, num_tweets):
        create_single_tweet(position, handle, tweets[position], unique_code)

    return num_tweets


def tweets_to_video(unique_code, num_tweets):
    all_tweets = []
    # Create a 'slide' of each tweet and store inside dir video
    for p in range(0, num_tweets):
        all_tweets.append(ffmpeg.input(f'videos/{unique_code}-{p}.mp4'))

    stream = ffmpeg.concat(*all_tweets)
    # stream = ffmpeg.overwrite_output(stream)
    stream = ffmpeg.output(stream, f'videos/{unique_code}.mp4',
                           loglevel='panic')
    ffmpeg.run(stream)


def create_video(user, unique_code):
    num_tweets = generate_indiv_slides(user, unique_code)
    tweets_to_video(unique_code, num_tweets)

    # Clean up files
    for i in range(0, num_tweets):
        try:
            os.remove(f"img/{unique_code}-{i}.jpeg")
        except FileNotFoundError:
            pass

        os.remove(f"videos/{unique_code}-{i}.mp4")


def removeVideo(unique_code):
    print(unique_code)
    try:
        os.remove(f"videos/{unique_code}.mp4")
    except FileNotFoundError:
        print("Error removing generated file!")


if __name__ == '__main__':
    create_video('michelleobama', "ba241")
