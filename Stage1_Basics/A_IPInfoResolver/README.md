# A_IPInfoResolver

A lightweight Python utility that resolves basic information about a given domain name or IP address.

## Features

- Resolve domain name to IP address
- Fetch remote or local hostname
- Display system OS and network type
- Retrieve MAC address if target is in a local/private network
- Clean and structured terminal output

## Requirements

- Python 3.6+
- No third-party dependencies (uses standard library only)

## Usage

### Run the Script

```bash
python ip_info_resolver.py
```

### Example Interaction

```
Enter a domain or IP address: google.com

--- IP Information ---
Domain: google.com
Resolved IP: 142.250.181.206
Hostname: fra24s34-in-f14.1e100.net
OS: Linux 5.15.0-1051-azure, Network Type: Ethernet
MAC Address: Not available (remote host)
```

## Notes

- The script uses `socket`, `platform`, and `uuid` modules from Python's standard library.
- MAC address is only available for local/private IPs.
- Hostname may not be retrievable for all public IPs and may return `Not available`.

## Project Structure

```
A_IPInfoResolver/
├── ip_info_resolver.py     # Main Python script
└── README.md               # Project documentation
```

