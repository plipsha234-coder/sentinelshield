# SentinelShield: Intrusion Detection & Web Protection System

## Project Overview
SentinelShield is a simulated Web Application Firewall (WAF) and Intrusion Detection System (IDS) designed for educational purposes. It analyzes HTTP requests, detects malicious patterns, applies rate limiting, logs events, and displays security insights.

---

## Features
- SQL Injection detection
- XSS detection
- Command injection detection
- Local File Inclusion detection
- Rate limiting (anti-brute force)
- Real-time logging system
- Security dashboard

---

## Tech Stack
- Python
- Flask
- Regex-based rule engine

---

## How It Works
1. User sends HTTP request
2. WAF engine checks patterns
3. Rate limiter checks request frequency
4. System decides:
   - Allow
   - Block
5. Event is logged
6. Dashboard displays logs

---

## Installation

```bash
pip install -r requirements.txt
python app.py