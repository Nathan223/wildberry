import os


def getImage(filename):
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname,filename)