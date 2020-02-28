import os


def current_dir(filename):
    return os.path.dirname(os.path.abspath(filename))


def parent_dir(filename):
    return os.path.dirname(current_dir(filename))
