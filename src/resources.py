from flask import jsonify, send_file
from flask_restful import Resource

from webargs import fields
from webargs.flaskparser import use_args

from twitter import get_tweets, get_num_followers

import uuid
from ffmpeg_converter import removeVideo, uuid_keys
from worker import workerQ


class LastTweet(Resource):
    @use_args({"handle": fields.Str(required=True)})
    def get(self, args):
        tweets = get_tweets(args["handle"])
        return jsonify(tweets[0].to_json())


class NumFollowers(Resource):
    @use_args({"handle": fields.Str(required=True)})
    def get(self, args):
        username = args["handle"]
        num = get_num_followers(username)
        return jsonify(f"handle: {username}, followers: {num}")


class CreateTweetVideo(Resource):
    @use_args({"handle": fields.Str(required=True)})
    def get(self, args):
        username = args["handle"]
        unique_code = uuid.uuid4().hex
        workerQ.put((username, unique_code))
        uuid_keys.append(unique_code)
        print("Added KEY: ", uuid_keys)
        # create_video(username)
        return f'Video for user {username} started! UUID: {unique_code}'


class getStatus(Resource):
    @use_args({"uuid": fields.Str(required=True)})
    def get(self, args):
        uuid = args["uuid"]
        if uuid in uuid_keys:
            return "Not done, please wait"
        else:
            return "Finished!"


class SendTweetVideo(Resource):
    @use_args({"uuid": fields.Str(required=True)})
    def get(self, args):
        uuid = args["uuid"]
        if uuid in uuid_keys:
            return "Not done, please wait"
        else:
            try:
                video = send_file(f'videos/{uuid}.mp4',
                                  attachment_filename=f'{uuid}.mp4')
                removeVideo(uuid)
                return video
            except FileNotFoundError:
                return "File Not Found"
