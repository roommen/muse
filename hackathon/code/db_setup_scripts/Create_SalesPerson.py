import mysql.connector
from common.CommonDefs import cnx_str


def create_salesperson():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE SalesPerson('
                       'SalesPerson_ID DOUBLE NOT NULL PRIMARY KEY,'
                       'First_Name VARCHAR(30) NOT NULL,'
                       'Last_Name VARCHAR(30) NOT NULL'
                       ';')
        print("Table SalesPerson created successfully.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


if __name__ == '__main__':
    create_salesperson()
