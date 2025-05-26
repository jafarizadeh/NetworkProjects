import socket
from utils import get_file_hash, get_file_size, now

HOST = '0.0.0.0'
PORT = 5001
BUFFER_SIZE = 4096
OUTPUT_FILE = 'received_tcp.txt'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print("[TCP] Waiting for connection...")

conn, addr = s.accept()
print(f"[TCP] Connected by {addr}")

with open(OUTPUT_FILE, 'wb') as f:
    start = now()
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        f.write(data)
    end = now()

conn.close()
print("[TCP] Transfer complete.")
print(f"Time: {end - start:.2f}s")
print(f"Size: {get_file_size(OUTPUT_FILE)} bytes")
print(f"MD5:  {get_file_hash(OUTPUT_FILE)}")
