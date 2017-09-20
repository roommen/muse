import mysql.connector
from common.CommonDefs import cnx_str


def create_apikeys():
    connection, cursor = None, None
    try:
        connection = mysql.connector.connect(host=cnx_str['host'], user=cnx_str['username'],
                                             password=cnx_str['password'], database=cnx_str['db'])
        cursor = connection.cursor()
        # Work on this one
        cursor.execute('CREATE TABLE Deployment('
                       'APIKey_ID DOUBLE NOT NULL AUTO_INCREMENT PRIMARY KEY,'
                       'User_ID DOUBLE NOT NULL,'
                       'API_Key VARCHAR(50) NOT NULL,'
                       'CONSTRAINT fk_users_apikeys FOREIGN KEY (User_ID)'
                       'REFERENCES Users(User_ID) ON DELETE CASCADE ON UPDATE RESTRICT)'
                       ';')
        print("Table APIKeys created successfully.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        if connection:
            connection.close()
        if cursor:
            cursor.close()


if __name__ == '__main__':
    create_apikeys()
