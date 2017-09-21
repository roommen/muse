import os
from common.CommonDefs import *


def check_network():
    response = os.system("ping -c 1 " + PING_SERVER)

    if response != 0:
        print("down")
        # Implement code to read from FailThreshold, check OFFLINE_THRESHOLD and update
        # Status file to 0 (offline) accordingly
        # return {"status": "down"}

    print("up")
    # Implement code to read from SuccessThreshold, check ONLINE_THRESHOLD and update
    # Status file to 1 (online) accordingly
    # return {"status": "up"}


if __name__ == "__main__":
    check_network()
