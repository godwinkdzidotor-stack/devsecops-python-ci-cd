# DevSecOps Python CI/CD Pipeline

This repository demonstrates a simple **DevSecOps workflow** for Python security tools using:

- GitHub Actions CI/CD
- Bandit static application security testing (SAST)
- Docker containerization

The pipeline runs on every push and pull request to the `main` branch.

![CI](https://github.com/godwinkdzidotor-stack/devsecops-python-ci-cd/actions/workflows/devsecops.yml/badge.svg)

---

## 🔧 Tools Included

### 1. `firewall_audit.py`

Reads a CSV of firewall rules and flags overly-permissive entries.

Expected columns:

- `name`
- `src`
- `dst`
- `service`
- `action`

Findings:

- `src = any`
- `dst = any`
- `0.0.0.0/0` in source or destination
- `allow` action with overly broad src/dst

Useful for quick firewall audits and security assessments.

---

### 2. `subnet_scan.py`

Simple ICMP reachability scanner for a subnet:

- Walks all hosts in a CIDR
- Sends one ping per host
- Reports reachable hosts

Great for learning network automation and basic troubleshooting.

---

## 🗂 Repository Structure

```text
devsecops-python-ci-cd/
├── firewall_audit.py
├── subnet_scan.py
├── requirements.txt
├── Dockerfile
└── .github/
    └── workflows/
        └── devsecops.yml
