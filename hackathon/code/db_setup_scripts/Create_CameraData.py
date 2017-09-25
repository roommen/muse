import mysql.connector
from common.CommonDefs import cnx_str


def create_cameradata():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE CameraData('
                       'Pic_ID DOUBLE NOT NULL PRIMARY KEY,'
                       'Store_ID DOUBLE NOT NULL,'
                       'Person_Count DOUBLE NOT NULL,'
                       'Object_Category VARCHAR(20) NOT NULL,'
                       'Shelf_Fill_Rate DOUBLE NOT NULL)'
                       ';')
        print("Table Camera_Data created successfully.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


if __name__ == '__main__':
    create_cameradata()
