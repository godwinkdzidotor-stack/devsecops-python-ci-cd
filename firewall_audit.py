#!/usr/bin/env python3
"""
firewall_audit.py

Reads a CSV of firewall rules and flags overly-permissive entries.
Expected columns:
    name, src, dst, service, action
"""

import csv
import sys


def is_overly_permissive(value: str) -> bool:
    value = (value or "").lower()
    return value in ["any", "0.0.0.0/0", "0.0.0.0"]


def audit_rules(path: str) -> None:
    with open(path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)

        print(f"{'Name':<20} {'Src':<18} {'Dst':<18} {'Service':<10} Finding")
        print("-" * 80)

        for row in reader:
            name = row.get("name", "")
            src = row.get("src", "")
            dst = row.get("dst", "")
            service = row.get("service", "")
            action = row.get("action", "").lower()

            finding = ""

            if action == "allow" and (is_overly_permissive(src) or is_overly_permissive(dst)):
                finding = "OVERLY PERMISSIVE"

            if finding:
                print(f"{name:<20} {src:<18} {dst:<18} {service:<10} {finding}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python firewall_audit.py rules.csv")
        sys.exit(1)

    audit_rules(sys.argv[1])
