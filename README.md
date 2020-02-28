# HW4: FFmpeg

## Summary
The API receives a Twitter handle which then converts the last 3 tweets of the user into a MP4 video. The API first uses the Tweepy library to grab the Twitter profile from the provided user. Then, the ffmpeg module initializes, where the tweets properties, such as the text and the images, are loaded into a function to create a single tweet image stored as JPEGs. These images are then fed into a function that generates a video for each individual tweet. After words, each of these generated videos are concatenated to one another to create one video MP4 file.

The user will be able to see the video generation status of his or her video. Once the video is finished processing, the user can download the processed video. 

Image and video generation are cleaned up at the end of each function call to prevent cluttering of files.

### Thread Execution for Parallel Processing
The API is capable of asynchronous requests through a backend implementation of of threads and queues. When an API call is made for **/createVideo**, a new task is added to the queue. The process of parallel execution is made possible by a Python feature called the ThreadPoolExecutor. With a maximum of four workers, the API is able to process four videos at a time. Whenever a new task is added to the queue, the ThreadPoolExecutor pops from the queue to process the request. The *get* request from the executor to the queue is blocking, so the need to check for a task is already automated.

My laptop has 2 Physical Cores and 4 Virtual Cores. I am able to run each video process on one thread for a total of 4 total workers working in parallel.

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
