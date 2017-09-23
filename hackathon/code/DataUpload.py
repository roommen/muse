import os
from common.CommonDefs import *
import csv


def data_upload():
    path_ = HUL_INSTALL_DIR + "/" + IS_OFFLINE
    print(path_)
    response = os.path.isfile(path_)

    # File does not exist
    if response is False:
        print("System online")

        filepath_ = HUL_INSTALL_DIR + "/" + BARCODE_DATA + "/" + BARCODE_DATAFILE
        with open(filepath_) as csvfile:
            readcsv = csv.reader(csvfile, delimiter=',')
            for row in readcsv:
                # start from here
                print(row[0], row[1], row[2])

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
