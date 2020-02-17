import ffmpeg
from textwrap import wrap
from twitter import get_tweets


def create_single_tweet(tweet):
    stream = ffmpeg.input(
        'img/white.jpg',
        pattern_type='glob',
        framerate=60
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

    stream = ffmpeg.output(stream, 'movie.mp4')
    ffmpeg.run(stream)


def create_video(person):
    tweets = get_tweets(person)
    one = tweets[0]
    create_single_tweet(one)


if __name__ == '__main__':
    print("Main function!")
    create_video('BR_MLB')
