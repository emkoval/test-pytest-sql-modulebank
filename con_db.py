import pymysql
import psycopg
import oracledb

def get_connection_mysql(password='ekmaxk'):
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

def get_connection_postgres(password='ekmaxk'):
    """
    Открывает соединение с PostgreSQL в Docker
    """
    return psycopg.connect(
        host='127.0.0.1',
        port=5433,
        user='emkoval',
        password=password,
        dbname='mytestdb',
    )

def get_connection_oracle(password='ekmaxk'):
    '''
    Открывает соединение с oracle в Docker
    '''
    return oracledb.connect(
        dsn="localhost:1521/FREEPDB1",
        user="emkoval",
        password=password,
    )


DATABASES = {
    'mysql': {
        'connect': get_connection_mysql,
        'query': "SELECT NOW()",
        'error': pymysql.err.OperationalError,
    },
    'postgres': {
        'connect': get_connection_postgres,
        'query': "SELECT NOW()",
        'error': psycopg.OperationalError,
    },
    'oracle': {
        'connect': get_connection_oracle,
        'query': 'select sysdate from dual',
        'error': oracledb.DatabaseError,
    },
}
