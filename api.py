from flask import Flask
from flask_restful import Api

from resources import LastTweet, NumFollowers, CreateTweetVideo
from resources import SendTweetVideo, getStatus

from worker import workerDispatcher
from threading import Thread

app = Flask(__name__)
api = Api(app)

api.add_resource(LastTweet, '/getLastTweet')
api.add_resource(NumFollowers, "/getNumFollowers")
api.add_resource(CreateTweetVideo, "/createVideo")
api.add_resource(getStatus, "/getStatus")
api.add_resource(SendTweetVideo, "/getVideo")

workerDispatcherThread = Thread(target=workerDispatcher, daemon=True)
workerDispatcherThread.start()


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
