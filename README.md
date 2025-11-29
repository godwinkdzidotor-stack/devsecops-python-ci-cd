# DevSecOps Python CI/CD Pipeline

![DevSecOps CI](https://github.com/godwinkdzidotor-stack/devsecops-python-ci-cd/actions/workflows/devsecops.yml/badge.svg)

This repository demonstrates a simple **DevSecOps workflow** for Python security tools using:

- **GitHub Actions CI/CD**
- **Bandit static application security testing (SAST)**
- **Docker containerization**
- Automated artifact upload (Bandit report)

The pipeline runs automatically on every push and pull request to the `main` branch.

---

## 🔧 Tools Included

### `firewall_audit.py`
Reads a CSV of firewall rules and flags overly-permissive entries.

Findings include:

- `src = any`
- `dst = any`
- `0.0.0.0/0` inbound rules
- Any overly broad `allow` rule

Useful for quick firewall audits and security assessments.

---

### `subnet_scan.py`
Simple ICMP reachability scanner for a subnet (CIDR-based):

- Walks all hosts in a CIDR
- Sends one ping per host
- Reports reachable hosts

Great for learning, troubleshooting, and basic automation.

---

## 🗂 Repository Structure

```text
devsecops-python-ci-cd/
├── firewall_audit.py
├── subnet_scan.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .github/
    └── workflows/
        └── devsecops.yml
```


🚀 CI/CD Pipeline Overview

The GitHub Actions workflow at .github/workflows/devsecops.yml runs the following stages:

1️⃣ Syntax Check

Uses python -m py_compile to detect syntax errors early

Fails immediately when invalid Python code is detected

2️⃣ Dependency Installation

Installs all Python packages from requirements.txt

Ensures Bandit and supporting tools are present during CI

3️⃣ Bandit SAST Security Scan

Runs Bandit recursively across the repository:

bandit -r . -f txt -o bandit-report.txt --exit-zero


Produces:

bandit-report.txt as an artifact

Uses --exit-zero so CI always succeeds (ideal for learning and portfolio use)

4️⃣ Docker Image Build

Builds a container image using the included Dockerfile

Ensures the project is fully containerized and build-ready

📦 Local Usage
1. Install dependencies
pip install -r requirements.txt

2. Run firewall audit
python firewall_audit.py rules.csv


Where rules.csv contains the columns:
name, src, dst, service, action.

3. Run subnet scan
python subnet_scan.py 192.168.1.0/24

⚠️ Disclaimer

These tools and the CI/CD workflow are intended for educational and lab use only.
Do not use them on production networks or systems without explicit authorization.
