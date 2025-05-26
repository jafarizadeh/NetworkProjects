"""
dns_resolver.py
---------------
Simulates a basic DNS resolver by manually crafting and sending
a DNS query over UDP and parsing the response.

Author: GroupB
"""

import socket
import struct

from netutils.logger import Logger
from netutils.randomgen import SimpleRandom

# Logger and Random generator instances
log = Logger(name="DNSResolver", log_level="INFO")
rand = SimpleRandom(logger=log)

# DNS constants
DNS_SERVER = "8.8.8.8"
DNS_PORT = 53

def build_dns_query(domain):
    """
    Construct a DNS query packet for a given domain name.
    Returns (transaction_id, raw_packet).
    """
    tx_id = rand.randint(0, 65535)
    flags = 0x0100  # Standard query with recursion desired
    qdcount = 1     # One question

    # Header section (12 bytes)
    header = struct.pack(">HHHHHH", tx_id, flags, qdcount, 0, 0, 0)

    # Question section
    qname = b''.join(struct.pack("B", len(part)) + part.encode() for part in domain.split(".")) + b'\x00'
    qtype = 1   # Type A
    qclass = 1  # Class IN
    question = qname + struct.pack(">HH", qtype, qclass)

    return tx_id, header + question

def parse_dns_response(data, tx_id):
    """
    Parse a DNS response and extract A record IP address and TTL.
    """
    recv_id = struct.unpack(">H", data[:2])[0]
    if recv_id != tx_id:
        log.warn("Transaction ID mismatch – possible spoofed response.")
        return

    # Skip header (12 bytes) and question section
    offset = 12
    while data[offset] != 0:
        offset += 1 + data[offset]
    offset += 5  # Skip null byte + QTYPE(2) + QCLASS(2)

    try:
        # Assume one answer for simplicity
        offset += 2  # name pointer (2 bytes)
        rtype, rclass, ttl, rdlength = struct.unpack(">HHIH", data[offset:offset + 10])
        offset += 10
        rdata = data[offset:offset + rdlength]

        if rtype == 1 and rclass == 1:
            ip = ".".join(str(b) for b in rdata)
            log.info("Response: A record")
            log.info(f"Resolved IP: {ip}")
            log.info(f"TTL: {ttl} seconds")
        else:
            log.warn("Record type not supported or not an A record.")

    except Exception as e:
        log.error(f"Failed to parse response: {e}")

def main():
    try:
        domain = input("Enter domain to resolve: ").strip()
        if not domain:
            log.error("No domain provided.")
            return

        log.info(f"Querying: {domain}")
        tx_id, packet = build_dns_query(domain)

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.settimeout(5)
            sock.sendto(packet, (DNS_SERVER, DNS_PORT))
            response, _ = sock.recvfrom(512)
            parse_dns_response(response, tx_id)

    except socket.timeout:
        log.error("DNS query timed out.")
    except Exception as e:
        log.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
