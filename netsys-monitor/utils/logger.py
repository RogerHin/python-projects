from datetime import datetime

def write_log(message):
    with open("logs/netsys_log.txt", "a") as log_file:
        log_file.write(f"{datetime.now()} | {message}\n")