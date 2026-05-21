import subprocess
from datetime import datetime

hosts = ["google.com", "github.com", "8.8.8.8", "192.168.1.1"]

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

with open("ping_log.txt", "a") as log_file:
    for host in hosts:
        status = ping_host(host)
        current_time = datetime.now()

        result = f"{current_time} | {host} | {status}"

        print(result)
        log_file.write(result + "\n")