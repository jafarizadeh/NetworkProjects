import socket
import uuid
import platform
import ipaddress
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_local_ip(ip_address):
    """Check if the given IP address belongs to a private/local network."""
    try:
        ip = ipaddress.ip_address(ip_address)
        return ip.is_private
    except ValueError:
        logging.warning("Invalid IP address format: %s", ip_address)
        return False

def get_mac_address():
    """Return the MAC address of the local machine."""
    mac_num = uuid.getnode()
    mac_hex = f"{mac_num:012X}"
    return ":".join(mac_hex[i:i + 2] for i in range(0, 12, 2))

def resolve_ip_info(target):
    """Resolve and log information about the given domain or IP address."""
    logging.info("Resolving target: %s", target)

    try:
        ip_address = socket.gethostbyname(target)
        logging.debug("Resolved IP address: %s", ip_address)
    except socket.gaierror:
        logging.error("Invalid domain or IP address: %s", target)
        return

    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        hostname = "Not available"
        logging.warning("Hostname not available for IP: %s", ip_address)

    os_info = f"{platform.system()} {platform.release()}"
    network_type = "Ethernet"  # Placeholder for future enhancement
    mac_address = get_mac_address() if is_local_ip(ip_address) else "Not available (remote host)"

    logging.info("--- IP Information ---")
    logging.info("Domain: %s", target)
    logging.info("Resolved IP: %s", ip_address)
    logging.info("Hostname: %s", hostname)
    logging.info("OS: %s, Network Type: %s", os_info, network_type)
    logging.info("MAC Address: %s", mac_address)

def main():
    try:
        user_input = input("Enter a domain or IP address: ").strip()
        if not user_input:
            logging.error("No input provided. Exiting.")
            return
        resolve_ip_info(user_input)
    except KeyboardInterrupt:
        logging.info("Program interrupted by user.")

if __name__ == "__main__":
    main()
