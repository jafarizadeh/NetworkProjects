import socket
from utils import get_file_hash, get_file_size, now

HOST = '0.0.0.0'
PORT = 5002
BUFFER_SIZE = 4096
OUTPUT_FILE = 'received_udp.txt'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
print("[UDP] Waiting for packets...")

with open(OUTPUT_FILE, 'wb') as f:
    s.settimeout(5.0)
    start = now()
    while True:
        try:
            data, addr = s.recvfrom(BUFFER_SIZE)
            if data == b'__END__':
                break
            f.write(data)
        except socket.timeout:
            break
    end = now()

print("[UDP] Transfer complete.")
print(f"Time: {end - start:.2f}s")
print(f"Size: {get_file_size(OUTPUT_FILE)} bytes")
print(f"MD5:  {get_file_hash(OUTPUT_FILE)}")
