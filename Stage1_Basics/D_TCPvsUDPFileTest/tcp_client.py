import socket
from utils import now, get_file_hash, get_file_size

SERVER_IP = '127.0.0.1'
PORT = 5001
BUFFER_SIZE = 4096
INPUT_FILE = 'test_file.txt'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((SERVER_IP, PORT))

with open(INPUT_FILE, 'rb') as f:
    start = now()
    while chunk := f.read(BUFFER_SIZE):
        s.sendall(chunk)
    end = now()

s.close()
print("[TCP] File sent.")
print(f"Time: {end - start:.2f}s")
print(f"Size: {get_file_size(INPUT_FILE)} bytes")
print(f"MD5:  {get_file_hash(INPUT_FILE)}")
