import pymysql
import psycopg

def get_connection_mysql(password='your_password'):
    """
    Открывает соединение с MySQL в Docker.
    """
    return pymysql.connect(
        host='127.0.0.1',
        port=3307,
        user='your_user',
        password=password,
        database='your_db',
    )

def get_connection_postgres(password='your_password'):
    """
    Открывает соединение с PostgreSQL в Docker
    """
    return psycopg.connect(
        host='127.0.0.1',
        port=5433,
        user='your_user',
        password=password,
        dbname='your_db',
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
}
