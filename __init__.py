import glob
import os
import time

from .Config import *
from .core import *

version = "v1"
group_username = "@LegendBotSpam"
start_time = time.time()


# Sudo Users
sudos = []
# full debugging
if SUDO_USERS:
    try:
        sudouser = SUDO_USERS
        print(sudouser)
        _list = []
        for x in sudouser:
            _list.append(int(x))
        sudos = _list
    except Exception as e:
        sudos = SUDO_USERS
        print(e)
else:
    print("Add Key Sudo User"
