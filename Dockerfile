FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY firewall_audit.py subnet_scan.py ./

CMD ["python", "--help"]
