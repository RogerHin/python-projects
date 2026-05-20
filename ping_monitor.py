import subprocess

def ping_host(host):

    response = subprocess.run(
        ["ping", "-c", "1", host],
        capture_output=True,
        text=True
    )

    if response.returncode == 0:
        print(f"{host} is UP")
    else:
        print(f"{host} is DOWN")

host = input("Enter IP or hostname: ")

ping_host(host)