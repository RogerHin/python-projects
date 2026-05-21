from network.ping import ping_host
from network.scanner import scan_ports
from system.system_info import get_system_info

while True:

    print("\n==== NETSYS MONITOR ====")
    print("1. Ping Host")
    print("2. Scan Ports")
    print("3. Show System Info")
    print("4. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":

        host = input("Enter host: ")

        result = ping_host(host)

        print(result)

    elif choice == "2":

        target = input("Enter target: ")

        results = scan_ports(target)

        for result in results:
            print(result)

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