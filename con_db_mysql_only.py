import pymysql

def get_connection(password='ekmaxk'):
    """
    Открывает соединение с MySQL в Docker.
    """
    return pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='emkoval',
        password=password,
        database='mytestdb',
    )