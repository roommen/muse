import mysql.connector
from common.CommonDefs import cnx_str


def create_barcodedata():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE BarCodeData('
                       'Record_ID DOUBLE NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                       'Store_ID DOUBLE NOT NULL,'
                       'Barcode VARCHAR(50) NOT NULL,'
                       'Date_Stamp VARCHAR(20) NOT NULL,'
                       'Time_Stamp VARCHAR(20) NOT NULL)'
                       ';')
        print("Table Bar_Code_Data created successfully.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


if __name__ == '__main__':
    create_barcodedata()
