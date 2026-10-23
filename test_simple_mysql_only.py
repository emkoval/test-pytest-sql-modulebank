import pymysql.err
import pytest
from con_db_mysql_only import get_connection

@pytest.fixture
def connection():
    """
    Создает и убирает соединение
    """
    connect = get_connection()
    yield connect
    connect.close()

def test_connection_open(connection):
    assert connection.open

def test_select_now(connection):
    """
    Выполняет простейший запрос
    и проверяет, что результат получен
    """
    with connection.cursor() as cur:
        cur.execute("SELECT NOW()")
        row = cur.fetchone()
    assert row is not None # ответ получен
    assert row[0] is not None # дата и время существуют в ответе


def test_wrong_password():
    """
    Демонстрация падения с неправильным паролем
    """
    get_connection(password="wrong")

def test_wrong_password_raises_error():
    """
    Не падает, проверяет ошибку
    """
    with pytest.raises(pymysql.err.OperationalError):
        get_connection(password="wrong_password")