import requests
import os

def read_in_chunk(file_object, CHUNK_SIZE):
    while True:
        

def upload_file(file):

    content_name = str(file)
    content_path = os.path.abspath(content_name)
    content_size = os.stat(content_path.st_size)

    file_object = open(content_path, 'rb')
    index = 0
    offset = 0
    headers = {}
    CHUNK_SIZE = 1024

    for chunk