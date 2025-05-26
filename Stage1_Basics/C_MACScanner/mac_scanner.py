"""
mac_scanner.py
--------------
Scans the local ARP/neighbor cache and prints IP-to-MAC mappings.
Supports both Windows and Linux using OS commands and regex parsing.
"""

import platform
import subprocess
import re
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from utils.my_logging import Logger
from utils.my_tabulate import print_table

log = Logger(name="MACScanner", log_level="INFO")

def is_windows():
    return platform.system().lower() == "windows"

def get_arp_output():
    """
    Executes the appropriate system command to get ARP or neighbor table.
    """
    try:
        cmd = ["arp", "-a"] if is_windows() else ["ip", "neigh"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except Exception as e:
        log.error(f"Failed to get ARP table: {e}")
        return ""

def parse_output(raw_output):
    """
    Parse raw command output and extract list of (IP, MAC, Interface) entries.
    """
    entries = []
    if is_windows():
        in_data_block = False
        for line in raw_output.splitlines():
            line = line.strip()
            if line.lower().startswith("internet address"):
                in_data_block = True
                continue
            if in_data_block and line:
                parts = re.split(r"\s{2,}", line)
                if len(parts) == 3:
                    ip, mac, _ = parts
                    if re.match(r"(\d{1,3}\.){3}\d{1,3}", ip) and re.match(r"([0-9a-fA-F]{2}[-:]){5}[0-9a-fA-F]{2}", mac):
                        mac = mac.replace("-", ":").lower()
                        entries.append([ip, mac, "N/A"])

    else:
        pattern = re.compile(r"(\\d+\\.\\d+\\.\\d+\\.\\d+)\\s+dev\\s+(\\w+).*lladdr\\s+([\\da-fA-F:]{17})")
        for line in raw_output.splitlines():
            match = pattern.search(line)
            if match:
                ip, interface, mac = match.groups()
                entries.append([ip, mac.lower(), interface])
    return entries

def main():
    log.info("Scanning local network for ARP entries...")
    raw = get_arp_output()
    parsed = parse_output(raw)
    if not parsed:
        log.warn("No entries found. Try pinging some local devices to populate ARP cache.")
    else:
        print_table(["IP Address", "MAC Address", "Interface"], parsed)

if __name__ == "__main__":
    main()
