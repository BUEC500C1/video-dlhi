import queue
from ffmpeg_converter import create_video
from concurrent.futures import ThreadPoolExecutor

workerQ = queue.Queue()


def workerDispatcher():
    with ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            username, unique_code = workerQ.get()
            print(f"Processing Video for handle user {username} . . .")
            executor.submit(create_video, username, unique_code)
