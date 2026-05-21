import socket

from utils.logger import write_log
from utils.colors import GREEN, RED, RESET

def scan_ports(target):

    ports = [22, 80, 443, 3306, 8080]

    results = []

    try:

        for port in ports:

            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            scanner.settimeout(1)

            result = scanner.connect_ex((target, port))

            if result == 0:

                message = f"PORT_SCAN | {target}:{port} | OPEN"

                print(f"{GREEN}{message}{RESET}")

            else:

                message = f"PORT_SCAN | {target}:{port} | CLOSED"

                print(f"{RED}{message}{RESET}")

            write_log(message)

            results.append(message)

            scanner.close()

    except Exception as error:

        print(f"Error: {error}")

    return results