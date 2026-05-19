import os
from datetime import datetime
print("==== SYSTEM MONITOR ====")
username = os.getlogin()
print(f"Current user: {username}")
current_time = datetime.now()
print(f"Current Time: {current_time}")
print("======================")