# HW4: FFmpeg

## Twitter Setup
Create a Twitter Development Account to obtain 4 distinct keys. You will need to create a **keys** file in the base directory with the following content:

```
[auth]

consumer_key = your_api_key
consumer_secret = your_api_secret_key
access_token = your_access_token
access_token_secret = your_access_token_secret
```

## Setting up the API
Create a virtual environment.
```
virtualenv -p /usr/bin/python3 venv
```

Install all the required dependencies through pip install.
```
pip3 install -r requirements.txt 
```

## Using the API
The user can use 4 different requests to the API:

1. /getLastTweet - Returns the desired user's last tweet in JSON format
2. /getNumFollowers - Returns the desired user's number of followers.
3. /createVideo - Create a video for the desired user's last 3 tweets.
4. /getVideo - Download the video using the provided UUID.

### Below are examples of these commands:

Ask the API to create a video for Michelle Obama
```
curl http://127.0.0.1:5000/createVideo?handle="michelleobama"
```
This returns:
> "Video for user michelleobama started! UUID: 6aa77ebfff1c46248755cf507dbbf857"

To view the status of your video, use the following command:
```
curl http://127.0.0.1:5000/getStatus?uuid=6aa77ebfff1c46248755cf507dbbf857
```

To download the video in the current directory of the terminal, use the following command:
```
curl http://127.0.0.1:5000/getVideo?uuid=6aa77ebfff1c46248755cf507dbbf857 --output video.mp4
```

Note! When downloading the video, if you submit a **/getVideo** request without the --output flag, you will not be able to download your video again. You will have to resubmit another **/createVideo** request.