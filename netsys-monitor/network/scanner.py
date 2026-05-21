import socket
import threading

from utils.logger import write_log
from utils.colors import GREEN, RED, RESET

def scan_single_port(target, port):
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
    scanner.close()

def scan_ports(target, ports):
    threads = []

    for port in ports:
        thread = threading.Thread(
            target=scan_single_port,
            args=(target, port)
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()