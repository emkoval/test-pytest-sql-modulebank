import pytest
from datetime import datetime
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

def test_select_now(connection, db):
    """
    Выполняет простейший запрос
    и проверяет, что результат получен
    """
    with connection.cursor() as cur:
        cur.execute(db['query'])
        row = cur.fetchone()
    assert row is not None, "Ответ не получен" # ответ получен
    assert isinstance(row[0], datetime), "Не показывает дату/время" # дата и время существуют в ответе, в таком виде должно работать для всех СУБД

@pytest.mark.xfail(strict=True, reason="демонстрация")
def test_wrong_password(db):
    """
    Демонстрация падения с неправильным паролем
    """
    db['connect'](password="wrong")

def test_wrong_password_raises_error(db):
    """
    Не падает, проверяет ошибку
    """
    with pytest.raises(db['error']) as exc:
        db['connect'](password="wrong_password")
    assert db['auth_error_text'] in str(exc.value)