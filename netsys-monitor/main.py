import os

from network.ping import ping_host
from network.scanner import scan_ports
from system.system_info import get_system_info

from utils.colors import CYAN, YELLOW, RESET

def clear_screen():

    os.system("clear")

def banner():

    print(f"""{CYAN}

███╗   ██╗███████╗████████╗███████╗██╗   ██╗███████╗
████╗  ██║██╔════╝╚══██╔══╝██╔════╝╚██╗ ██╔╝██╔════╝
██╔██╗ ██║█████╗     ██║   ███████╗ ╚████╔╝ ███████╗
██║╚██╗██║██╔══╝     ██║   ╚════██║  ╚██╔╝  ╚════██║
██║ ╚████║███████╗   ██║   ███████║   ██║   ███████║
╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝

{RESET}""")

while True:

    clear_screen()

    banner()

    print(f"{YELLOW}1.{RESET} Ping Host")
    print(f"{YELLOW}2.{RESET} Scan Ports")
    print(f"{YELLOW}3.{RESET} Show System Info")
    print(f"{YELLOW}4.{RESET} Exit")

    choice = input("\nChoose option: ")

    if choice == "1":

        host = input("Enter host: ")

        ping_host(host)

    elif choice == "2":

        target = input("Enter target: ")

        scan_ports(target)

    elif choice == "3":

        info = get_system_info()

        print(f"\nUser: {info['user']}")
        print(f"Directory: {info['directory']}")
        print(f"Time: {info['time']}")

    elif choice == "4":

        print("Goodbye!")
        break

    else:

        print("Invalid option")

    input("\nPress Enter to continue...")