#!/usr/bin/env python3
"""
subnet_scan.py

Simple ICMP reachability scanner across a subnet.
"""

import ipaddress
import subprocess
import sys


def ping_host(ip: str) -> bool:
    try:
        subprocess.check_output(
            ["ping", "-c", "1", "-W", "1", str(ip)],
            stderr=subprocess.DEVNULL,
        )
        return True
    except Exception:
        return False


def scan_subnet(cidr: str) -> None:
    net = ipaddress.ip_network(cidr, strict=False)
    print(f"Scanning subnet: {cidr}")

    for ip in net.hosts():
        if ping_host(ip):
            print(f"[+] Host reachable: {ip}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python subnet_scan.py <cidr>")
        sys.exit(1)

    scan_subnet(sys.argv[1])
