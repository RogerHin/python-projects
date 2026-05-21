import socket

target = input("Enter IP or hostname: ")

ports = [22, 80, 443, 3306, 8080]

print(f"\nScanning {target}...\n")

for port in ports:

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    else:
        print(f"Port {port} is CLOSED")

    scanner.close()