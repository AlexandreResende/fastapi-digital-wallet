from pytest import fixture
from sqlalchemy import text

from src.models import Users
from tests.utils.database import TestingSessionLocal, engine

@fixture
def user():
    user = Users(
        username='username',
        password='password',
        email='test@gmail.com',
        first_name='Tester',
        last_name='Testing',
        is_active=True,
        role='admin',
        id=1
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()

    yield user
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM users;'))
        connection.commit()