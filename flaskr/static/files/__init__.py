import os

def file_path():
    files = os.listdir()
    path = os.path.dirname(__file__)
    print(files)
    print(path)
