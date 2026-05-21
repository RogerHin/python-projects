import subprocess

from utils.logger import write_log
from utils.colors import GREEN, RED, RESET

def ping_host(host):

    try:

        response = subprocess.run(
            ["ping", "-c", "1", host],
            capture_output=True,
            text=True
        )

        if response.returncode == 0:
            result = f"PING | {host} | UP"

            print(f"{GREEN}{result}{RESET}")

        else:
            result = f"PING | {host} | DOWN"

            print(f"{RED}{result}{RESET}")

        write_log(result)

        return result

    except Exception as error:

        return f"Error: {error}"