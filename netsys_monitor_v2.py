import os
import socket
import subprocess
from datetime import datetime

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def write_log(message):
    with open("netsys_log.txt", "a") as log_file:
        log_file.write(message + "\n")

def ping_host():
    host = input("Enter host: ")

    response = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    current_time = datetime.now()

    if response.returncode == 0:
        result = f"{current_time} | PING | {host} | UP"
        print(f"{GREEN}{result}{RESET}")
    else:
        result = f"{current_time} | PING | {host} | DOWN"
        print(f"{RED}{result}{RESET}")

    write_log(result)

def port_scanner():
    target = input("Enter target: ")
    ports = [22, 80, 443, 3306, 8080]

    print(f"\nScanning {target}...\n")

    for port in ports:
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)

        result_code = scanner.connect_ex((target, port))
        current_time = datetime.now()

        if result_code == 0:
            result = f"{current_time} | PORT_SCAN | {target}:{port} | OPEN"
            print(f"{GREEN}{result}{RESET}")
        else:
            result = f"{current_time} | PORT_SCAN | {target}:{port} | CLOSED"
            print(f"{RED}{result}{RESET}")

        write_log(result)
        scanner.close()

def system_info():
    print(f"\n{YELLOW}Current User:{RESET} {os.getlogin()}")
    print(f"{YELLOW}Current Directory:{RESET} {os.getcwd()}")
    print(f"{YELLOW}Current Time:{RESET} {datetime.now()}")

def show_files():
    print("\nFiles:\n")
    for file in os.listdir():
        print(file)

while True:
    print("\n==== NETSYS MONITOR V2 ====")
    print("1. Ping Host")
    print("2. Scan Ports")
    print("3. Show System Info")
    print("4. Show Files")
    print("5. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":
        ping_host()
    elif choice == "2":
        port_scanner()
    elif choice == "3":
        system_info()
    elif choice == "4":
        show_files()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option")