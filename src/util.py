import os


def current_dir(filename):
    return os.path.dirname(os.path.abspath(filename))


def parent_dir(filename):
    thisfolder = os.path.dirname(os.path.abspath(filename))
    return os.path.dirname(thisfolder)
