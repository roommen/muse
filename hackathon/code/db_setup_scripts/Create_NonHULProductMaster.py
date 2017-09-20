import mysql.connector
from common.CommonDefs import cnx_str


def create_nonhulproductmaster():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE NonHUL_Product_Master('
                       'Barcode VARCHAR(50) NOT NULL PRIMARY KEY,'
                       'Product_Desc VARCHAR(100) NOT NULL,'
                       'Price DOUBLE NOT NULL)'
                       ';')
        print("Table NonHUL_Product_Master created successfully.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


if __name__ == '__main__':
    create_nonhulproductmaster()
