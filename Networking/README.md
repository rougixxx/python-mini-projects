# Networking Projects

Using Python to Do Some Networking related Stuff.

## Requirements
```bash
python3 -m pip install scapy
```
```bash
python3 -m pip install dnspython
```
```bash
python3 -m pip install socket
```
```bash
python3 -m pip install python-geoip
```
```bash
python3 -m pip install wifi
```

## Scripts:
- `arp_spoofer.py`: ARP Spoofing Attack using Scapy package:
```bash
python3 arp_spoofer.py
```
- `dns_lookup.py`: DNS lookup using dsnpython package on a given IP/DOMAIN:
```bash
python3 dns_lookup.py
```
- `network_scanner.py`: simple Network scanner using Scapy package to scan all Hosts on a Local Network:
```bash
python3 network_scanner.py
```
- `network_scanner2.py`: an Improved version of the previous network scanner:
```bash
python3 network_scanner2.py
```
- `network_sniffer.py`: a Simple Packet analyzer-like Wireshark to scan for ICMP,TCP,UDP packets using scapy module
```bash
python3 network_sniffer.py
```
- `port_scanner.py`: scanning for open ports using the socket module
```bash
python3 port_scanner.py
```
- `wifi_scanner.py`: scanning wifi networks with details Informations about each network using wifi module
```bash
python3 wifi_scanner.py
```
