import hashlib
import time
import os

def get_file_hash(filename, algo='md5'):
    h = hashlib.new(algo)
    with open(filename, 'rb') as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

def get_file_size(filename):
    return os.path.getsize(filename)

def now():
    return time.time()
