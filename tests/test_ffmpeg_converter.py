import os
import sys
from io import BytesIO

sys.path.append('../src')


def test_get_image():
    from ffmpeg_converter import get_image
    image = get_image("https://d233bqaih2ivzn.cloudfront.net/100/640x360.jpg")
    with open('./tests/test_image.jpg', 'rb') as f:
        requested_image = f.read()
    assert requested_image == image


def test_resize_image():
    from ffmpeg_converter import resize_image
    url = "https://d233bqaih2ivzn.cloudfront.net/100/640x360.jpg"
    image = resize_image('1', url, '1', '1', 'image')
    imgByteArr = BytesIO()
    image.save(imgByteArr, format='jpeg')
    imgByteArr = imgByteArr.getvalue()

    with open('./tests/test_image_resized.jpeg', 'rb') as f:
        requested_image = f.read()

    os.remove('./img/1-1.jpeg')
    assert requested_image == imgByteArr


# This test only works if keys file is in home directory
# def test_create_single_tweet():
#     from ffmpeg_converter import create_video, uuid_keys
#     uuid_keys.append('testing')
#     string = create_video('michelleobama', 'testing')
#     assert string == "UUID Removed"
