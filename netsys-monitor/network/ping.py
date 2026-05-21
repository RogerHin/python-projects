import subprocess
from utils.logger import write_log

def ping_host(host):
    response = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    if response.returncode == 0:
        result = f"PING | {host} | UP"
    else:
        result = f"PING | {host} | DOWN"

    write_log(result)
    return result