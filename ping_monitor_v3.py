import subprocess
import time
from datetime import datetime

hosts = ["google.com", "github.com", "8.8.8.8"]

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def ping_host(host):

    response = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    if response.returncode == 0:
        return "UP"
    else:
        return "DOWN"

while True:

    print("\n==== NETWORK MONITOR ====\n")

    for host in hosts:

        status = ping_host(host)

        current_time = datetime.now()

        if status == "UP":
            print(f"{GREEN}{current_time} | {host} | {status}{RESET}")

        else:
            print(f"{RED}{current_time} | {host} | {status}{RESET}")

    time.sleep(5)