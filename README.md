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
├── README.md
└── .github/
└── workflows/
└── devsecops.yml


---

## 🚀 CI/CD Pipeline Overview

### ✔️ 1. Syntax Check
Ensures Python files compile cleanly before running scans or building images.

### ✔️ 2. Dependency Installation
Installs required Python dependencies from `requirements.txt`.

### ✔️ 3. Bandit SAST Scan
Runs Bandit and exports:
- A security report  
- Uploaded as `bandit-report.txt` artifact  

The scan uses `--exit-zero` so the pipeline continues even if vulnerabilities are detected.

### ✔️ 4. Docker Image Build
Builds a Docker image directly inside GitHub Actions.

---

## 🧪 Usage

### Install dependencies locally

```bash
pip install -r requirements.txt


Run firewall audit
python firewall_audit.py rules.csv

Run subnet scan
python subnet_scan.py 192.168.1.0/24

⚠️ Disclaimer

These tools and the CI/CD workflow are intended for educational and lab use only.
Do not use them on production networks without proper authorization.
