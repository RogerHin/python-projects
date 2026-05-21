import os
import socket
import subprocess
from datetime import datetime

def ping_host():

    host = input("Enter host: ")

    response = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    if response.returncode == 0:
        print(f"{host} is UP")

    else:
        print(f"{host} is DOWN")

def port_scanner():

    target = input("Enter target: ")

    ports = [22, 80, 443]

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

def system_info():

    print(f"\nCurrent User: {os.getlogin()}")
    print(f"Current Directory: {os.getcwd()}")
    print(f"Current Time: {datetime.now()}")

def show_files():

    files = os.listdir()

    print("\nFiles:\n")

    for file in files:
        print(file)

while True:

    print("\n==== NETSYS MONITOR ====")
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