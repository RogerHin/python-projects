import os
from datetime import datetime

def get_system_info():

    info = {
        "user": os.getlogin(),
        "directory": os.getcwd(),
        "time": datetime.now()
    }

    return info