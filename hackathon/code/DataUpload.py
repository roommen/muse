import os
from common.CommonDefs import *
import csv
import requests
import tinys3


def data_upload():
    path_ = HUL_INSTALL_DIR + "/" + IS_OFFLINE
    print(path_)
    response = os.path.isfile(path_)

    # File does not exist - so RaPi system is online
    if response is False:
        upload_barcode_data()
        upload_image_data()

    return {"status": "offline"}
    # TODO: Move the data for that time to a separate location of file system to be copied
    # by a HUL representative on inserting a pendrive when he comes to kirana store


def upload_barcode_data():
    filepath_ = HUL_INSTALL_DIR + "/" + BARCODE_DATA + "/" + BARCODE_DATAFILE
    print(filepath_)
    with open(filepath_) as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        url = 'https://6lgqkmwdt7.execute-api.ap-south-1.amazonaws.com/prod/uploadBarcodeData'
        for row in readcsv:
            # start from here
            # print(row[0], row[1], row[2])
            payload = {'sid': row[0], 'bc': row[1], 'ds': row[2], 'ts': row[3]}
            headers = {}
            requests.post(url, data=payload, headers=headers)
        return {"status": "success"}


def upload_image_data():
    # S3 Access Key removed for submission into Github repo
    conn = tinys3.Connection('S3_ACCESS_KEY', 'S3_SECRET_KEY', tls=True)
    filepath_ = HUL_INSTALL_DIR + "/" + IMAGE_DATA + "/" + IMAGE_DATAFILE
    fileobj = open(filepath_, 'rb')
    conn.upload('some_file.zip', fileobj, 'hul_bucket')


if __name__ == "__main__":
    data_upload()
