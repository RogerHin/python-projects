import os
from datetime import datetime

def show_user():
    print(f"Current User: {os.getlogin()}")

def show_time():
    print(f"Current Time: {datetime.now()}")

def show_directory():
    print(f"Current Directory: {os.getcwd()}")

def show_files():
    files = os.listdir()
    
    print("Files in current directory:")
    
    for file in files:
        print(file)

while True:

    print("\n==== SYSTEM MONITOR ====")
    print("1. Show current user")
    print("2. Show current time")
    print("3. Show current directory")
    print("4. Show files")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_user()

    elif choice == "2":
        show_time()

    elif choice == "3":
        show_directory()

    elif choice == "4":
        show_files()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option")