import mysql.connector
from common.CommonDefs import *


def upload_barcode_data(store_id, barcode, datestamp, timestamp):
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        # Create the record for the generated barcode data
        insert_barcode = "INSERT INTO Bar_Code_Data (Store_ID, Barcode, Date_Stamp, Time_Stamp) " \
                         "VALUES('%s', '%s', '%s', '%s')" % (store_id, barcode, datestamp, timestamp)

        cursor = connection.cursor()
        cursor.execute(insert_barcode)
        connection.commit()

        return {"update": "true"}
    except mysql.connector.Error as err:
            return {"update": err}
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


def lambda_handler(event, context):
    store_id = event['sid']
    barcode = event['bc']
    datestamp = event['ds']
    timestamp = event['ts']

    return upload_barcode_data(store_id, barcode, datestamp, timestamp)
