import os
from common.CommonDefs import *


# Dynamically determine if the RaPi system is onine or offline
# Depending on which the data upload happens or offline storage for later retrieval
def check_network():
    response = os.system("ping -c 1 " + PING_SERVER)

    if response != 0:
        file_obj_r = open(HUL_INSTALL_DIR+OFFLINE_THRESHOLD, 'r')
        offline_threshold = file_obj_r.read()
        if offline_threshold <= OFFLINE_THRESHOLD_LIMIT:
            offline_threshold += 1
            file_obj_w = open(HUL_INSTALL_DIR+OFFLINE_THRESHOLD, 'w')
            file_obj_w.write(offline_threshold)
            file_obj_w.close()
        else:
            os.system("touch " + HUL_INSTALL_DIR+IS_OFFLINE)
            os.system("echo 1 > " + HUL_INSTALL_DIR+IS_OFFLINE)
        # return {"status": "down"}
        file_obj_r.close()
    else:
        file_obj_r = open(HUL_INSTALL_DIR+ONLINE_THRESHOLD, 'r')
        online_threshold = file_obj_r.read()
        if online_threshold <= ONLINE_THRESHOLD_LIMIT:
            online_threshold += 1
            file_obj_w = open(HUL_INSTALL_DIR + ONLINE_THRESHOLD, 'w')
            file_obj_w.write(online_threshold)
            file_obj_w.close()
        else:
            os.system("rm -f " + HUL_INSTALL_DIR+IS_OFFLINE)
        # return {"status": "up"}
        file_obj_r.close()


if __name__ == "__main__":
    check_network()
