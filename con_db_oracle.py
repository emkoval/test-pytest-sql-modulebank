import oracledb

def get_connection(password='ekmaxk'):
    """
    Открывает соединение с oracle в Docker.
    """
    return oracledb.connect(
        dsn="localhost:1521/FREEPDB1",
        user="emkoval",
        password=password,
    )