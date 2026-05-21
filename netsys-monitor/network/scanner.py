import socket
from utils.logger import write_log

def scan_ports(target):

    ports = [22, 80, 443, 3306, 8080]

    results = []

    for port in ports:

        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        scanner.settimeout(1)

        result = scanner.connect_ex((target, port))

        if result == 0:
            message = f"PORT_SCAN | {target}:{port} | OPEN"

        else:
            message = f"PORT_SCAN | {target}:{port} | CLOSED"

        write_log(message)

        results.append(message)

        scanner.close()

    return results