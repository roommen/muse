import os
from common.CommonDefs import *


def data_upload():
    response = os.path.isfile(HUL_INSTALL_DIR/IS_OFFLINE)

    # File does not exist
    if response is False:
        print("System online")
        return
        # Implement code to read the barcode data stored and insert into the DB
        # Also check for file size limitations - if greater than 5 MB, make it offline store
        # return {"status": "success"}

    print("System offline")
    return
    # Move the barcode scanner data for that time to a separate location of file system
    # return {"status": "fail"}


if __name__ == "__main__":
    data_upload()
