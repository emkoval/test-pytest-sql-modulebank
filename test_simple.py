import pytest
from con_db import DATABASES

@pytest.fixture(params=DATABASES)
def db(request):
    return DATABASES[request.param]

@pytest.fixture
def connection(db):
    """
    Создает и убирает соединение
    """
    connect = db["connect"]()
    yield connect
    connect.close()

# def test_connection_open(connection):
#     assert connection.open
# не работает на универсальный вариант
# но вообще следующий тест по сути содержит эту же проверку

def test_select_now(connection, db):
    """
    Выполняет простейший запрос
    и проверяет, что результат получен
    """
    with connection.cursor() as cur:
        cur.execute(db['query'])
        row = cur.fetchone()
    assert row is not None # ответ получен
    assert row[0] is not None # дата и время существуют в ответе


def test_wrong_password(db):
    """
    Демонстрация падения с неправильным паролем
    """
    db['connect'](password="wrong")

def test_wrong_password_raises_error(db):
    """
    Не падает, проверяет ошибку
    """
    with pytest.raises(db['error']):
        db['connect'](password="wrong_password")