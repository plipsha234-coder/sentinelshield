import datetime

LOG_FILE = "logs/security.log"

def log_event(ip, request, status, detection):
    time = datetime.datetime.now()

    with open(LOG_FILE, "a") as f:
        f.write(f"{time} | {ip} | {request} | {status} | {detection}\n")