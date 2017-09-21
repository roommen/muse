import mysql.connector
from common.CommonDefs import cnx_str


def create_cameradata():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE CameraData('
                       'Record_ID DOUBLE NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                       'Store_ID DOUBLE NOT NULL,'
                       'Timestamp VARCHAR(30) NOT NULL,'
                       'Shelf_Number VARCHAR(10) NOT NULL,'
                       'Shelf_Desc VARCHAR(30) NOT NULL,'
                       'Average_Quantity DOUBLE NOT NULL,'
                       'Shelf_Occupancy_Perc DOUBLE NOT NULL,'
                       'Store_Person_Activity DOUBLE NOT NULL,'
                       'Customer_Activity DOUBLE NOT NULL,'
                       'Footfall_Activity DOUBLE NOT NULL,'
                       'Counter_Activity DOUBLE NOT NULL)'
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
