import mysql.connector
from common.CommonDefs import cnx_str


def create_store():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE Store('
                       'Store_ID DOUBLE NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                       'Store_Name VARCHAR(100) NOT NULL,'
                       'Pincode VARCHAR(10) NOT NULL'
                       ';')
        print("Table Store created successfully.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


if __name__ == '__main__':
    create_store()
