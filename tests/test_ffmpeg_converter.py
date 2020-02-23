import sys
from io import BytesIO

sys.path.append('../src')


def test_resize_image():
    from ffmpeg_converter import resize_image
    url = "https://d233bqaih2ivzn.cloudfront.net/100/640x360.jpg"
    image = resize_image('1', url, '1', '1', 'image')
    imgByteArr = BytesIO()
    image.save(imgByteArr, format='jpeg')
    imgByteArr = imgByteArr.getvalue()

    with open('./tests/test_image_resized.jpeg', 'rb') as f:
        requested_image = f.read()
    assert requested_image == imgByteArr
